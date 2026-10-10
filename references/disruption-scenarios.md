# Disruption Scenarios

Turns the Deflation Sign Test in `moat-analysis.md` into a valuation input. Read at Step 4 when a
technology, regulation, or free alternative could change the **revenue line** of at least one segment
— AI agents, government free-file, open-source substitutes, platform bundling — then carry the result
into Step 6.

A disruption argument that never reaches the valuation is commentary. One that reaches it as a
lowered growth rate in a single DCF is invisible. This file makes it an explicit, probability-weighted
scenario that a reader can disagree with line by line.

## 1. Run the Deflation Sign Test per segment, not per company

Run Tests A, B, C and the Proprietary-Input Counter from `moat-analysis.md` separately for each
reported segment and record a sign:

| Segment | % revenue | % owner earnings | Customer buys | Deflation hits | Retainable? | Proprietary input left once the tech is universal | Sign |
|---|---|---|---|---|---|---|---|

Mixed signs are normal (Intuit: DIY consumer tax negative, small-business platform positive). Weight
segments by owner-earnings contribution, not equally and not by revenue alone.

## 2. Build four scenarios

| Scenario | Definition | Default probability guide |
|---|---|---|
| Disruption | negative-sign segments shrink; positive ones grow slowly; terminal growth ≤ 0% | 15–30% when any core segment is negative-signed |
| Bear | disruption absorbed through price cuts; low single-digit growth | 20–30% |
| Base | management guidance haircut 10–20%, then fade (per `intrinsic-value.md` growth rules) | 35–45% |
| Bull | the technology is net accretive; growth near the top of guidance | 10–20% |

- Probabilities sum to 100%, each justified in one line citing the evidence in §3.
- **Same discount rate in every scenario** (10% default). Do not lower it in the bull case to lift
  value; uncertainty belongs in the probabilities and the cash flows, not in r.
- Owner earnings and share count are the Step 3.5 / Step 2.5 figures in every scenario. Only growth
  and terminal assumptions differ.

## 3. Evidence the probabilities must cite

- Segment growth and unit economics (ARPC, customer counts) from filings and the last two call
  transcripts — the quarterly profit bridge (`quarterly-profit-bridge.md`) isolates the operational
  part of any slowdown
- Whether management is cutting price to defend share — the leading indicator of revenue-line deflation
- Customer counts in the vulnerable segment, not just revenue
- Reverse-DCF implied growth: if the market already prices the disruption scenario, say so

## 4. Tripwires

For each scenario, one observable signal that moves probability toward it, stating **both** an
operational and a valuation condition (Step 10.5 trigger specification rule):

> "TurboTax customer count falls YoY in the next tax season **AND** price > disruption-weighted IV →
> cut to MONITOR."

## 5. Compute and report

Run `scripts/scenario_dcf.py` with the four scenarios. Report, in the Valuation section:

| Scenario | p | g1 / g2 / tg | Value/share | MoS |
|---|---|---|---|---|
| Disruption | | | | |
| Bear | | | | |
| Base | | | | |
| Bull | | | | |
| **Probability-weighted** | 100% | | | |

plus reverse-DCF implied growth, EPV floor, and the Base sensitivity grid. The probability-weighted
value joins the Step 6 triangulation; it does not replace the other methods. Copy figures from the
script's JSON output into the canonical figure block — never retype them.
