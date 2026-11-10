#!/usr/bin/env python3
"""Residual-income valuation with an explicit fade, for banks and insurers.

The primary method for financials (references/intrinsic-value.md, Mandatory Fade Disclosure;
industry-playbooks.md §F.5). Value per share = book value + PV of (ROE - r) x opening book, with ROE
fading linearly from today's normalized level to a terminal level over a stated number of years.
The fade assumption dominates the answer, so the script always prints the fade ladder.

Usage:
  python3 residual_income.py input.json

input.json (per-share figures in the reporting currency):
{
  "ticker": "HDB",
  "bvps": 640.0,                  # book value per share, ex-perpetual (SKILL.md Step 2.5, Check 14)
  "roe": 0.15,                    # normalized ROE today (through-cycle credit cost)
  "payout": 0.32,                 # dividends / earnings; growth in book = ROE x (1 - payout)
  "r": 0.12,                      # cost of equity (validated rates, industry-playbooks.md §F.5)
  "fade_years": 20,               # house calibration for a wide-moat franchise
  "terminal_roe_spread": 0.02,    # terminal ROE = r + spread. 0 = commodity; +0.02 = house wide-moat
  "terminal_growth": 0.055,       # must be below r
  "price": 800.0,
  "ladder": [[10, 0.00], [10, 0.01], [20, 0.02], [30, 0.02]]   # optional extra (years, spread) rungs
}

Output: value per share, its split (book / fade-period residual income / terminal), the justified-P/B
test (VOID where sustainable growth >= r), and the fade ladder including the no-fade rung, which is
reported as undefined rather than omitted when it does not exist.
"""
import json
import sys


def value(bvps, roe0, payout, r, years, roe_t, tg):
    """Returns (value, pv of fade-period residual income, pv of terminal residual income)."""
    if tg >= r:
        raise ValueError("terminal growth must be below the cost of equity")
    book, pv = bvps, 0.0
    for t in range(1, years + 1):
        roe = roe0 + (roe_t - roe0) * t / years
        pv += (roe - r) * book / (1 + r) ** t
        book *= 1 + roe * (1 - payout)
    # After the fade, book grows at tg and earns roe_t for ever.
    terminal = (roe_t - r) * book / (r - tg) / (1 + r) ** years
    return bvps + pv + terminal, pv, terminal


def main(path):
    with open(path) as fh:
        c = json.load(fh)
    for k in ("bvps", "roe", "payout", "r", "fade_years", "terminal_roe_spread", "terminal_growth"):
        if c.get(k) is None:
            sys.exit(f"STOP: '{k}' is missing.")
    b, roe, pay, r, n, sp, tg = (c["bvps"], c["roe"], c["payout"], c["r"], int(c["fade_years"]),
                                 c["terminal_roe_spread"], c["terminal_growth"])
    warnings = []
    g_sust = roe * (1 - pay)
    jpb = {"sustainable_growth": round(g_sust, 4), "r_minus_g": round(r - g_sust, 4)}
    if g_sust >= r:
        jpb.update(status="VOID", reason="ROE x (1 - payout) >= r: justified P/B is negative or explosive; not reported")
    else:
        jpb.update(status="CONDITIONAL" if g_sust >= r - 0.01 else "USABLE",
                   multiple=round((roe - g_sust) / (r - g_sust), 2),
                   note="may not carry primary weight" if g_sust >= r - 0.01 else "count with EPV as one method")
    if tg > (r + sp) * (1 - pay) + 1e-9:
        warnings.append(f"terminal growth {tg:.1%} exceeds what the terminal ROE and payout can fund "
                        f"({(r + sp) * (1 - pay):.1%})")
    v, pv, tv = value(b, roe, pay, r, n, r + sp, tg)
    price = c.get("price")
    out = {"ticker": c.get("ticker"), "method": "residual income, linear ROE fade",
           "inputs": {"bvps": b, "roe": roe, "payout": pay, "r": r, "fade_years": n,
                      "terminal_roe": round(r + sp, 4), "terminal_growth": tg},
           "value_per_share": round(v, 2),
           "split": {"book": round(b, 2), "fade_period_residual_income": round(pv, 2), "terminal": round(tv, 2),
                     "terminal_share_pct": round(tv / v * 100, 1) if v > 0 else None},
           "implied_pb": round(v / b, 2),
           "mos_pct": None if not price or v <= 0 else round((1 - price / v) * 100, 1),
           "justified_pb": jpb}
    rungs = [(10, 0.0), (10, 0.01), (20, 0.0), (20, 0.02), (30, 0.02)] + [tuple(x) for x in c.get("ladder", [])]
    ladder = []
    for yrs, spread in sorted(set(rungs)):
        lv = value(b, roe, pay, r, int(yrs), r + spread, tg)[0]
        ladder.append({"fade_years": int(yrs), "terminal_roe": round(r + spread, 4), "value_per_share": round(lv, 2),
                       "vs_house_pct": round((lv / v - 1) * 100, 1)})
    # No fade: ROE held for ever, book compounding at ROE x (1 - payout).
    if g_sust >= r:
        ladder.append({"fade_years": "none", "terminal_roe": roe, "value_per_share": None,
                       "note": "UNDEFINED — growth at the current ROE and payout is not below r"})
    else:
        nf = b + (roe - r) * b / (r - g_sust)
        ladder.append({"fade_years": "none", "terminal_roe": roe, "value_per_share": round(nf, 2),
                       "vs_house_pct": round((nf / v - 1) * 100, 1)})
    out["fade_ladder"] = ladder
    defined = [x["value_per_share"] for x in ladder if x["value_per_share"] is not None]
    out["fade_ladder_spread_pct"] = round((max(defined) / min(defined) - 1) * 100, 1) if min(defined) > 0 else None
    warnings.append("the fade assumption dominates this value: print the ladder and state which rung is used and why")
    out["warnings"] = warnings
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
