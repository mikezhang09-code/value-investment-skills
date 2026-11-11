#!/usr/bin/env python3
"""Scenario owner-earnings DCF, probability weighting, reverse DCF, EPV and sensitivity grid.

Implements the Step 6 arithmetic in references/intrinsic-value.md so the numbers are
reproducible. Inputs must already have passed Step 2.5 (share count) and Step 3.5
(normalized owner earnings). The JSON this prints is the source for the canonical
figure block -- derive from it, never retype (Key Principle 14).

Usage:
  python3 scenario_dcf.py input.json                  # needs "validation": a PASS file from validate_inputs.py
  python3 scenario_dcf.py input.json --illustrative   # sweeps and teaching examples only; output is labelled

  python3 scenario_dcf.py input.json --reading "H+A total count"   # UNRESOLVED data: one run per reading

Data gate: input.json must name the validation file written by scripts/validate_inputs.py
("validation": "validation_<ticker>_<date>.json", path relative to input.json). The valuation runs on
VERIFIED and on QUALIFIED data (the output then carries the gaps, the PROVISIONAL tag, the conviction
cap and the extra margin of safety). On UNRESOLVED data it runs only as a named reading and gives no
verdict. It always stops if the inputs file changed after validation or if owner_earnings,
diluted_shares, price or net debt were retyped rather than taken from it (references/data-inputs.md).

input.json example (millions, except price and per-share values):
{
  "ticker": "INTU",
  "validation": "validation_INTU_2026-10-10.json",   # required unless --illustrative
  "owner_earnings": 6607,          # OPERATING owner earnings: normalized operating profit x (1 - tax)
                                   #   + D&A - maintenance capex. Pre-interest; stock compensation stays
                                   #   an expense. Taken from the validated inputs file, never retyped
  "reinvestment": {"ronic": 0.30, "terminal_ronic": 0.12,   # REQUIRED. Growth costs g / RONIC each year
                   "basis": "incremental ROIC FY22-FY26: change in NOPAT / change in invested capital"},
  "bridge": [],                    # optional: [{"label": "Spotify stake", "amount": 2549, "reason": "Check 22"}]
                                   #   stakes +, minority interests -, pension deficit -
  "legacy_owner_earnings": null,   # optional: old-definition figure, prints the old method beside the new
  "net_debt": 1136,                # REQUIRED unless "treasury" is given; negative = net cash. Never assume 0.
  "treasury": {                    # preferred (Check 21): net_debt is BUILT from these, not typed
    "cash": 3600, "short_term_investments": 0, "term_deposits": 0, "other_liquid": 0,
    "restricted_cash": 0,           # shown, excluded from net debt
    "debt": [3800, 936],            # every interest-bearing line incl. convertibles/exchangeables
    "subsequent_cash_events": [],   # [{"label": "fine", "amount": -5180}] outflows negative
    "issuer_liquidity": null,       # issuer's own published total, if any
    "issuer_liquidity_includes_restricted": false,
    "reconciling_items": ""         # required if the computed total misses issuer_liquidity by >5%
  },
  "diluted_shares": 277,           # reconciled total from Step 2.5
  "price": 306.96,                 # must have passed P1-P5
  "currency": "USD",               # currency the cash flows are earned in; sets the base rate
  "risk": {"op_profit_declines": 1, "operating_loss_year": false, "moat": "narrow",
           "net_debt_ebitda": 0.0, "cyclical": false, "industry_beta": 1.28, "window": "FY22-FY26"},
  "discount_rate": 0.10,           # optional; defaults to the table rate; any other value needs discount_rate_reason
  "discount_rate_reason": "",
  "epv": {                         # optional; EPV per intrinsic-value.md Method 2
    "after_tax_operating_earnings": 5900,
    "excess_cash": 3000,
    "total_debt": 4136
  },
  "scenarios": [
    {"name": "Disruption", "g1": 0.00, "g2": -0.02, "tg": 0.00,  "p": 0.20},
    {"name": "Bear",       "g1": 0.04, "g2": 0.03,  "tg": 0.02,  "p": 0.25},
    {"name": "Base",       "g1": 0.09, "g2": 0.06,  "tg": 0.03,  "p": 0.40},
    {"name": "Bull",       "g1": 0.13, "g2": 0.09,  "tg": 0.035, "p": 0.15}
  ]
}
g1 = years 1-5 growth, g2 = years 6-10 growth, tg = terminal growth, p = probability.
A scenario may set "r" only together with "r_reason" -- do not lower r to lift the bull case.
A scenario may set "oe_factor" (with "oe_factor_reason") to shift the LEVEL of owner earnings, e.g. 0.8
for a margin-compression case, and its own "ronic".

Output "fair_value" is the one headline figure: the lower of Base and the probability-weighted value.
Each scenario also prints its terminal-value share and a per-share bridge (operations, terminal, net cash).

Reverse DCF holds the Base scenario's terminal growth and g1->g2 step-down fixed and
solves for the g1 that prices the stock. Years 6-10 growth is floored at terminal growth
(or at g1, when g1 itself is below terminal growth) so the implied path never dips below
the terminal rate and then recovers; "g2_floored" in the output says when the floor bound. "implied_return_pct" is the discount rate at which the Base cash flows equal the price:
the annual return the current price offers if the Base case happens. Report it beside
the discount rate in every deliverable. The sensitivity grid shifts Base g1 and g2
together, so its centre cell equals the Base scenario value.
"""
import hashlib
import json
import os
import sys

DEFAULT_R = 0.10
RONIC_CAP = 0.60   # house cap on return on new capital, years 1-10 (intrinsic-value.md Step 2b)
# Currency rate table, references/intrinsic-value.md Method 1 Step 3. Yields of 2026-10-09.
# rate = 10% USD hurdle + (local 10y yield - US 10y yield), rounded to 0.5pt, floor 8%.
RATE_TABLE_DATE = "2026-10-09"
RATE_TABLE = {"USD": (0.10, 0.030), "HKD": (0.09, 0.020), "RMB": (0.08, 0.010), "CNY": (0.08, 0.010),
              "INR": (0.12, 0.050), "JPY": (0.08, 0.010), "SGD": (0.08, 0.010), "TWD": (0.08, 0.010)}  # (rate, max terminal growth)


def enterprise_parts(oe, g1, g2, tg, r, ronic, tronic):
    """PV of years 1-10 and of the terminal value, on OPERATING owner earnings (pre-interest, after tax).
    Growth is not free: each year reinvests g / RONIC of owner earnings; the terminal year reinvests
    tg / terminal RONIC. With terminal RONIC == r, perpetual growth adds no value beyond year 11's own step."""
    if r <= tg:
        raise ValueError(f"discount rate {r} must exceed terminal growth {tg}")
    pv, cash = 0.0, oe
    for year in range(1, 11):
        g = g1 if year <= 5 else g2
        cash *= 1 + g
        pv += cash * (1 - max(g, 0.0) / ronic) / (1 + r) ** year
    terminal = cash * (1 + tg) * (1 - max(tg, 0.0) / tronic) / (r - tg) / (1 + r) ** 10
    return pv, terminal


def per_share_value(oe, g1, g2, tg, r, net_debt, shares, ronic, tronic, bridge=0.0):
    """Equity value per share = enterprise value - net debt + other bridge items (stakes +, minorities -).
    Owner earnings are pre-interest, so net cash is added once and debt deducted once."""
    pv, terminal = enterprise_parts(oe, g1, g2, tg, r, ronic, tronic)
    return (pv + terminal - net_debt + bridge) / shares


def mos_pct(value, price):
    # Margin of safety relative to intrinsic value; undefined when value <= 0.
    return None if value <= 0 else round((1 - price / value) * 100, 1)


def implied_g2(g1, step, tg):
    # Step-down from g1, but never below terminal growth unless g1 itself is below it.
    return max(g1 + step, min(g1, tg))


def reverse_dcf(oe, price, r, net_debt, shares, tg, step, ronic, tronic, bridge, lo=-0.30, hi=0.60):
    """Solve g1 (with g2 = implied_g2(g1)) so that value == price. None if outside [lo, hi]."""
    hi = min(hi, ronic * 0.999)      # growth above RONIC cannot be self-funded; value stops rising there
    f = lambda g: per_share_value(oe, g, implied_g2(g, step, tg), tg, r, net_debt, shares, ronic, tronic, bridge) - price
    if f(lo) > 0 or f(hi) < 0:
        return None
    for _ in range(100):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def implied_return(oe, price, net_debt, shares, g1, g2, tg, ronic, tronic, bridge, lo=None, hi=0.60):
    """Discount rate at which the Base cash flows are worth exactly the price (an IRR).
    Needs no discount-rate choice. None if no solution between tg and 60%."""
    lo = tg + 0.002 if lo is None else lo
    f = lambda r: per_share_value(oe, g1, g2, tg, r, net_debt, shares, ronic, tronic, bridge) - price
    if f(lo) < 0 or f(hi) > 0:
        return None
    for _ in range(100):
        mid = (lo + hi) / 2
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def risk_adjustment(risk):
    """Step 3b: one-directional business-risk addition, 0 to +2.0 points. Returns (decimal, parts)."""
    downs = int(risk.get("op_profit_declines", 0))
    var = 2.0 if risk.get("operating_loss_year") or downs >= 4 else {0: 0.0, 1: 0.5, 2: 1.0, 3: 1.5}[downs]
    moat = {"wide": 0.0, "narrow": 0.5, "none": 1.0}[risk.get("moat", "narrow")]
    nd = float(risk.get("net_debt_ebitda", 0.0))
    lev = 0.0 if nd <= 1 else (0.5 if nd <= 2.5 else 1.0)
    cyc = 1.0 if risk.get("cyclical") else 0.0
    total = min(2.0, var + moat + lev + cyc)
    return total / 100, {"variability": var, "moat": moat, "leverage": lev, "cyclical": cyc,
                         "total_pts": total, "window": risk.get("window", "not stated")}


def build_net_debt(t):
    """Check 21 R1/R2: net debt from every treasury line, reconciled to the issuer headline."""
    for k in ("cash", "short_term_investments", "term_deposits", "debt"):
        if t.get(k) is None:
            sys.exit(f"STOP: treasury.{k} is missing. Record 0 explicitly if the issuer has none "
                     f"(Check 21 R1: an absent treasury line is how TCOM lost RMB59.3B).")
    debt = t["debt"] if isinstance(t["debt"], (int, float)) else sum(t["debt"])
    gross = t["cash"] + t["short_term_investments"] + t["term_deposits"] + t.get("other_liquid", 0)
    events = sum(e.get("amount", 0) for e in t.get("subsequent_cash_events", []))
    info = {"gross_cash_like": gross, "total_debt": debt, "subsequent_events": events,
            "net_cash": gross - debt + events}
    hl = t.get("issuer_liquidity")
    if hl:
        ours = gross + (t.get("restricted_cash", 0) if t.get("issuer_liquidity_includes_restricted") else 0)
        gap = abs(ours - hl) / hl
        info["issuer_liquidity_gap_pct"] = round(gap * 100, 2)
        if gap > 0.05 and not t.get("reconciling_items"):
            sys.exit(f"STOP: treasury lines total {ours:,.0f} vs issuer-published {hl:,.0f} "
                     f"({gap:.1%} gap). A line is missing, or list treasury.reconciling_items (Check 21 R2).")
    return -(gross - debt + events), info


def check_validation(cfg, cfg_path, reading=None):
    """Data gate. The valuation always runs; the stamp says how far it can be trusted.
    VERIFIED / QUALIFIED: the four figures that drive value must be the validated ones.
    UNRESOLVED: runs only as one named reading of the conflicting number, and carries no verdict."""
    ref = cfg.get("validation")
    if not ref:
        sys.exit("STOP: no 'validation' file named. Run scripts/validate_inputs.py on the inputs file "
                 "first, or pass --illustrative for a sweep that will not be published.")
    vpath = ref if os.path.isabs(ref) else os.path.join(os.path.dirname(os.path.abspath(cfg_path)), ref)
    try:
        with open(vpath, encoding="utf-8") as fh:
            v = json.load(fh)
    except OSError as e:
        sys.exit(f"STOP: validation file not readable ({e}).")
    status = v.get("status")
    if status not in ("VERIFIED", "QUALIFIED", "UNRESOLVED"):
        sys.exit(f"STOP: validation status is {status}. Run validate_inputs.py at the final stage.")
    ipath = os.path.join(os.path.dirname(vpath), v.get("inputs_file", ""))
    try:
        with open(ipath, "rb") as fh:
            digest = hashlib.sha256(fh.read()).hexdigest()
    except OSError as e:
        sys.exit(f"STOP: inputs file behind the validation is not readable ({e}).")
    if digest != v.get("inputs_sha256"):
        sys.exit("STOP: the inputs file changed after it was validated. Re-run validate_inputs.py.")
    gate = {"status": status, "file": os.path.basename(vpath), "inputs_sha256": digest[:12],
            "measured_roic": (v.get("derived") or {}).get("roic"),
            "consequences": v.get("consequences", {}), "gaps": v.get("gaps", []), "conflicts": v.get("conflicts", []),
            "not_validated": []}
    if status == "UNRESOLVED":
        if not reading:
            sys.exit("STOP: the data is UNRESOLVED — a number that drives value disagrees with its cross-check:\n  "
                     + "\n  ".join(v.get("conflicts", [])) +
                     "\nRun once per reading with --reading \"<which figure is used>\"; the report shows each "
                     "reading and gives no verdict.")
        gate["reading"] = reading
        return gate
    d = v.get("derived", {})
    pairs = [("owner_earnings", cfg["owner_earnings"], [d.get("owner_earnings")]),
             ("diluted_shares", cfg["diluted_shares"], [d.get("valuation_count")]),
             ("net_debt", cfg["net_debt"], [d.get("net_debt")]),
             ("price", cfg["price"], [d.get("price"), d.get("price_in_reporting_currency")])]
    for name, ours, refs in pairs:
        refs = [r for r in refs if r is not None]
        if not refs:
            gate["not_validated"].append(name)          # a gap: the report must say so
        elif not any(abs(ours - r) <= max(1e-9, 0.001 * abs(r)) for r in refs):
            sys.exit(f"STOP: {name} {ours:,} is not the validated figure {refs}. Derive it from the "
                     f"inputs file, never retype.")
    return gate


def main(path, illustrative=False, reading=None):
    with open(path) as fh:
        cfg = json.load(fh)
    warnings = []

    treasury_info = None
    if cfg.get("treasury"):
        built, treasury_info = build_net_debt(cfg["treasury"])
        if cfg.get("net_debt") is not None and abs(cfg["net_debt"] - built) > max(1.0, 0.01 * abs(built)):
            sys.exit(f"STOP: net_debt {cfg['net_debt']:,.0f} disagrees with the treasury lines "
                     f"({built:,.0f}). Use one figure (Check 21 R3/R4).")
        cfg["net_debt"] = built
    else:
        warnings.append("net_debt typed in, not built from a 'treasury' block (Check 21 R1): "
                        "confirm every cash, deposit and investment line is included")
    for key in ("owner_earnings", "net_debt", "diluted_shares", "price", "scenarios"):
        if cfg.get(key) is None:
            sys.exit(f"STOP: '{key}' is missing or empty. Re-source it before valuing "
                     f"(a missing debt figure is a gate failure, not zero).")
    oe, nd, sh, price = cfg["owner_earnings"], cfg["net_debt"], cfg["diluted_shares"], cfg["price"]
    if sh <= 0 or price <= 0:
        sys.exit("STOP: diluted_shares and price must be positive.")
    if illustrative:
        gate = {"status": "UNVALIDATED", "note": "illustrative run — figures may not be published"}
        warnings.append("UNVALIDATED: --illustrative run; no figure here may enter a report or the command center")
    else:
        gate = check_validation(cfg, path, reading)
        if gate["status"] == "QUALIFIED":
            c = gate["consequences"]
            warnings.append(f"QUALIFIED data ({len(gate['gaps'])} gap(s)): verdict PROVISIONAL, conviction capped at "
                            f"{c.get('conviction_cap')}/10, required margin of safety +{c.get('margin_of_safety_add_pts')} points")
            if gate["not_validated"]:
                warnings.append(f"not covered by the validation: {gate['not_validated']} — say so beside every figure built on them")
        elif gate["status"] == "UNRESOLVED":
            warnings.append(f"UNRESOLVED data — this run is ONE reading ('{reading}'). No verdict; margin-of-safety "
                            f"figures here are per-reading and may not be quoted as the fair value")

    ccy = cfg.get("currency", "USD").upper()
    if ccy not in RATE_TABLE:
        sys.exit(f"STOP: currency '{ccy}' is not in the rate table {sorted(RATE_TABLE)}; "
                 f"add it to intrinsic-value.md Step 3 and RATE_TABLE first.")
    base_r, max_tg = RATE_TABLE[ccy]
    risk = cfg.get("risk")
    if risk is None:
        warnings.append("no 'risk' block: rate is the currency base only (Step 3b not applied)")
        adj, parts = 0.0, {}
    else:
        adj, parts = risk_adjustment(risk)
    table_r = base_r + adj
    r = cfg.get("discount_rate", table_r)
    if abs(r - table_r) > 1e-9 and not cfg.get("discount_rate_reason"):
        warnings.append(f"discount_rate {r:.2%} differs from the rule rate {table_r:.2%} "
                        f"({ccy} base {base_r:.1%} + risk {adj*100:+.1f}) with no discount_rate_reason stated")
    beta_check = None
    if risk and risk.get("industry_beta") is not None:
        beta_check = base_r + (risk["industry_beta"] - 1) * 0.05
        if abs(beta_check - r) > 0.01 + 1e-9:
            warnings.append(f"rate {r:.2%} differs from the industry-beta check {beta_check:.2%} by more "
                            f"than 1 point: explain in the report")
    for s_ in cfg["scenarios"]:
        if s_["tg"] > max_tg + 1e-9:
            warnings.append(f"scenario '{s_['name']}' terminal growth {s_['tg']:.1%} exceeds the "
                            f"{ccy} cap of {max_tg:.1%}")

    # Reinvestment: what growth costs (intrinsic-value.md Method 1 Step 2b).
    rv = cfg.get("reinvestment") or {}
    if not rv.get("ronic") or not rv.get("terminal_ronic"):
        sys.exit("STOP: 'reinvestment' needs 'ronic' (return on new invested capital, years 1-10, read from the "
                 "measured incremental ROIC) and 'terminal_ronic' (r for no moat, r+2 narrow, r+4 wide). "
                 "Growth is not free — intrinsic-value.md Method 1 Step 2b.")
    ronic, tronic = float(rv["ronic"]), float(rv["terminal_ronic"])
    if ronic > RONIC_CAP + 1e-9:
        warnings.append(f"ronic {ronic:.0%} is above the house cap of {RONIC_CAP:.0%}: even a capital-light business "
                        f"pays something for growth")
    if not rv.get("basis"):
        warnings.append("reinvestment.basis not stated: say how RONIC was measured (window, numerator, denominator)")
    moat = (risk or {}).get("moat")
    cap = r + {"wide": 0.04, "narrow": 0.02, "none": 0.0}.get(moat, 0.02)
    if tronic > cap + 1e-9:
        warnings.append(f"terminal_ronic {tronic:.1%} exceeds the cap {cap:.1%} for a '{moat or 'unstated'}' moat "
                        f"(r + 0 / 2 / 4 points): excess returns are assumed to last forever")
    if tronic > ronic + 1e-9:
        warnings.append(f"terminal_ronic {tronic:.1%} is above the explicit-period ronic {ronic:.1%}")
    seen = gate.get("measured_roic") if isinstance(gate, dict) else None
    if seen:
        top = min(RONIC_CAP, max(x for x in (seen.get("average"), seen.get("incremental"), seen.get("organic_average"),
                                             seen.get("organic_incremental")) if x is not None))
        if ronic > top + 1e-9:
            warnings.append(f"ronic {ronic:.1%} is above the measured return on capital (average {seen.get('average')}, "
                            f"incremental {seen.get('incremental')}, organic {seen.get('organic_average')} / "
                            f"{seen.get('organic_incremental')}, {seen.get('window')}; house cap {RONIC_CAP:.0%}): justify or lower it")
    elif not illustrative:
        warnings.append("no measured ROIC in the validation (statement rows carry no 'invested_capital'): "
                        "the RONIC rests on the stated basis alone")
    bridge_items = cfg.get("bridge") or []
    for b_ in bridge_items:
        if not isinstance(b_.get("amount"), (int, float)) or not b_.get("reason"):
            sys.exit(f"STOP: bridge item '{b_.get('label')}' needs an amount and a reason "
                     f"(stakes +, minority interests -, pension deficit -).")
    bridge = sum(b_["amount"] for b_ in bridge_items)

    scen = cfg["scenarios"]
    total_p = sum(s["p"] for s in scen)
    if abs(total_p - 1) > 1e-6:
        sys.exit(f"STOP: probabilities sum to {total_p}, not 1")
    names = [s["name"] for s in scen]
    if len(set(names)) != len(names):
        sys.exit("STOP: scenario names must be unique")

    out = {"ticker": cfg.get("ticker"), "data_gate": gate, "price": price, "currency": ccy, "discount_rate": r,
           "method": "operating owner earnings (pre-interest, after tax), growth charged at g / RONIC",
           "reinvestment": {"ronic": ronic, "terminal_ronic": tronic, "terminal_ronic_cap": round(cap, 4),
                            "basis": rv.get("basis", "")},
           "net_debt_used": nd, "bridge": {"items": bridge_items, "total": bridge}, "treasury": treasury_info,
           "rate_build": {"currency_base": base_r, "risk": parts},
           "industry_beta_check": None if beta_check is None else round(beta_check, 4), "scenarios": []}
    weighted = 0.0
    for s in scen:
        sr = s.get("r", r)
        if "r" in s and not s.get("r_reason"):
            warnings.append(f"scenario '{s['name']}' overrides r without r_reason")
        factor, s_ronic = s.get("oe_factor", 1.0), s.get("ronic", ronic)
        if factor != 1.0 and not s.get("oe_factor_reason"):
            warnings.append(f"scenario '{s['name']}' shifts the owner-earnings level (oe_factor {factor}) without oe_factor_reason")
        for label, g in (("g1", s["g1"]), ("g2", s["g2"])):
            if g >= s_ronic:
                warnings.append(f"scenario '{s['name']}' {label} {g:.1%} is not self-funded at RONIC {s_ronic:.1%}: "
                                f"it needs outside capital (debt or new shares) the model does not charge")
        pv, tv = enterprise_parts(oe * factor, s["g1"], s["g2"], s["tg"], sr, s_ronic, tronic)
        v = (pv + tv - nd + bridge) / sh
        weighted += v * s["p"]
        if v <= 0:
            warnings.append(f"scenario '{s['name']}' value is <= 0; equity is impaired in it")
        out["scenarios"].append({**s, "value_per_share": round(v, 2), "mos_pct": mos_pct(v, price),
                                 "terminal_value_share_pct": round(tv / (pv + tv) * 100, 1) if pv + tv > 0 else None,
                                 "per_share_bridge": {"operations_years_1_10": round(pv / sh, 2), "terminal": round(tv / sh, 2),
                                                      "net_cash": round(-nd / sh, 2), "other": round(bridge / sh, 2)}})
    out["weighted_iv"] = round(weighted, 2)
    out["weighted_mos_pct"] = mos_pct(weighted, price)

    # Zero-growth capitalization of owner earnings -- NOT the EPV of intrinsic-value.md.
    out["zero_growth_oe_value"] = round((oe / r - nd + bridge) / sh, 2)
    epv = cfg.get("epv")
    if epv:
        if treasury_info and abs((epv["excess_cash"] - epv["total_debt"]) - (-nd)) > max(1.0, 0.01 * abs(nd)) \
                and not epv.get("excess_cash_reason"):
            warnings.append("epv excess_cash - total_debt differs from treasury net cash: state "
                            "epv.excess_cash_reason (e.g. operating cash held back) or align (Check 21 R4)")
        # Bridge items (stakes, minorities) belong in every per-share figure, as in zero_growth_oe_value.
        equity = epv["after_tax_operating_earnings"] / r + epv["excess_cash"] - epv["total_debt"] + bridge
        out["epv_per_share"] = round(equity / sh, 2)
    else:
        out["epv_per_share"] = None
        warnings.append("no 'epv' block: EPV not computed (zero_growth_oe_value is not EPV)")

    base = next((s for s in scen if s["name"].lower().startswith("base")), None)
    if base is None:
        sys.exit("STOP: one scenario must be named 'Base'")
    # ONE headline figure (intrinsic-value.md "Fair value"): the lower of Base and the probability-weighted
    # value. Margin of safety, entry zone and verdict are struck on it and on nothing else.
    base_v = next(x["value_per_share"] for x in out["scenarios"] if x["name"] == base["name"])
    fv = min(base_v, out["weighted_iv"]) if len(scen) > 1 else base_v
    out["fair_value"] = fv
    out["fair_value_basis"] = ("Base (single scenario)" if len(scen) == 1 else
                               "probability-weighted (below Base)" if out["weighted_iv"] < base_v else
                               "Base (probability-weighted is higher and is not used)")
    out["fair_value_mos_pct"] = mos_pct(fv, price)
    b_oe, b_ronic = oe * base.get("oe_factor", 1.0), base.get("ronic", ronic)
    step = base["g2"] - base["g1"]
    g_rev = reverse_dcf(b_oe, price, r, nd, sh, base["tg"], step, b_ronic, tronic, bridge)
    out["reverse_dcf"] = {
        "implied_g1_pct": None if g_rev is None else round(g_rev * 100, 2),
        "implied_g2_pct": None if g_rev is None else round(implied_g2(g_rev, step, base["tg"]) * 100, 2),
        "g2_floored": None if g_rev is None else implied_g2(g_rev, step, base["tg"]) > g_rev + step + 1e-12,
        "held_fixed": {"tg": base["tg"], "g2_minus_g1": round(step, 4), "r": r},
    }
    if g_rev is None:
        warnings.append("reverse DCF has no solution in g1 between -30% and the RONIC ceiling; "
                        "the price implies growth outside that range (or is below net cash) -- check inputs")

    ir = implied_return(b_oe, price, nd, sh, base["g1"], base["g2"], base["tg"], b_ronic, tronic, bridge)
    out["implied_return_pct"] = None if ir is None else round(ir * 100, 2)
    out["discount_rate_basis"] = cfg.get("discount_rate_basis") or (f"{ccy} base {base_r:.1%} + risk {adj*100:.1f} (table {RATE_TABLE_DATE})" if abs(r - table_r) < 1e-9 else cfg.get("discount_rate_reason", ""))
    if ir is None:
        warnings.append("implied return has no solution between terminal growth and 60%")

    # Transition (intrinsic-value.md change log 2026-11-10): the old method, for one side-by-side print.
    if cfg.get("legacy_owner_earnings") is not None:
        cash, pv = cfg["legacy_owner_earnings"], 0.0
        for year in range(1, 11):
            cash *= 1 + (base["g1"] if year <= 5 else base["g2"])
            pv += cash / (1 + r) ** year
        tvl = cash * (1 + base["tg"]) / (r - base["tg"]) / (1 + r) ** 10
        out["legacy_method_base"] = {"value_per_share": round((pv + tvl - nd + bridge) / sh, 2),
                                     "note": "pre-2026-11-10 method: net-income-based owner earnings, growth free, "
                                             "net debt deducted again. For the transition comparison only"}

    grid = {}
    for dr in (r - 0.02, r - 0.01, r, r + 0.01, r + 0.02):
        row = {}
        for d in (-0.04, -0.02, 0.0, 0.02, 0.04):
            g1 = base["g1"] + d
            row[f"g1={g1:.1%}"] = (None if dr <= base["tg"] else round(
                per_share_value(b_oe, g1, base["g2"] + d, base["tg"], dr, nd, sh, b_ronic, tronic, bridge), 2))
        grid[f"r={dr:.1%}"] = row
    out["sensitivity_base"] = grid
    out["warnings"] = warnings
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    argv, reading = sys.argv[1:], None
    if "--reading" in argv:
        i = argv.index("--reading")
        if i + 1 >= len(argv):
            sys.exit(__doc__)
        reading = argv[i + 1]
        del argv[i:i + 2]
    args = [a for a in argv if a != "--illustrative"]
    if len(args) != 1:
        sys.exit(__doc__)
    main(args[0], illustrative="--illustrative" in argv, reading=reading)
