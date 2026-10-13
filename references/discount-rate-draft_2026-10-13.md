# Discount rate with business risk — ADOPTED 2026-10-13 (version B)

Status: **adopted by Mike on 2026-10-13** as version B below, with the single 25% margin of safety.
The governing text is `intrinsic-value.md` Method 1 Step 3b; this file is the validation record.

## Rule as drafted (version B, re-centred — recommended)

```
rate = currency base rate (table)  +  business-risk adjustment (0 to +2 points)

Earnings variability   years in the window with operating profit down >15% YoY
                       0 → 0 · 1 → +0.5 · 2 → +1.0 · 3 → +1.5 · 4+ or any loss year → +2.0
Moat (scorecard /30)   wide (≥24) 0 · narrow (18–23) +0.5 · none (<18) +1.0
Leverage               net debt / EBITDA ≤1 → 0 · 1–2.5 → +0.5 · >2.5 → +1.0
Cyclical / capital-heavy business (autos, semis, batteries, materials, shipping)  +1.0
Total capped at +2.0. Window: 10 fiscal years where available.
Terminal growth ≤ rate − 7 points and ≤ local 10-year yield (unchanged).
Cross-check: base + (industry levered beta − 1) × 5%; a gap above 1 point is explained in the report.
Stock-level beta is shown for reference only and is never used to set the rate.
Margin of safety: one 25% requirement for all names; 40%+ for turnarounds and distressed cases.
Financials: unchanged (validated cost-of-equity rates).
```

The currency base is the rate for the steadiest business; risk can only add to it.

## Why version A (−1.5 to +2) was rejected

Tested on seven names, version A lowered the rate for six and raised it for none. Combined with the
currency table it put Tencent, Moutai, CATL and TSMC at the 7% floor, raising their operating value about
22% over the old 10% practice. The book is weighted toward quality businesses, so a two-sided adjustment
centred on "average" works almost entirely in one direction.

## Sweep results (operating value, illustrative common growth path 6% / 4%)

| Name | Currency | Version B rate | Industry-beta check | Stock-beta check | Op. value vs table |
|---|---|---|---|---|---|
| Zoom | USD | 11.0% | 11.4% | 10.2% | −12.8% |
| ServiceNow | USD | 10.0% | 11.4% | 10.0% | 0.0% |
| Tencent | RMB | 8.0% | 11.5% | 6.7% | 0.0% |
| Kweichow Moutai | RMB | 8.0% | 7.0% | 4.7% | 0.0% |
| CATL | RMB | 9.0% | 9.2% | 5.3% | −8.8% |
| Great Wall Motor | RMB | 10.0% | 10.3% | 6.4% | −20.3% |
| TSMC | TWD | 9.5% | 10.6% | 9.2% | −14.9% |

Inputs: operating profit FY21–TTM, net debt and EBITDA, stock betas — StockAnalysis, 9–13 Oct 2026;
industry betas — Damodaran US dataset, January 2026. ServiceNow's moat class (wide) and Great Wall's
(narrow/none) are assumed ▲; their scorecards were not on file.

## Known limits of the sweep

- Only five years plus TTM were available, not ten; this flatters growing cyclicals (CATL showed no
  profit declines in the window).
- Industry betas are US peer groups; for China names they reflect US comparables, not local risk.
- The value effect uses one growth path for all names; real fair-value moves depend on each model and
  on how much of the value is cash.
