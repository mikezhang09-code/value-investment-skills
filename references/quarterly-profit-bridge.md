# Quarterly Profit Bridge

Separates operating deterioration from tax, one-off, non-operating, seasonal and definitional effects
**before** a quarterly profit print is allowed to move the moat view, the growth assumptions or the
verdict. This is the full procedure behind `process-lessons.md` Check 19; Check 19's operating /
non-operating split is step 2 below.

## When to run it

Run it whenever **either** trigger fires — and always at earnings-reaction and thesis-refresh scope:

1. **Consensus trigger (Check 19):** reported profit beats or misses consensus by more than ~5%, in
   either direction.
2. **Divergence trigger:** in any of the last four quarters, net-profit growth diverges from revenue
   growth by more than 10 percentage points, or turns negative while revenue grows.

The second trigger exists because a print can land on consensus and still carry a large non-operating
or tax swing — and because many names, especially outside the US, have thin or no consensus coverage.

## Procedure

### 1. Build an 8-quarter YoY table

Revenue, gross profit, operating profit, each non-operating line, pretax income, tax, net income
attributable, diluted EPS — with the YoY change on every line. Quarterly filings have no notes (see
`process-lessons.md`, "Quarterly filings cannot support a deep dive"); take one-off detail from the
earnings release, the call transcript or the 8-K / HKEx announcement, and cite which.

### 2. Label every line below operating profit O or N

```
Operating profit .......................... O   <- ONLY this may characterise the business
Net gains/losses from investments ......... N
Share of associates and JVs ............... N
Interest income / finance costs ........... N
FX translation / fair-value remeasurement . N
Income tax ................................ N?  (split: rate change vs discrete item)
```

### 3. Walk the bridge in this order and quantify each step

```
Prior-year quarter NI
  + Δ operating profit, organic          (revenue growth × prior margin, plus margin change)
  − one-off charges this quarter         (restructuring, impairment, litigation)
  + one-off charges in prior-year quarter
  ± Δ non-operating income               (associates, investment marks, interest, FX)
  ± Δ tax expense                        (separate: rate change vs prior-year discrete benefit)
= Current-quarter NI                      (must tie to the reported figure; if not, find the gap)
```

**Bridge through pretax income first.** A tax line can reverse the sign of the headline on its own.

### 4. Classify each driver

| Driver | Typical sign | Recurring? | Valuation treatment |
|---|---|---|---|
| Seasonality shift (revenue moves between quarters) | either | timing only | ignore; use full-year or TTM |
| Base effect (prior-year quarter unusually low/high) | either | no | ignore |
| Prior-year discrete tax benefit / charge | either | no | normalize to the guided tax rate |
| Restructuring / impairment | negative | no, unless in 3+ of the last 5 years | add back once; if repeated, treat as an operating cost (Class 6) |
| Associate / investment / FX swing | either | no | Class 13; belongs in the normalisation bridge, not the narrative |
| Non-GAAP definition change (e.g., SBC now included) | either | definitional | restate both years on one definition |
| Price cut / mix down in a core segment | negative | yes | carries into owner earnings and the moat trend |
| Segment growth slowdown | negative | possibly | test against `disruption-scenarios.md` |

### 5. Conclude in one sentence, with numbers

> "Of the X-point gap between revenue and profit growth, Y points are non-recurring (tax, one-offs,
> non-operating); Z points are operational, from [segment]."

**Only the operational Z feeds the growth assumptions, the moat trend and the verdict.**

## Worked examples

**Tencent 2Q2026 — non-operating swing (Class 13).** IFRS operating profit +11.9% at a stable 33%
margin; attributable profit +0.7% because share of associates swung −RMB14.5bn. Operational
component of the "miss": none. Full case in `process-lessons.md` Class 13.

**Intuit FY2026 (fiscal year ends 31 July) — tax base effect and restructuring.**
- Q4: net income −4.7% while pretax income rose ~47.5%. Prior-year Q4 tax was a −$15M benefit versus
  +$177M this year; ~$300M restructuring charge for a 17% workforce cut; non-GAAP EPS +47%.
  Operational component: none negative. An accounting decline, not an operating one.
- Q3 (Feb–Apr, the tax-season quarter): net income +8.7% versus revenue +10.4%. Consumer grew only 8%
  (TurboTax +7%, Pro Tax flat) while the business segment grew 15%; Q1–Q2 had flattered from low
  prior-year bases; tax rate +0.8pp. Operational component: weak DIY tax — the input that feeds the
  disruption scenario.

The two quarters point in opposite directions: the large headline decline (Q4) was noise, and the
small headline gap (Q3) carried the real signal. Size of the headline is not a guide to which matters.
