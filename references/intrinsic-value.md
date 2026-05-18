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

### Step 3: Choose Discount Rate

The discount rate represents the required return. Buffett typically uses the 10-year US Treasury yield + a risk premium.

```
Common discount rates:
  Very safe business (utility, consumer staple): 8–9%
  Good business with some risk: 10%
  Cyclical or moderate-risk business: 11–12%
  Higher-risk or international: 12–15%

Default to 10% for most analyses — it matches Buffett's historical practice.
```

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

## Triangulation and Final Estimate

After running at least two methods, compare results:

| Method | Intrinsic Value (per share) | Confidence | Weight |
|--------|----------------------------|-----------|--------|
| Owner Earnings DCF | | | |
| EPV | | | |
| Graham Formula | | | |
| DDM (if applicable) | | | |
| **Weighted Average** | | | |

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

**Required margin of safety guidelines:**

| Business Quality | Required Margin of Safety | Rationale |
|-----------------|--------------------------|-----------|
| Wide moat, highly predictable | 20–25% | High certainty, lower required discount |
| Narrow moat, good visibility | 30–35% | Moderate uncertainty in projections |
| Cyclical or less predictable | 40–50% | Higher uncertainty warrants bigger cushion |
| Turnaround or distressed | 50%+ | Very high uncertainty; Graham's deep value zone |

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
