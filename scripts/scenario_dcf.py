#!/usr/bin/env python3
"""Scenario owner-earnings DCF, probability weighting, reverse DCF, EPV and sensitivity grid.

Implements the Step 6 arithmetic in references/intrinsic-value.md so the numbers are
reproducible. Inputs must already have passed Step 2.5 (share count) and Step 3.5
(normalized owner earnings). The JSON this prints is the source for the canonical
figure block -- derive from it, never retype (Key Principle 14).

Usage:
  python3 scenario_dcf.py input.json

input.json example (millions, except price and per-share values):
{
  "ticker": "INTU",
  "owner_earnings": 6607,          # normalized FCF - SBC (Step 3.5)
  "net_debt": 1136,                # REQUIRED; negative = net cash. Never assume 0.
  "diluted_shares": 277,           # reconciled total from Step 2.5
  "price": 306.96,                 # must have passed P1-P5
  "discount_rate": 0.10,           # 10% default; any other value needs discount_rate_reason
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

Reverse DCF holds the Base scenario's terminal growth and g1->g2 step-down fixed and
solves for the g1 that prices the stock. The sensitivity grid shifts Base g1 and g2
together, so its centre cell equals the Base scenario value.
"""
import json
import sys

DEFAULT_R = 0.10


def per_share_value(oe, g1, g2, tg, r, net_debt, shares):
    if r <= tg:
        raise ValueError(f"discount rate {r} must exceed terminal growth {tg}")
    pv, cash = 0.0, oe
    for year in range(1, 11):
        cash *= 1 + (g1 if year <= 5 else g2)
        pv += cash / (1 + r) ** year
    terminal = cash * (1 + tg) / (r - tg) / (1 + r) ** 10
    return (pv + terminal - net_debt) / shares


def mos_pct(value, price):
    # Margin of safety relative to intrinsic value; undefined when value <= 0.
    return None if value <= 0 else round((1 - price / value) * 100, 1)


def reverse_dcf(oe, price, r, net_debt, shares, tg, step, lo=-0.30, hi=0.60):
    """Solve g1 (with g2 = g1 + step) so that value == price. None if outside [lo, hi]."""
    f = lambda g: per_share_value(oe, g, g + step, tg, r, net_debt, shares) - price
    if f(lo) > 0 or f(hi) < 0:
        return None
    for _ in range(100):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main(path):
    with open(path) as fh:
        cfg = json.load(fh)
    warnings = []

    for key in ("owner_earnings", "net_debt", "diluted_shares", "price", "scenarios"):
        if cfg.get(key) is None:
            sys.exit(f"STOP: '{key}' is missing or empty. Re-source it before valuing "
                     f"(a missing debt figure is a gate failure, not zero).")
    oe, nd, sh, price = cfg["owner_earnings"], cfg["net_debt"], cfg["diluted_shares"], cfg["price"]
    if sh <= 0 or price <= 0:
        sys.exit("STOP: diluted_shares and price must be positive.")

    r = cfg.get("discount_rate", DEFAULT_R)
    if abs(r - DEFAULT_R) > 1e-9 and not cfg.get("discount_rate_reason"):
        warnings.append(f"discount_rate {r:.2%} differs from the 10% default with no "
                        f"discount_rate_reason stated")

    scen = cfg["scenarios"]
    total_p = sum(s["p"] for s in scen)
    if abs(total_p - 1) > 1e-6:
        sys.exit(f"STOP: probabilities sum to {total_p}, not 1")
    names = [s["name"] for s in scen]
    if len(set(names)) != len(names):
        sys.exit("STOP: scenario names must be unique")

    out = {"ticker": cfg.get("ticker"), "price": price, "discount_rate": r, "scenarios": []}
    weighted = 0.0
    for s in scen:
        sr = s.get("r", r)
        if "r" in s and not s.get("r_reason"):
            warnings.append(f"scenario '{s['name']}' overrides r without r_reason")
        v = per_share_value(oe, s["g1"], s["g2"], s["tg"], sr, nd, sh)
        weighted += v * s["p"]
        if v <= 0:
            warnings.append(f"scenario '{s['name']}' value is <= 0; equity is impaired in it")
        out["scenarios"].append({**s, "value_per_share": round(v, 2), "mos_pct": mos_pct(v, price)})
    out["weighted_iv"] = round(weighted, 2)
    out["weighted_mos_pct"] = mos_pct(weighted, price)

    # Zero-growth capitalization of owner earnings -- NOT the EPV of intrinsic-value.md.
    out["zero_growth_oe_value"] = round((oe / r - nd) / sh, 2)
    epv = cfg.get("epv")
    if epv:
        equity = epv["after_tax_operating_earnings"] / r + epv["excess_cash"] - epv["total_debt"]
        out["epv_per_share"] = round(equity / sh, 2)
    else:
        out["epv_per_share"] = None
        warnings.append("no 'epv' block: EPV not computed (zero_growth_oe_value is not EPV)")

    base = next((s for s in scen if s["name"].lower().startswith("base")), None)
    if base is None:
        sys.exit("STOP: one scenario must be named 'Base'")
    step = base["g2"] - base["g1"]
    g_rev = reverse_dcf(oe, price, r, nd, sh, base["tg"], step)
    out["reverse_dcf"] = {
        "implied_g1_pct": None if g_rev is None else round(g_rev * 100, 2),
        "implied_g2_pct": None if g_rev is None else round((g_rev + step) * 100, 2),
        "held_fixed": {"tg": base["tg"], "g2_minus_g1": round(step, 4), "r": r},
    }
    if g_rev is None:
        warnings.append("reverse DCF has no solution in g1 between -30% and +60%; "
                        "the price implies growth outside that range -- check inputs")

    grid = {}
    for dr in (r - 0.02, r - 0.01, r, r + 0.01, r + 0.02):
        row = {}
        for d in (-0.04, -0.02, 0.0, 0.02, 0.04):
            g1 = base["g1"] + d
            row[f"g1={g1:.1%}"] = (None if dr <= base["tg"] else round(
                per_share_value(oe, g1, base["g2"] + d, base["tg"], dr, nd, sh), 2))
        grid[f"r={dr:.1%}"] = row
    out["sensitivity_base"] = grid
    out["warnings"] = warnings
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
