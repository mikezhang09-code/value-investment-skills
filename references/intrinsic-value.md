# Intrinsic Value Calculation Methods

Intrinsic value is what a business is actually worth — independent of what the market says. Graham called it "that value which is determined by the facts." Never rely on a single method. Use at least two, triangulate, and present a range.

---

## ⚠️ Pre-Valuation Anchor Check (MANDATORY)

Before applying any of the methods below, confirm Step 2.5 reconciliation from SKILL.md is complete:

```
□ Market cap reconciliation: computed = published (±5%)
□ EPS back-check: NI ÷ EPS = assumed share count (±2%)
□ Per-share metrics: BV/share × shares = total equity (±5%)
□ Share-class structure: all classes documented (H + A, multi-class, ADRs, etc.)
```

**One wrong share count poisons every per-share intrinsic value.** No method below can compensate for bad inputs. If reconciliation has not been done, return to SKILL.md Step 2.5.

---

## Method 1: Owner Earnings DCF (Buffett's Preferred)

This is the gold standard for high-quality businesses with predictable cash flows.

### Step 1: Calculate Normalized Owner Earnings

Owner earnings represent the cash the business genuinely generates for its owners each year.

```
Owner Earnings = Net Income
               + Depreciation & Amortization
               + Other Non-Cash Charges (stock comp, etc.)
               − Maintenance Capital Expenditure
               ± Normalized Working Capital Changes

Maintenance CapEx Estimation:
  Asset-light business (software, brand): Maintenance CapEx ≈ 10–20% of Total CapEx
  Moderate-asset business (consumer): Maintenance CapEx ≈ 40–60% of Total CapEx
  Capital-intensive business (industrial): Maintenance CapEx ≈ 60–90% of Total CapEx

Use average of last 3–5 years to normalize for one-time items.
```

### Step 2: Determine Growth Rate Assumptions

Be conservative. Buffett says to be skeptical of high growth assumptions.

| Stage | Period | Recommended Approach |
|-------|--------|---------------------|
| Near-term growth | Years 1–5 | Use last 5-yr earnings CAGR, but cap at 15% |
| Mid-term growth | Years 6–10 | Haircut the near-term rate by 30–50% |
| Terminal growth | Year 10+ | Use 2–3% (in line with GDP) |

**Rule**: For most businesses, assume mid-term growth = 50–70% of recent history. If a company grew at 20%, assume 10–12% going forward.

### Step 3: Choose Discount Rate — one hurdle, translated by currency (adopted 2026-10-11)

The discount rate is built in two layers. **Step 3** sets the base: the investor's required return,
translated into the **currency the cash flows are earned in**, because a nominal 10% is a different real
hurdle in renminbi than in rupees. **Step 3b** adds a fixed, one-directional allowance for the
business's own risk. Because business risk now sits in the rate, the required margin of safety is a
single 25% for all going concerns (see "Margin of Safety Calculation") — risk is charged once.

**Rule.** The hurdle is **10% in US dollars**. For another currency:

```
r(currency) = 10% + (local 10-year government yield − US 10-year Treasury yield)
              rounded to the nearest 0.5 point, with a FLOOR of 8%

terminal growth ≤ r − 7 points, and never above the local 10-year yield
```

**Rate table — yields of 9 Oct 2026. Review every January, or when a yield moves more than 1 point.**

| Cash-flow currency | 10-yr yield | Formula result | **Rate used** | Max terminal growth |
|---|---|---|---|---|
| USD | 5.24% | 10.0% | **10.0%** | 3.0% |
| HKD (Hong Kong-earning businesses) | 4.13% ▲ | 8.9% | **9.0%** | 2.0% |
| RMB / CNY | 1.69% | 6.5% | **8.0%** (floor) | 1.0% |
| INR | 7.29% ▲ | 12.1% | **12.0%** | 5.0% |
| JPY | 3.09% | 7.8% | **8.0%** | 1.0% |
| SGD | 2.45% ▲ | 7.2% | **8.0%** (floor) | 1.0% |
| TWD | not fetched ▲ | below floor for any yield under 3.2% | **8.0%** (floor) | 1.0% |

Sources: Trading Economics and FXMacroData, 9 Oct 2026; ▲ = single source.

**How to apply it**
1. **Currency means where the cash is earned, not where the share is listed.** An HK-listed or
   ADR-listed company reporting in RMB uses the RMB rate; value it in RMB and convert the result at spot.
2. **The only per-stock adjustment is Step 3b below** — a fixed, one-directional business-risk
   addition read from data. Free judgment ("safer business", "riskier business") is not a reason. Country and governance risks (VIE structures, trapped cash, withholding)
   stay in the cash flows and haircuts — see `process-lessons.md` Checks 15–16.
3. **The floor is deliberate.** The formula gives 6.5% for RMB. An equity discount rate that low rests
   on interest-rate parity actually holding for a foreign holder; the 8% floor declines to rely on that.
4. **Financials are unchanged.** Banks and insurers keep their cost-of-equity rates as validated
   (`industry-playbooks.md` §F.5, #11-R). This table governs owner-earnings DCFs.
5. **Transition.** Existing command-center rows keep their fair values until their next refresh. The
   first refresh under this table prints fair value at the old rate and at the table rate side by side.
   **A fair value that rises only because the rate changed does not raise the entry zone.**
6. Apply one rate across all scenarios; never lower it in a bull case to lift value.
7. A mixed-currency business uses the currency of the majority of owner earnings, stated in the report.

*Why not "safe business 8–9%, risky business 12–15%"?* That older ladder is withdrawn. It was the
easiest input to tune toward a wanted answer (an undefended 9.5% once lifted base IV by ~9% with no
change in the business). Business risk now enters through Step 3b, mechanically.

### Step 3b: Business-risk adjustment (adopted 2026-10-13)

The currency rate above is the rate for the **steadiest possible business** in that currency. A
business's own risk can only **add** to it — never subtract. Every factor is read from data or from a
score set before the valuation, so the adjustment cannot be tuned toward an answer.

```
rate = currency base rate (Step 3)  +  business-risk adjustment (0 to +2.0 points)

Earnings variability   years in the window with OPERATING PROFIT down >15% YoY
                       0 → 0 · 1 → +0.5 · 2 → +1.0 · 3 → +1.5 · 4+ or any operating-loss year → +2.0
Moat (scorecard /30)   wide (≥24) → 0 · narrow (18–23) → +0.5 · none (<18) → +1.0
Leverage               net debt / EBITDA: ≤1× (or net cash) → 0 · 1–2.5× → +0.5 · >2.5× → +1.0
Cyclical / capital-heavy (autos, semiconductors, batteries, materials, shipping, airlines) → +1.0
Total capped at +2.0.
```

**Rules of use**
1. **Window:** the last 10 fiscal years where available; state the window used. Operating profit, not
   net income (investment marks distort it) and not FCF (working-capital timing distorts it — Moutai's
   FCF fell 48% in FY22 on advance receipts while operating profit rose 18%).
2. **Terminal-growth cap does not rise with the rate.** It stays at the currency table's cap, so a
   riskier business never earns a higher terminal growth rate.
3. **Industry-beta cross-check, printed beside the rate, never used to set it:**
   `check = currency base + (industry levered beta − 1) × 5%` (Damodaran industry tables). If the rate
   and the check differ by more than 1 point, the report says why in one line.
4. **Stock-level beta is shown for reference only.** It measures share-price co-movement, not business
   risk, and is unreliable for China-exposed names (5-year betas of 0.34 for Moutai and 0.47 for CATL
   would imply rates below 6%).
5. **Financials are unchanged** — validated cost-of-equity rates (`industry-playbooks.md` §F.5).
6. **Transition:** as in Step 3 — each name moves at its next refresh, old and new fair values side by
   side; a fair value that rises only because the rate changed does not raise the entry zone.

**Validation (2026-10-13 sweep, seven names).** A first draft that also allowed −1.5 points for
quality lowered the rate for six of seven names and raised it for none — the book is weighted toward
quality, so a two-sided scale works in one direction. The adopted one-sided version gave: Zoom 11.0%,
ServiceNow 10.0%, Tencent 8.0%, Moutai 8.0%, CATL 9.0%, Great Wall 10.0%, TSMC 9.5%, within about one
point of the independent industry-beta check for five of the seven. The cyclical factor was added after
CATL scored as the lowest-risk business on a five-year earnings window. Full record:
`references/discount-rate-draft_2026-10-13.md` (in Project Knowledge: `claude/discount-rate-draft_2026-10-13.md`).

**State the rate even when it is the default.** The verdict box of every deliverable carries the
discount rate and its build-up (e.g. "11.0% = USD base 10.0% + risk 1.0: variability +0.5, narrow moat +0.5"), terminal growth and the industry-beta check, with the **implied return at the
current price** beside it — the discount rate at which the Base cash flows equal today's price
(`implied_return_pct` in `scripts/scenario_dcf.py`). The implied return needs no rate assumption, so
it lets a reader judge the price without arguing about 9% versus 10%.

### Step 4: Calculate Present Value

```
DCF Formula:
  Year N Cash Flow = Owner Earnings × (1 + growth rate)^N
  PV of Year N = Year N Cash Flow / (1 + discount rate)^N

Terminal Value (at Year 10):
  TV = Year 10 Owner Earnings × (1 + terminal growth) / (discount rate − terminal growth)
  PV of Terminal Value = TV / (1 + discount rate)^10

Intrinsic Value = Sum of PV Years 1–10 + PV of Terminal Value + Cash − Debt

Per Share Value = Intrinsic Value / Diluted Shares Outstanding
```

**⚠️ Per-Share Reminder:** "Diluted Shares Outstanding" must equal the reconciled total from Step 2.5 — including ALL share classes (H + A for HK Chinese, Class A + B + C for US dual-class, etc.). Always cross-check by computing: Total IV (RMB B) ÷ Per-Share IV (RMB) = shares (should match reconciliation).

### Step 5: Sensitivity Table

Always present results as a range:

| Growth Rate | Discount Rate 9% | Discount Rate 10% | Discount Rate 11% |
|-------------|-----------------|------------------|------------------|
| Low case (g-2%) | | | |
| Base case (g) | | | |
| High case (g+2%) | | | |

The range of these outcomes is your intrinsic value range.

### Step 6: Probability-Weighted Scenarios (when outcomes are genuinely bimodal)

Where a disruption, regulatory or binary risk makes one base case misleading, value four explicit
scenarios (Disruption / Bear / Base / Bull) with probabilities summing to 100%, each justified in one
line — see `references/disruption-scenarios.md`. Only growth and terminal assumptions differ between
scenarios; owner earnings, share count, net debt and the discount rate are the same.

Run `scripts/scenario_dcf.py` for the arithmetic. It computes the per-scenario values, the
probability-weighted IV, a reverse DCF (Base terminal growth and step-down held fixed), EPV as
defined in Method 2 below (when its `epv` inputs are supplied), and a sensitivity grid whose centre equals Base. It stops on a missing
net-debt figure and warns on an undefended discount rate. Report its warnings; do not suppress them.

---

## Method 2: Earnings Power Value (EPV)

EPV calculates what the business is worth assuming zero growth — only the earnings from existing operations, in perpetuity. It's Buffett's "floor value."

```
EPV = Normalized After-Tax Operating Earnings / Cost of Capital

Normalized EBIT:
  1. Take average operating income over 5–7 years (smooth cyclical effects)
  2. Adjust for one-time items (add back non-recurring costs, remove non-recurring income)
  3. Apply a normal tax rate

After-Tax Operating Earnings = Normalized EBIT × (1 − effective tax rate)

Cost of Capital: Use same discount rate as DCF (8–12%)

EPV = After-Tax Operating Earnings / Discount Rate
Adjusted EPV = EPV + Excess Cash − Total Debt
Per Share EPV = Adjusted EPV / Diluted Shares Outstanding
```

**Interpretation:**
- If Current Price < EPV: The market is pricing in earnings decline — ask why. If the business is stable, this is potentially a great buy.
- If Current Price ≈ EPV: You're paying fair value for current earnings; growth is "free."
- If Current Price >> EPV: The market expects significant growth — the investment relies entirely on that growth materializing.

---

## Method 3: Graham Formula

A quick, rough estimate suitable for simpler, mature businesses. Not suitable for high-growth or capital-light businesses.

```
Intrinsic Value = EPS × (8.5 + 2g) × (4.4 / Y)

Where:
  EPS = trailing twelve month earnings per share (or normalized EPS)
  8.5 = P/E appropriate for a zero-growth company
  2g  = premium for growth (g = expected annual EPS growth rate, %)
  4.4 = Graham's original "normal" AAA bond yield
  Y   = current AAA corporate bond yield (use ~4.5–5.0% in 2024)

Example:
  EPS = $5.00, expected growth = 8%, AAA yield = 4.7%
  IV = $5.00 × (8.5 + 16) × (4.4/4.7)
  IV = $5.00 × 24.5 × 0.936
  IV = $114.7 per share
```

**Limitations of the Graham Formula:**
- Designed for simple, slow-growth businesses
- Does not account for balance sheet strength
- Growth estimate is very sensitive — a 1% change in g changes value materially
- Use as a cross-check only, not primary valuation

---

## Method 4: Dividend Discount Model (DDM)

Best for: mature, dividend-paying businesses with stable payout ratios (utilities, banks, insurance, consumer staples).

```
Gordon Growth Model (simplest DDM):
  Intrinsic Value = D1 / (r − g)

Where:
  D1 = expected dividend next year = Current Dividend × (1 + g)
  r  = required rate of return (8–10%)
  g  = sustainable dividend growth rate

Example:
  Current dividend = $2.50, growth = 5%, required return = 9%
  D1 = $2.50 × 1.05 = $2.625
  IV = $2.625 / (0.09 − 0.05) = $65.63

Multi-Stage DDM (more realistic):
  Stage 1 (Years 1–5): Higher growth phase
  Stage 2 (Year 6+): Steady-state growth
  Use present value of both stages combined
```

**Suitability:**
- Excellent for: REITs, utilities, mature consumer staples, banks with stable dividends
- Poor for: growth companies, companies that reinvest most earnings

---

## Method 5: Asset-Based / NCAV (Graham Deep Value)

For distressed situations, liquidation scenarios, or companies trading below asset value.

```
Net Current Asset Value (NCAV):
  NCAV = Current Assets − Total Liabilities (including long-term)
  NCAV per share = NCAV / Shares Outstanding

Graham's rule: Buy if Price < 2/3 × NCAV per share

Liquidation Value (more conservative):
  Liquidation Value = (Cash × 1.0)
                    + (Receivables × 0.75)
                    + (Inventory × 0.5)
                    + (PP&E × 0.25)
                    − Total Liabilities
```

**When to use:** NCAV analysis is most relevant when:
- The business has no earnings (turnaround situation)
- You are explicitly analyzing downside protection
- The company is in a cyclical downturn and earnings are temporarily depressed

---

## Method 6: Sum-of-the-Parts (SOTP)

**Mandatory** for holding companies, conglomerates, and any business where distinct segments have
materially different economics or would command materially different multiples standalone.
`earnings-quality-and-distortions.md` Class 3 (Type B, holding company portfolios) requires an SOTP
reconciliation; this section is the method it requires.

```
For each part:
  Value = segment metric × justified multiple
          (or a standalone DCF/EPV where the segment merits it)

Then:
  Gross asset value      = Σ (all parts)
  − Net holdco debt
  − Capitalized holdco corporate costs (see below)
  − Tax on unrealized gains where disposal is the realization path
  = Net asset value (NAV)
  NAV per share = NAV / total diluted shares (all classes — Step 2.5 Anchor 4)
```

**Valuing each part:**

| Part type | Basis |
|---|---|
| Listed stake | Market value of the stake × ownership %. Use the market price, not your own IV — the discount you are testing for is the *holdco* discount, not a double-counted subsidiary discount |
| Unlisted operating subsidiary | Peer multiple on the subsidiary's own earnings, or standalone EPV |
| Non-operating assets (property, cash, investments) | Book value if recently marked; independent estimate if stale |
| Loss-making segment | Value it. A negative number is a legitimate SOTP input — do not floor it at zero |

**Holdco corporate costs are a real deduction.** Unallocated head-office cost is a perpetual charge
against the parts. Capitalize it (annual cost ÷ discount rate) and subtract. Omitting this is the
most common way an SOTP overstates NAV.

**The discount question is the whole analysis.** A holdco trading below NAV is not automatically
mispriced. A persistent structural discount — state control, poor capital allocation history, no
realization path, tax friction on disposal — is a *feature* of the security, not a mispricing.

> **Required before any SOTP-based verdict:** state a specific reason the discount narrows, with a
> mechanism and a timeframe. "It is too wide" is not a reason. If no mechanism exists, value the
> stock at the historical average discount rather than at NAV.

### ⚠️ A discount requires a named enforcing mechanism (amendment #14, 2026-07-27)

**Do not apply a holding-company discount because the entity is structurally a holding company.**
Structural resemblance is not a mechanism. Name which of the following is present, and size the
discount to *that*:

| # | Mechanism | What makes it real |
|---|---|---|
| 1 | **Separately listed subsidiary** | The stub is directly observable. The market quotes the discount — you are *measuring* it, not assuming it |
| 2 | **Cross-listing arbitrage** (A/H, ADR+local) | An observable price on the same underlying claim, struck in another venue |
| 3 | **Documented cash-flow leakage** | Minority leakage, trapped regulatory capital, or dividend-upstreaming restrictions **not already removed** by using attributable figures |

**If none is present, apply no discount.** Where the analysis already works from profit and equity
*attributable to owners*, leakage to minorities has been deducted once — applying a discount on top
**double-counts it**.

> **This list is explicitly non-exhaustive.** It enumerates the mechanisms observed to date, not the
> set of mechanisms that can exist. A fourth candidate under consideration is a controlling
> shareholder with a demonstrated history of value transfer — but that is a **governance** discount
> with different sizing logic and a different evidence bar, and it should be argued as such rather
> than folded into the structural list. Extend the table when a new mechanism is found and named;
> do not stretch an existing row to cover it.

**Decompose bundled discounts.** A single range covering "SOE / holdco / leverage" is three claims
wearing one number. Each needs its own mechanism, its own size and its own evidence, or it comes out.

*Live example — China Taiping (0966.HK) vs PICC Group (1339.HK), 2026-07-27.* Both are holding
companies over regulated insurance subsidiaries, and the reflex was to carry the discount across.
It does not transfer. PICC Group's discount is enforced by mechanism 1 — PICC P&C (2328.HK) is
separately listed — plus mechanism 2, an A/H pair: the stub is observable and a 22% discount is
*measured*. China Taiping's subsidiaries are **not** separately listed, there is no A-share twin, and
minority leakage was already removed by working from attributable figures throughout. **No discount
applied.** Materiality: a reflexive 15% would have cut base fair value HK$24.51 → ~HK$20.83, i.e. **to
roughly spot**, converting a WATCHLIST carrying 15% margin of safety into a false PASS on a
manufactured number.

### ⚠️ The duplicate-exposure test (amendment 2026-07-26)

**When one listed stake is the large majority of a holdco's value, holdco-vs-NAV is the wrong
comparison. The right one is holdco vs. owning the subsidiary directly.**

```
Stake concentration = (listed stake at market) ÷ (holdco market cap)
```

| Concentration | Reading |
|---|---|
| > 80% | **Run the duplicate-exposure test — it usually decides the case.** The holdco is a wrapper |
| 50–80% | Test as a cross-check |
| < 50% | Genuine conglomerate; standard SOTP governs |

Above ~80%, buying the holdco is substantially buying the subsidiary plus a bundle of *everything
else the holdco contains*, wrapped in a discount. Ask directly:

1. What does the holdco give me that owning the subsidiary directly does not? (Usually: nothing —
   no control, no better access, no cheaper entry.)
2. What does it *add*? (Corporate cost, a tax layer on realization, the other subsidiaries' economics,
   governance distance, and a discount that may never close.)
3. **Is the discount large enough to pay for what it adds?**

If the answer to (3) is no, the subsidiary is the better instrument and the holdco is a WATCHLIST at
best regardless of how wide the NAV discount looks.

*Live example — PICC Group (1339.HK), 2026-07-26.* The 68.98% PICC P&C stake at market was **95.3%**
of group market cap (112.7% at the lower price print), so ~95% of the capital bought an exposure
available directly and more cleanly at 2328.HK — plus a life insurer writing over 40% of the sector's
loss-making new business, inside a discount with no closing mechanism. The duplicate-exposure test,
not the NAV discount, decided the verdict.

> **Portfolio consequence.** A parent and its listed subsidiary are **one exposure held two ways, not
> two positions.** If both are held, the combined position cap is the subsidiary's cap — **never the
> sum.** Record them as a single line for concentration purposes.

**Error checks (both are on the `data-sources.md` red-flag list):**
- **RF-1** — no pending M&A embedded on both sides. A target being acquired must appear once: either
  as consideration outflow or as an acquired asset, never as both.
- **RF-2** — every stake percentage verified from a filing, listed *and* unlisted. Unverified stakes
  are the canonical double-count setup.

Also confirm the sum of segment earnings reconciles to consolidated earnings before you start; if it
does not, the segments are not exhaustive and something is being valued at zero by omission.

---

## ⚠️ Mandatory Fade Disclosure (financials) — amendment #11-R, 2026-07-26 · **VALIDATED · BINDING**

> **Status: validated on ICICI Bank (IBN), same day.** The scheduled validation ran and **confirmed
> the rule while proving the original threshold too weak.** IBN — non-merged, CASA 39%, ROE 16%,
> payout 15.5% — produced a **negative** justified P/B, not merely a fragile one. The problem is
> **general to financials**, not specific to post-merger franchises; HDB was the *milder* case.
> Promoted from provisional to binding.

### The binding condition is g ≥ r, not (r − g) < 3pp

The original draft said "demote where (r − g) < 3pp." That understates it. For a bank, g is not free:
**g = ROE × (1 − payout)**. The method therefore requires **payout > 1 − r/ROE**:

| Bank ROE | Minimum payout for justified P/B to function (r = 12%) |
|---|---|
| 14% | 14.3% |
| **16%** | **25.0%** |
| 18% | 33.3% |
| 20% | 40.0% |

High-quality Asian banks retain 80–85% precisely *because* they can redeploy at high returns. They
**systematically fail** this condition. IBN pays 15.5% against a 25.0% requirement.

**The perverse property — the finding that matters.** Higher ROE and lower payout are the two
defining features of a great compounder, and **both push g up toward and past r.** The method is
most reliable on mediocre, high-payout banks and breaks down entirely on exactly the franchises a
value investor most wants to own. This should have been visible from the algebra before either deep
dive was run.

### The rule

1. **Justified P/B may not carry primary weight for any bank or insurer where ROE × (1 − payout) ≥ r − 1pp.** For most high-quality Asian banks this is unconditional.
2. **Where g ≥ r the method is not demoted — it is VOID.** Do not report the output; a negative or explosive fair value is not a data point.
3. The fade-sensitivity ladder remains mandatory. **Where the no-fade rung is undefined, state it as undefined rather than omitting the row** — its absence is itself the diagnostic.
4. Primary anchor is **residual income with an explicit, moat-calibrated fade.**

**Materiality:** applying this rule cut base fair value **~33% on HDB and ~17% on IBN**, in both cases
with negligible FX contribution. It changes verdicts, which raises rather than lowers the burden of
applying it carefully.

**Comparative evidence:**

| | HDB | IBN |
|---|---|---|
| ROE × retention = g | 15.0% × 68.1% = **10.21%** | 16.0% × 84.5% = **13.53%** |
| (r − g) at r = 12% | **+1.78pp** — fragile | **−1.53pp** — broken |
| Justified P/B | 2.68× | **−1.62× (negative)** |
| Fade-ladder spread (defined rungs) | +39% | **+75%** |
| No-fade bound | ₹1,051 | **does not exist** |

For any bank or insurer valued on **justified P/B** or **residual income**, the terminal assumption —
how long above-cost-of-capital returns persist before fading — routinely dominates every other input
in the model. It must be surfaced, not buried.

> ⚠️ **Superseded text removed 2026-07-26 (d).** This section previously ended with a "Two
> requirements" block stating that justified P/B is *"demoted to corroborative where (r − g) < 3pp."*
> **That threshold is superseded by "The rule" above and has been deleted** — it was left in place by
> an incomplete edit and, for roughly one working session, this section contained two contradictory
> thresholds for the same test. The binding condition is **g ≥ r → VOID**. Retained below is only the
> rationale and the live case, neither of which conflicts.

**Why the terminal assumption dominates.** Justified P/B = (ROE − g)/(r − g) is degenerate as
(r − g) → 0 and inverts once (r − g) < 0. And for a bank g is not a free parameter: sustainable
g = ROE × (1 − payout). A bank earning 15% ROE and retaining 68% has an implied g of 10.2%, so an
r of 12% leaves a spread of just 1.8pp — **a narrow spread is the *normal* case for a healthy bank,
not an edge case, and a negative spread is normal for an excellent one.**

*Live case (HDFC Bank, 2026-07-26):* base fair value ranged **₹542 (10-yr fade to r+1%) → ₹1,051
(no fade)** — a **94% swing on one assumption**, from the same ROE and the same discount rate. A
10-year fade to cost of capital is a *commodity* assumption and is indefensible for a franchise with
two decades of 16–18% ROE; no fade is equally indefensible. The house calibration adopted was a
**20-year fade to r+2%, terminal g 5.5%.** Roughly two-thirds of the gap between the resulting fair
value and the sell-side consensus was attributable to this choice alone rather than to any difference
in forecast. **Stating that split is more useful to the reader than the point estimate.**

**Cross-reference:** `industry-playbooks.md` §F.5 already notes that P/B and EPV are not independent
(they converge as normalized ROE → r) and must be counted as one method. This amendment is the
companion constraint on the same family of methods, and **§F.5's method table was corrected on
2026-07-26 (d)** to remove the now-contradictory "Primary anchor" designation for P/B.

---

## Triangulation and Final Estimate

After running at least two methods, compare results:

| Method | Intrinsic Value (per share) | Confidence | Weight |
|--------|----------------------------|-----------|--------|
| Owner Earnings DCF | | | |
| EPV | | | |
| Graham Formula | | | |
| DDM (if applicable) | | | |
| SOTP (if holdco/conglomerate) | | | |
| **Weighted Average** | | | |

**Method selection is not universal.** Financials (insurers, banks) use a different method set —
**residual income with an explicit, moat-calibrated fade as the primary anchor** (justified P/B is
conditional and VOID where g ≥ r — see the Mandatory Fade Disclosure above), EPV as floor, DDM or
SOTP alongside, and **no Graham Formula and no NCAV**. See `industry-playbooks.md` §F.5 before
valuing any financial.
Where the standard DCF-led set is not used, say so explicitly in the report rather than leaving the
reader to assume it was skipped.

**When methods diverge significantly:**
- EPV << DCF: The market is paying a lot for growth. Risky if growth disappoints.
- EPV ≈ DCF: Modest growth expectations. More conservative investment.
- NCAV approach gives much lower value: Company is not trading on asset value; intrinsic value comes from earnings power.

**Final intrinsic value range (always present this way):**
```
Conservative:  $XX (use most pessimistic method or assumptions)
Base case:     $XX (weighted average of methods)
Optimistic:    $XX (most favorable method/assumptions)
Current price: $XX
```

---

## Margin of Safety Calculation

```
Margin of Safety = (Intrinsic Value − Current Price) / Intrinsic Value × 100%

Positive = stock is undervalued (discount to intrinsic value)
Negative = stock is overvalued (premium to intrinsic value)
```

**Required margin of safety (changed 2026-10-13):**

| Situation | Required margin of safety | Rationale |
|-----------|--------------------------|-----------|
| All going concerns | **25%** | Business risk is now priced in the discount rate (Step 3b); a tiered requirement would charge it twice |
| Turnaround or distressed | **40%+** | Outcomes the cash-flow model cannot represent |
| Earnings-quality gate failed (3+ distortion classes) | **+10–15 points** on the above | Unchanged — model-input uncertainty, not business risk |

*Replaces the moat-tiered table (wide 20–25%, narrow 30–35%, cyclical 40–50%).* Existing entry zones
stand until each name's next refresh.

Graham's classic line: *"The margin of safety is the secret of sound investing."*

---

## ⚠️ Output Plausibility Checks (MANDATORY Before Publishing)

A valuation conclusion is only as good as its sanity checks. The most expensive errors in fundamental analysis are not from disagreements about growth rates or discount rates — they are from arithmetic mistakes, wrong share counts, currency confusion, or scale errors that survive into the final report because no one looked at the answer skeptically.

Apply ALL FOUR plausibility tests before reporting valuation conclusions.

### Test 1: The "Too Good to Be True" Test

For a heavily-covered mega-cap stock (top 50 by market cap in any major index, or covered by 20+ analysts), a margin of safety >40% to base-case IV is **rare and warrants skepticism**. The market is not usually that wrong about widely-followed stocks.

**Examples of legitimate large MoS** (rare but real):
- Acute market panic (March 2020, late 2008)
- Specific corporate crisis (Wells Fargo 2016, Boeing post-MAX, Meta Q4 2022)
- Index forced selling (post-S&P deletion)

**Examples of suspicious large MoS** (usually errors):
- "Quiet" mega-cap with no obvious catalyst
- Stock that analyst consensus rates Buy/Hold (if it were truly mispriced, dispersion would be wider)
- Margin of safety primarily driven by one input (share count, growth rate, discount rate)

**Action when triggered:**
1. Return to Step 2.5 reconciliation — verify all four anchors
2. Identify which specific input drives the large MoS
3. Stress-test that input: if it changes ±20%, does the MoS persist?
4. Cross-check against analyst consensus — what specifically do you see differently?

A 40%+ MoS on a mega-cap should require an explicit explanation of "why is the market wrong here?" Default to error probability, not market inefficiency.

**Coverage condition (when Test 1 does NOT apply).** This test derives its force from the number of
professional eyes on the stock. It is not a general rule that large discounts are errors. Test 1 does
not fire by default where:
- Analyst coverage is thin (roughly <5 sell-side analysts), or
- The name is a small/micro-cap outside major indices, or
- The stock was deliberately sourced from a neglect screen, where a wide discount is the *thesis*
  rather than an anomaly

In those cases, substitute Tests 2 and 3 (peer multiple cross-check and reverse DCF) as the primary
discipline — they test the model against observable prices rather than against consensus attention.
State in the report which test set was applied and why. Applying Test 1 by reflex to a neglected name
inverts its purpose: it would systematically talk you out of exactly the setups the neglect screen
exists to find.

### Test 2: Peer Multiple Cross-Check

Compare your implied valuation multiples against industry peers:

| Multiple | Subject | Peer Median | Ratio | Plausibility |
|----------|---------|-------------|-------|--------------|
| P/E | X | Y | X/Y | If ratio < 0.5 or > 2.0, investigate |
| EV/EBITDA | X | Y | X/Y | Same |
| P/B | X | Y | X/Y | Same |

If your "fair value" implies the stock should trade at 2-3x peer multiples while having similar business quality, ask: *why are peers mispriced too?* If they aren't, your model has an error.

Industry peers should be:
- Same primary business
- Similar geographic exposure
- Similar growth profile
- Similar capital structure

For BYD: peers include Geely, Li Auto, NIO, Tesla, Toyota (for scale), Stellantis. Median peer P/E gives an anchor.

### Test 3: Reverse DCF

Instead of solving "what's the stock worth?", solve "what does the market believe?"

```
Current Market Cap = Sum of PV(future cash flows at consensus discount rate)

Solve for: implied long-term growth rate at current price
```

Interpretation:
- **Implied growth 0-3%**: Market expects stagnation. If business is healthy, likely undervalued.
- **Implied growth 4-8%**: Market expects normal economic growth. Likely fairly valued.
- **Implied growth 9-15%**: Market expects strong growth. Justified for high-quality compounders.
- **Implied growth 16-25%**: Market expects exceptional growth. Justified only for early-stage rapid expanders.
- **Implied growth > 25% or negative**: Either rare opportunity OR (more likely) model/data error.

Reverse DCF anchors your conclusion in *what the market believes* rather than just what your model says. It's especially powerful when your forward DCF says "stock is cheap" — reverse DCF tells you exactly how cheap the market thinks it should be.

### Test 4: Analyst Consensus Divergence

If your fair value is >50% above or below analyst consensus, you must identify the specific driving assumption:

**Strong explanations** (suggest you may be right):
- "I'm using a different normalization period — 5-year average earnings vs. their TTM"
- "I'm assuming higher maintenance capex than the Street is modeling"
- "I'm applying a higher discount rate for China political risk"
- "Consensus uses non-GAAP; I'm using GAAP"

**Weak explanations** (suggest you're wrong):
- "Analysts are wrong" (without specifics)
- "The market doesn't understand the business" (rare for covered stocks)
- "Analysts have conflicts of interest" (true generically, but they still have access to better information than you)

**Wider divergence requires stronger explanation.** A 20% gap vs. consensus needs a clear assumption difference. A 100% gap requires a fundamental thesis disagreement that you can articulate in one sentence.

### Stop Conditions

If your output fails 2+ of the four tests:
1. Return to Step 2.5 (reconciliation anchors)
2. Verify all inputs against primary sources
3. Re-run the valuation methods
4. Only publish if you can explain the divergence with a specific, defensible assumption difference

---

## Common Valuation Pitfalls

**1. Using adjusted/non-GAAP earnings without scrutiny**
Companies frequently present "adjusted EPS" that adds back real costs. Always start from GAAP, then make your own adjustments with explicit justification.

**2. Extrapolating recent growth rates indefinitely**
High recent growth (15–20%) often reverts toward GDP growth over time. Be skeptical of models that assume 15% growth for 10+ years.

**3. Terminal value dominates**
In a standard DCF, the terminal value often represents 60–80% of total value. Small changes in terminal growth rate dramatically change the answer. This is why you must be conservative and check with EPV.

**4. Ignoring the balance sheet**
A company with $50/share in debt has the same enterprise value math but the equity value is $50/share less. Always subtract net debt from equity value.

**5. Confusing market cap with enterprise value**
- **Market Cap** = Shares × Price (equity value)
- **Enterprise Value** = Market Cap + Debt − Cash (total business value)
- Valuation multiples should be applied to enterprise value, then subtract debt to get equity value

**6. Currency and cross-border adjustments**
For HK, India, Singapore companies: ensure all numbers are in the same currency before comparing. Use end-of-period exchange rates for balance sheet, average annual rates for income statement (standard practice).

**7. Survivorship bias in comparable companies**
Don't benchmark a company against only the winners in its sector. Include the full competitive set.

**8. Wrong share count (the most common single-point-of-failure error)** ⚠️ NEW
The single most common error in equity valuation is using a wrong share count. This is mechanical, not analytical — and it propagates through every per-share metric (EPS, BV/share, IV/share). Always reconcile share count against reported EPS arithmetic before any per-share calculation. See Step 2.5 in SKILL.md.

Particularly common share-count errors:
- HK-listed Chinese companies: using H-share float instead of total H+A
- US dual-class: omitting non-voting Class C (Google)
- Pre/post-split or pre/post-placement confusion (timing of equity raises)
- Treasury shares not subtracted from "shares issued"
- Dilutive instruments (convertibles, warrants, ESOPs) not added to basic count

---

## Change Log

- **2026-10-13** — **Step 3b business-risk adjustment adopted; margin of safety unified at 25%.** The
  rate is now currency base + a one-directional addition (0 to +2) from operating-profit variability,
  moat, leverage and a cyclical flag; industry beta printed as a cross-check; stock beta reference
  only. Validated on a seven-name sweep in which a two-sided draft failed (6 of 7 rates lowered, 0
  raised). The margin-of-safety tiers collapse to 25% (40%+ turnaround/distressed) so risk is not
  charged twice. Effect: cyclicals and narrow-moat names get higher rates but a smaller required MoS;
  wide-moat steady names keep the base rate and need 25% instead of 20–25%. Each name moves at its next refresh.

- **2026-10-11 (c)** — **Method 1 Step 3 rewritten: currency-based discount-rate table adopted.** One
  hurdle (10% in USD) translated to other currencies by the 10-year government-yield differential,
  rounded to 0.5, floored at 8%; terminal growth capped at r − 7 points and at the local yield. The
  quality-based ladder (8–9% safe … 12–15% risky) is withdrawn. Financials unchanged. **Not validated
  by a retrospective sweep:** the per-name models are not on file, so fair values are not restated;
  each name moves at its next refresh with old-rate and table-rate values shown side by side, and
  entry zones do not rise on a rate change alone. Expected direction: RMB-earning non-financials move
  from 10% to 8% (fair values up); USD names unchanged; HKD-earning names 10% → 9%.

- **2026-07-27** — **Amendment #14: a Method 6 holding-company discount now requires a named
  enforcing mechanism.** **BINDING on adoption** — the rule is a *restraint*, not a number: it demands
  that an assumption be stated rather than imposing a valuation input, so adopting it can only surface
  an assumption, never manufacture one. Derived from the **China Taiping (0966.HK) vs PICC Group
  (1339.HK)** contrast: both are holding companies over regulated insurance subsidiaries, but PICC
  Group's 22% discount is *enforced* by a separately listed subsidiary (PICC P&C, 2328.HK) plus an A/H
  pair — observable stub — while CTIH has no listed subsidiary, no A-share twin, and minority leakage
  already removed via attributable figures. **No discount applied to CTIH.** Materiality: a reflexive
  15% would have cut base FV HK$24.51 → ~HK$20.83, **to roughly spot**, turning a 15%-MoS WATCHLIST
  into a false PASS on a manufactured number. General form: **structural resemblance is not a
  mechanism.** The mechanism table (1–3) is **explicitly non-exhaustive** and is the part still open —
  a fourth candidate (controlling shareholder with a demonstrated history of value transfer) is a
  *governance* discount with different sizing logic and should be argued separately rather than folded
  in. Companion rule added in the same commit: **decompose bundled discounts** — a single "SOE /
  holdco / leverage" range is three claims wearing one number. Retrospective scope: PICC Group (#49)
  **passes** as written; **Shenzhen International (#43)** carries a bundled 30–40% discount ▲ on a name
  where the SOTP *is* the valuation, and is flagged for re-examination.

- **2026-07-26 (d)** — **#11 VALIDATED on ICICI Bank (IBN) → promoted to #11-R, binding.** Threshold
  rewritten from "(r − g) < 3pp" to **g ≥ r**; where g ≥ r the method is **void**, not demoted. IBN
  returned a negative justified P/B (−1.62×). Perverse property identified: the method breaks down
  precisely on high-ROE, low-payout compounders. §F.5 method table corrected in the same commit —
  P/B demoted from primary anchor to conditional; residual income with explicit fade promoted in its
  place. Materiality: ~33% FV cut on HDB, ~17% on IBN.
- **2026-07-26 (c)** — **Amendment #11: Mandatory Fade Disclosure (financials) added.** ⚠ **UNVALIDATED —
  single-case derivation from HDFC Bank (HDB) Q1 FY27 refresh.** Requires the fade-sensitivity ladder
  to be printed for any financial valued on justified P/B or residual income, and demotes justified
  P/B to corroborative where **(r − g) < 3pp**. Derivation: HDB base fair value swung **₹542 → ₹1,051
  (94%)** on the fade assumption alone, from an identical ROE and discount rate; roughly two-thirds of
  the gap to sell-side consensus was attributable to that one choice. Note that for a bank the
  narrow-spread condition is the **normal** case, since sustainable g = ROE × (1 − payout).
  **Scheduled validation: ICICI Bank (IBN)** — non-merged balance sheet in the same market and
  sector. Do not extend beyond financials until validated. Companion to `industry-playbooks.md` §F.5
  (P/B and EPV are not independent — count as one method).
- **2026-07-26 (b)** — Method 6 (SOTP) duplicate-exposure test and the parent/subsidiary
  single-exposure rule for concentration caps added (amendments #6 and #8, PICC session).

> **Commit-letter convention (set 2026-07-26 (d)).** Suffix letters are **session-level, not
> per-file**: (a) file created · (b) PICC session · (c) HDB session · (d) IBN validation session.
> A given letter therefore means the same commit in every knowledge file, so cross-file references
> resolve. Corrected here on 2026-07-26 (d), where the IBN commit had been labelled (c) in this file
> and (d) in `industry-playbooks.md` while a cross-reference in the same file pointed to (d).
