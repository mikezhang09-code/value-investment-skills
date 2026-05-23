# Earnings Quality & Analytical Distortions

> **When to read this file:** Step 3.5 of the workflow — after financial data collection and reconciliation, before moat assessment and valuation. Also revisit during Step 6 (valuation) when one-time items, dilution history, or investment portfolios materially affect inputs.

This file addresses **interpretive errors** — situations where the reported data is technically correct but produces wrong conclusions if accepted at face value. These differ from **mechanical errors** (covered in SKILL.md Step 2.5 reconciliation) where the inputs themselves are wrong.

The asymmetry to remember: **mechanical errors are catastrophic but visible** (a 3x wrong share count breaks everything). **Interpretive errors are subtle but cumulative** (a decade of dilution silently destroys per-share value while reported metrics look fine).

---

## The Core Principle

> *"Reported earnings × Reported share count ≠ underlying business economics × shareholders' true claim."*

The job of value investing analysis is to bridge that gap. Eight distortion classes can break the bridge. Apply each as a separate gate.

---

## Distortion Class 1: One-Time Items in Earnings

### The Asymmetric Trap

Management has structural incentive to:
- **Loudly highlight one-time costs** ("non-recurring restructuring charge," "transformation expense") → makes "adjusted" earnings look better than GAAP
- **Quietly bury one-time gains** in operating income → makes recurring earnings look better than they are

The analyst must do this normalization independently. Never rely on management's "adjusted" or "non-GAAP" presentation without scrutiny.

### One-Time Gains That Inflate Reported Earnings

| Item | Where it Hides | Common Markets |
|------|---------------|----------------|
| Asset disposal gains | Other income, operating income | Universal |
| Fair-value remeasurements (investment portfolio) | Other income, FVTPL line | HK conglomerates, insurance |
| Government subsidies (R&D, NEV credits, export rebates) | Other income, operating income | China industrials, semis, EV |
| Tax credits / one-time tax benefits | Income tax expense | Universal |
| Insurance recoveries | Other income | Universal |
| Reversal of prior impairments | Operating expenses (negative) | Cyclicals after recoveries |
| Bargain purchase gains | Other income (M&A year) | Acquirers |
| Reclassification gains (investment property) | Other income | HK property, REITs |
| Disposal of subsidiaries | Discontinued operations or other | Conglomerates |

### One-Time Costs That Depress Reported Earnings

| Item | Often Legitimate Add-Back? | Notes |
|------|---------------------------|-------|
| Restructuring charges | Sometimes | If recurring every 2-3 years → not one-time |
| Goodwill impairment | Yes (non-cash) | But signals prior overpayment for M&A |
| Litigation settlements | Usually | Unless serial litigation = structural issue |
| Inventory writedowns | Sometimes | If recurring → demand/forecasting problem |
| COVID-era charges | Yes for 2020-2022 | But check if 2023+ "COVID charges" are real |
| Pension settlement losses | Yes (non-cash) | One-time accounting effect |
| Hedge ineffectiveness charges | Yes | If derivatives are non-core |

### The "Recurring But Policy-Contingent" Third Bucket

Some items aren't purely operating and aren't purely one-time — they're recurring but dependent on policy that could change:

- **Chinese NEV subsidies and credits** — recurring for now, but phase-out scheduled
- **R&D super-deductions (China, India)** — policy-dependent
- **Export rebates** — policy-dependent
- **Tax holidays for new investments** — sunset clauses
- **Renewable energy tax credits (US IRA)** — political risk

**Treatment:** Count in current normalized earnings BUT stress-test their removal. If removing them flips the verdict, the thesis depends on policy continuation, not business quality.

### Normalized Earnings Construction

```
Reported Net Income                                  XXX
  + One-time costs (itemized with documentation)     +XX
  − One-time gains (itemized with documentation)     −XX
  ± Tax adjustment on the above (at effective rate)  ±X
  = Normalized Net Income                            XXX

Quality check: |Normalized NI − Reported NI| / Reported NI
  If < 10% → reported is reliable proxy
  If 10-25% → use normalized; note adjustment in report
  If > 25% → use normalized; flag prominently in executive summary;
              question whether "earnings power" itself is well-defined
```

### Output Format for Report

Always show the bridge:

| Item | Amount | Recurring? | Source |
|------|--------|-----------|--------|
| Reported Net Income FY2025 | 32,623 | — | Annual report p.X |
| Less: Fair-value gain on investments | (1,200) | No | Note X |
| Less: Government grant (NEV credit) | (2,800) | Policy-contingent | Note X |
| Add back: Restructuring charge | 450 | No | MD&A |
| Tax effect at 22% | 800 | — | Computed |
| **Normalized Net Income** | **29,873** | — | **Computed** |

This bridge is what the analyst, not management, must construct.

---

## Distortion Class 2: Dilution & Per-Share Drift

### The Hidden Destruction

Aggregate growth (revenue, NI, equity) without corresponding per-share growth is **economically meaningless to existing shareholders**. The classic pattern:

```
Year 1: Revenue 100, NI 10, Shares 100  → EPS 0.10
Year 5: Revenue 200, NI 20, Shares 200  → EPS 0.10
        "100% growth"                      Per-share growth: 0%
```

This silently destroys shareholder value in:
- Chinese tech/EV/biotech (frequent placements and follow-ons)
- HK property developers (rights issues, scrip dividends)
- US biotech (constant secondary offerings)
- SPACs and recent IPOs (warrant overhang, sponsor shares)
- Indian companies with frequent QIPs (Qualified Institutional Placements)
- Korean chaebols with cross-holdings and rights issues

### The Per-Share Scorecard (Required for 10-Year Analysis)

Always compute and present both aggregate AND per-share growth:

| Metric | 10-yr Aggregate CAGR | 10-yr Per-Share CAGR | Dilution Drag |
|--------|---------------------|---------------------|---------------|
| Revenue | X% | Y% | X−Y |
| Net Income | X% | Y% | X−Y |
| Book Value / Equity | X% | Y% | X−Y |
| Free Cash Flow | X% | Y% | X−Y |

**Interpretation of dilution drag:**
- 0-1%: Healthy — minor ESOP dilution, possibly offset by buybacks
- 1-3%: Moderate — accept if growth is high and value-creating
- 3-5%: Significant — requires justification (acquisitions creating value? high-IRR investments?)
- 5%+: Severe — major red flag; per-share economics are flat or worse

### Capital Allocation Quality Assessment

For each material equity issuance over the analysis period:

| Year | Shares Issued | Use of Proceeds | Issue Price | IV at Time | Value Impact |
|------|---------------|-----------------|-------------|-----------|--------------|
| | | M&A / Capex / GenCorp / Refi | | | Creating / Neutral / Destructive |

**The Buffett rule:** *"If a company issues stock at a price below its intrinsic value, the per-share value of the remaining shareholders is reduced — even if the cash is well-deployed."*

This is mechanical. Issuing 10% new shares at 80% of IV destroys ~2% of per-share value even if every dollar of proceeds earns the cost of capital. The dilution math is independent of how good the deployment is.

### Buyback Quality Assessment

Symmetric to issuance — buybacks at the right price create value, at the wrong price destroy it:

| Year | Shares Bought | Avg Price | IV at Time | Value Impact |
|------|---------------|-----------|-----------|--------------|
| | | | | Creating / Neutral / Destructive |

**Common failure pattern:** Companies buy back heavily during euphoric markets (high prices) and stop or issue during panics (low prices). This is exactly backward and destroys per-share value over cycles. Apple's pattern is the positive counter-example.

### Forward Dilution Risk

Items NOT yet in the share count but will dilute future EPS:
- Out-of-the-money options near strike
- Unvested RSUs
- Convertible bonds (track if-converted scenarios)
- Warrants
- Anti-dilution provisions in preferred shares
- ESOP allocations announced but not granted

For each, estimate the dilution overhang as % of current diluted shares. If > 5%, model fully-diluted scenarios.

---

## Distortion Class 3: Firm-Owned Investment Portfolios

This is critical for Asian markets — especially HK conglomerates, Chinese SOEs, Japanese cross-holdings, insurance companies, and any holding company structure.

### Three Distinct Patterns

#### Type A: Insurance & Banking Float Portfolios
*Examples: Ping An, AIA, Berkshire Hathaway, Manulife, AIG*

- Investment income is **core** to the business model
- BUT fair-value remeasurements through P&L are NOT underlying earnings
- Solvency II / IFRS 17 (insurance) and CECL (banking) make this even more volatile

**Analytical approach:**
```
True earnings = Underwriting profit / Net interest margin
              + Normalized investment yield × Average invested assets
              − Realistic provisioning

NOT = Reported NI (which includes mark-to-market swings)
```

Use 3-5 year average investment yields, not single-year results.

#### Type B: Holding Company Investment Portfolios
*Examples: Fosun (656.HK), CK Hutchison, SoftBank, Berkshire's equity portfolio, Naspers/Prosus*

- Investment gains/losses can dwarf operating earnings
- Headline P&L is dominated by mark-to-market noise
- Operating businesses may be healthy while reported income looks terrible (or vice versa)

**Analytical approach — Sum-of-the-Parts (SOTP):**
```
Operating businesses     → EV/EBITDA or DCF on operating cash flows
+ Investment portfolio   → Mark-to-market value
  − Holding company discount (typically 15-35%)
    Reasons: tax leakage, structure costs, capital allocation risk, illiquidity
− Net debt at holding-co level
− Holding company overhead (capitalize at 10x)
= Equity value
```

#### Type C: Industrial Companies with Strategic Stakes
*Examples: Tencent's investment portfolio (often > 20% of market cap), Alibaba's stakes, Samsung's cross-holdings, BYD's small stake portfolio*

- "Investment income" line is non-recurring and unpredictable
- Strategic stakes often have hidden value (held at cost, not market) OR overstated value (held at peak)
- Disclosure quality varies wildly

**Analytical approach:**
- Identify the major investments individually
- Mark to market where possible (listed holdings)
- For private holdings, use most recent funding round valuation (with skepticism if dated)
- Apply 20-30% discount to mark for illiquidity and uncertainty
- Treat investment income/loss line as noise, not signal — exclude from normalized earnings

### The Holding Company Discount

Many Asian holding companies trade at 30-50% discount to NAV. **This is often rational, not mispricing:**

Reasons the discount exists:
1. **Tax leakage** — eventual sale of stakes triggers capital gains tax
2. **Structure costs** — holding company overhead, management fees
3. **Capital allocation risk** — will management redeploy gains well, or destroy value via bad M&A?
4. **Illiquidity** — strategic stakes can't be sold quickly without market impact
5. **Conflicts of interest** — controlling shareholder may extract value through related-party transactions
6. **No catalyst** — no path to closing the gap

**A "BUY because trading at 40% discount to NAV" thesis is naive without:**
- Historical analysis: has the discount averaged 40% for a decade? Then it's structural, not mispricing.
- Catalyst identification: what would close the gap? Spin-off? Tender offer? Activist?
- Capital allocation track record: are gains compounded or destroyed?

### SOTP Reconciliation Check

After computing SOTP, sanity-check:
```
SOTP value per share = $X
Current market price = $Y
Implied discount/premium = (Y−X)/X = Z%

If discount > 50% → ask why; identify catalyst
If discount 20-40% → typical for holding company; reasonable
If discount < 20% → market gives credit; assess if justified
If premium → operating business must be exceptional; verify quality
```

---

## Distortion Class 4: Working Capital & Receivables Quality

### The Revenue-Receivables Paradox

Revenue can grow without genuine economic improvement if customers aren't actually paying. Common in:
- Chinese industrials (channel stuffing, accommodating distributors)
- B2B businesses with elongating payment terms
- Companies entering new geographies with weaker credit standards
- Year-end revenue pulls (booking sales but extending DSO)

### Indicators to Track

| Metric | Healthy | Warning | Red Flag |
|--------|---------|---------|----------|
| DSO trend | Stable or declining | Rising 5-15 days over 3 years | Rising >20 days |
| Inventory days | Stable | Rising slowly | Rising fast — demand softening |
| Bills receivable / total AR | <20% | 20-40% | >40% — Chinese accommodation |
| Provision for bad debt / AR | Stable ratio | Falling ratio (despite rising AR) | Falling sharply — under-provisioning |
| Cash from ops / Net income | >1.0 (5-yr avg) | 0.8-1.0 | <0.8 — earnings quality issue |
| Top 3 customers % of revenue | <20% | 20-40% | >40% — concentration risk |

### China-Specific: Bills Receivable

Chinese B2B companies (especially industrials, including CNC tools like 1651.HK) often accept **bank acceptance bills** (银行承兑汇票) or **commercial acceptance bills** (商业承兑汇票) from customers instead of cash. These show up as "bills receivable" or "notes receivable" on the balance sheet.

Key considerations:
- Bank acceptance bills are relatively safe (bank guarantees payment)
- Commercial acceptance bills carry counterparty risk (only the customer guarantees)
- Companies often factor/discount these for cash → hidden financing cost
- Heavy use can mask deteriorating collection terms

For 1651.HK and similar Chinese industrials, scan disclosure for:
- Bills receivable as % of total receivables
- Split between bank and commercial acceptance
- Whether they're being factored (cash flow impact)
- Trend over 5 years

### Customer Concentration

If top customer > 10% OR top 3 customers > 30% of revenue:
- Investigate customer's own financial health
- Assess pricing power (likely weak — captive supplier)
- Consider what happens if they shift to competitor or in-source

---

## Distortion Class 5: Stock-Based Compensation (SBC)

### The Dishonest Add-Back

Many tech companies (especially US, increasingly China ADRs and HK tech) report "non-GAAP" earnings that add back SBC. This is economically dishonest because:

1. **SBC is real expense** — the company is transferring ownership to employees
2. **Dilution is real** — RSU vesting increases share count
3. **You cannot have it both ways** — adding back SBC while ignoring dilution double-counts the benefit

### Rules for SBC Treatment

| Scenario | Correct Treatment |
|----------|------------------|
| Using GAAP earnings | Already deducts SBC — no adjustment needed |
| Using non-GAAP / "adjusted" earnings that excludes SBC | Either subtract SBC back, OR use fully-diluted shares including all RSU vesting |
| Computing FCF | SBC is non-cash → added back to OCF — but you must use fully-diluted share count to reflect true per-share FCF |
| DCF valuation | Project SBC as ongoing expense; project share count growth from RSU vesting; do not "save" the SBC and not dilute |

### SBC Magnitude Check

| SBC as % of Revenue | Assessment |
|--------------------|-----------|
| 0-2% | Normal |
| 2-5% | Elevated — common for mature tech |
| 5-10% | High — common for growth tech; scrutinize |
| 10-20% | Very high — often loss-making growth tech |
| >20% | Extreme — usually pre-profit tech; question whether "earnings" exist at all |

For Chinese ADRs (PDD, BIDU, NTES, JD) and HK tech (Meituan, Kuaishou), SBC routinely 5-15% of revenue. Companies and bullish analysts always present non-GAAP; the analyst must always cross-check GAAP.

---

## Distortion Class 6: Related-Party Transactions (RPTs)

### Why This Matters in Asian Markets

Family-controlled (Indian, Korean chaebols), state-controlled (Chinese SOEs), and founder-controlled (HK Chinese, family conglomerates) companies often have RPTs that drain value invisibly:

- Sales to related parties at below-market prices → revenue understated, but who benefits?
- Purchases from related parties at above-market prices → costs inflated, related party profits
- Loans to controlling shareholders at below-market rates → balance sheet usage with no return
- Loans from controlling shareholders at above-market rates → interest expense inflated
- Property leases at non-arm's-length terms
- Management services from related parties (typical fee extraction)
- Guarantees provided to related parties (off-balance-sheet liability)

### RPT Disclosure Scan

Every annual report has a related-party transactions note. Scan for:

1. **Total RPT volume** — if > 5% of revenue or > 10% of total transactions → material
2. **Pricing basis** — "market terms" claimed but often unverifiable
3. **Trend** — RPT volume increasing or decreasing?
4. **Counterparties** — does ultimate beneficial owner benefit?

### Red Flag Patterns

- Material sales to a customer that is also a related party (especially controlling shareholder's other business)
- Material purchases from a supplier that is a related party
- Loans outstanding to related parties (any amount is questionable)
- Guarantees to related parties' obligations
- Trademark / IP licensing from related parties (royalty extraction)
- Frequent changes in RPT counterparties (restructuring to obscure trail)

### Country-Specific Notes

**India:** Promoter pledging of shares + RPTs = serious financial distress signal. Check promoter shareholding pledge status.

**China A-shares / HK Chinese:** SOEs may have RPTs with parent company holding undisclosed loss-making assets — value transfer to parent at minority shareholders' expense.

**Korea (chaebol):** Cross-shareholding structures and tunneling — gains flow to chairman family at minority shareholders' expense.

---

## Distortion Class 7: Off-Balance-Sheet & Hidden Leverage

### Items NOT in Reported Debt

| Item | Where to Find | How to Treat |
|------|---------------|--------------|
| Operating lease liabilities (pre-IFRS 16 entities) | Note disclosure | Add to debt at PV |
| Guarantees to subsidiaries/JVs | Note disclosure | Contingent liability; assess probability |
| JV/associate proportionate debt | Investments-in-JV note | Add proportional share if material |
| Pension underfunding | Pension note | Real obligation; add to debt |
| Litigation contingencies | Legal proceedings note | Probability-weighted |
| Asset retirement obligations | Long-term liabilities | Already on BS but often overlooked |
| Discounted bills receivable | Off-balance after factoring | Hidden financing |
| Letter of credit / banker's acceptance | Note disclosure | Contingent |
| VIE structures (Chinese ADRs) | Risk factors / structure note | Economic exposure ≠ legal ownership |
| Convertible bonds (pre-conversion) | Debt note | On BS as debt but converts to equity |

### True Net Debt Calculation

```
Reported Net Debt
  + Operating leases (PV)              [for older non-IFRS 16 reports]
  + Pension underfunding
  + Material guarantee exposures
  + Proportional JV debt (if material)
  + Probable litigation settlements
  = True Net Debt
```

### IFRS 16 / ASC 842 — Operating Leases Now On Balance Sheet

Post-2019, operating lease liabilities are on balance sheet. But many analysts still mentally treat them as "different" from financial debt. They aren't — they're contractual obligations with fixed payments, same as bond debt.

For asset-light businesses with large lease obligations:
- Restaurants (McDonald's, Starbucks)
- Retail (especially apparel)
- Logistics (DHL, FedEx)
- Hotels
- Airlines (aircraft operating leases historically)

True leverage is much higher than the "long-term debt" line suggests. EBITDAR (R = rent) was the workaround pre-IFRS 16; now, just use total debt including leases.

---

## Distortion Class 8: Goodwill, Intangibles & Acquisition Accounting

### Acquisition-Led Growth ≠ Organic Growth

Companies grow in two fundamentally different ways:
1. **Organic** — winning new customers, raising prices, launching products
2. **Acquired** — buying revenue and earnings from another company

Reported growth combines both. Per-dollar of organic growth is far more valuable than per-dollar of acquired growth because:
- Organic requires moat (you're winning against competition)
- Acquired just requires capital (you bought the moat at a price)
- Organic creates value; acquired only creates value if purchase price < intrinsic value

### Disentangling Organic from Acquired

```
Organic Revenue Growth = Total Revenue Growth
                      − Revenue contribution from acquisitions (12 months trailing)
                      − FX translation impact
                      = Pure organic
```

Companies that consistently grow only via M&A while organic growth is flat or negative are often value-destroying serial acquirers (think Valeant, Tyco, many SPACs).

### Goodwill Quality Indicators

| Indicator | Healthy | Warning | Red Flag |
|-----------|---------|---------|----------|
| Goodwill / Total Assets | <20% | 20-50% | >50% |
| Goodwill / Equity | <30% | 30-100% | >100% (tangible book negative) |
| Goodwill impairment history | None / minor | Occasional | Recurring → systematic overpayment |
| Acquisitions per year (5-yr) | 0-2 | 3-5 | 6+ → serial acquirer |
| Premium paid (above book) | Justified by moat | High but defensible | Extreme — multiple of book |

### ROIC Including vs. Excluding Goodwill

```
ROIC (reported) = NOPAT / Invested Capital
ROIC (ex-goodwill) = NOPAT / (Invested Capital − Goodwill)
```

The second metric reveals whether the **operating business** earns good returns or whether reported ROIC is just an accounting artifact of having overpaid for acquisitions years ago.

- If ROIC ex-goodwill is high but reported ROIC is mediocre → operating business is good but acquisitions destroyed capital
- If ROIC ex-goodwill is mediocre too → underlying business has no moat
- If ROIC ex-goodwill is much higher than peers → consider what acquisitions did beyond just adding scale

### Intangibles Beyond Goodwill

- Customer relationships (acquired) — amortized; recurring "non-cash" expense
- Trade names — sometimes indefinite-life (no amortization) → watch for impairment
- Developed technology — amortized; signals if R&D is being capitalized
- IPR&D — in-process R&D, capitalized then amortized when ready

Heavy customer-relationship amortization can compress reported earnings while obscuring genuine economics. Track both reported and adjusted (ex-amortization) earnings, but be honest about whether customer relationships truly "depreciate" (sometimes yes, sometimes no).

---

## Other Distortions Worth Noting

### Currency Translation Effects

For multinationals — reported growth in home currency can diverge meaningfully from constant-currency growth in volatile FX years.

- **JPY weakness (2022-2024)** inflates reported foreign sales for Japan-based exporters
- **Strong USD** compresses reported sales for non-USD multinationals
- **CNY weakness** affects HK-listed Chinese companies' reported HKD figures

Always check constant-currency growth disclosures (most large multinationals provide this). If a company's "5% reported growth" was actually "-2% constant currency," the underlying business is shrinking.

### Segment Reporting Distortions

Consolidated metrics can hide segment-level reality:
- Profitable segment cross-subsidizes loss-making segment
- Segment ROIC differs from consolidated ROIC
- One segment's growth masks another's decline

**Always disaggregate when segment data is available:**
| Segment | Revenue | Revenue Growth | Operating Margin | Capital Employed | ROIC |
|---------|---------|----------------|-----------------|-----------------|------|
| Core | | | | | |
| Growth | | | | | |
| Legacy | | | | | |

If one segment has ROIC < WACC persistently, it should arguably be divested. Track whether management addresses this (rationality) or ignores it (institutional imperative).

### Pension & Post-Employment Obligations

For old industrials (especially Japanese, Korean, US legacy auto): pension underfunding is real debt.

Discount rate sensitivity is huge — a 1% drop in discount rate can increase pension liability by 15-20%. In low-rate environments, pension liabilities expand; in rising-rate environments, they shrink.

Companies with material pension exposure (>10% of market cap) should have their net debt adjusted for net pension liability.

---

## Step 3.5 Workflow Integration

Use this checklist after Step 3 (financial analysis) and before Step 4 (moat assessment):

```
□ One-time items normalized (Class 1)
  - One-time gains identified and removed
  - One-time costs assessed (genuine vs. recurring)
  - Policy-contingent items flagged
  - Normalized NI computed and bridged from reported

□ Per-share scorecard computed (Class 2)
  - 10-yr aggregate vs. per-share growth compared
  - Dilution drag calculated
  - Material equity issuances analyzed for value impact
  - Buyback quality assessed
  - Forward dilution risk noted

□ Investment portfolios separated (Class 3)
  - Insurance/banking float: underwriting/NIM analyzed separately
  - Holding company SOTP if applicable
  - Strategic stakes valued separately
  - Investment income excluded from operating earnings

□ Working capital quality assessed (Class 4)
  - DSO trend
  - Inventory days trend
  - Bills receivable scrutiny (Chinese industrials)
  - Customer concentration
  - Cash conversion ratio

□ SBC treatment confirmed (Class 5)
  - GAAP vs. non-GAAP reconciled
  - SBC magnitude assessed
  - Dilution from RSU vesting captured

□ RPT scan completed (Class 6)
  - RPT volume vs. revenue
  - Pattern assessment
  - Country-specific red flags checked

□ Off-balance-sheet items captured (Class 7)
  - True net debt computed
  - Lease liabilities included
  - Pension underfunding included
  - Material contingencies noted

□ Acquisition vs. organic disentangled (Class 8)
  - Organic growth computed
  - Goodwill quality assessed
  - ROIC ex-goodwill computed
  - Serial acquirer pattern check
```

**Gate condition:** If 3+ distortion classes show material issues, the company's reported earnings are not a reliable proxy for underlying economics. The valuation in Step 6 must use normalized figures throughout, and the report must flag this prominently in the executive summary.

---

## Report Section Requirements

Every full deep-dive report must include an "Earnings Quality" section between the Financial History and Moat sections, containing:

1. **Normalized earnings bridge** (Class 1)
2. **Per-share scorecard** (Class 2)
3. **Capital allocation history** (Class 2)
4. **Earnings quality scorecard** (composite of Classes 4-8)

| Dimension | Score | Evidence |
|-----------|-------|----------|
| One-time item discipline | /5 | |
| Per-share economics (dilution-adjusted) | /5 | |
| Investment portfolio transparency | /5 | |
| Working capital quality | /5 | |
| SBC honesty | /5 | |
| RPT cleanliness | /5 | |
| Off-balance-sheet transparency | /5 | |
| Organic vs. acquired growth balance | /5 | |
| **Earnings Quality Composite** | **/40** | |

Score interpretation:
- 32-40: Exceptional — reported numbers can be trusted at face value
- 24-31: Good — minor adjustments needed; reported numbers are reliable directionally
- 16-23: Questionable — meaningful normalization required; treat reported with caution
- <16: Poor — reported numbers cannot be relied upon; deep skepticism warranted

---

## The Meta-Principle

> *"The first principle is that you must not fool yourself — and you are the easiest person to fool."* — Feynman

Reported financials are not designed to fool you, but they are designed to comply with accounting standards, not to reveal underlying economics. The gap between compliance and economic reality is where distortions live.

The value investing analyst's job is to bridge that gap, gate by gate, distortion by distortion, until the normalized economic picture emerges. **No valuation method can compensate for unfaithful inputs.** This file's eight distortion classes are upstream of all valuation work — they determine whether your DCF and EPV are computing anything meaningful at all.
