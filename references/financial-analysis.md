# Financial Analysis Framework

This file defines how to conduct a rigorous 10-year financial analysis. The goal is to understand the true earning power of the business, the quality of those earnings, and the trend direction.

---

## Table of Contents
1. [Data Gathering Priority](#1-data-gathering-priority)
2. [The 10-Year Financial Summary Table](#2-the-10-year-financial-summary-table)
3. [Income Statement Analysis](#3-income-statement-analysis)
4. [Balance Sheet Analysis](#4-balance-sheet-analysis)
5. [Cash Flow Analysis](#5-cash-flow-analysis)
6. [Return Metrics (Most Important)](#6-return-metrics-most-important)
7. [Earnings Quality Assessment](#7-earnings-quality-assessment)
8. [Industry-Specific Adjustments](#8-industry-specific-adjustments)
9. [Financial Health Scorecard](#9-financial-health-scorecard)

---

## 1. Data Gathering Priority

Collect at minimum:
- **10 years** of annual data (or all available if company < 10 years old)
- All values in a consistent currency and fiscal year basis
- Per-share data adjusted for stock splits

If exact numbers are unavailable from filings, use aggregators (Macrotrends, Screener.in) but note the source.

---

## 2. The 10-Year Financial Summary Table

Build this table first — it is the backbone of the analysis:

| Metric | FY15 | FY16 | FY17 | FY18 | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 | 10yr CAGR |
|--------|------|------|------|------|------|------|------|------|------|------|-----------|
| **Revenue** ($M) | | | | | | | | | | | |
| **Gross Profit** ($M) | | | | | | | | | | | |
| **Gross Margin %** | | | | | | | | | | | |
| **Operating Income** ($M) | | | | | | | | | | | |
| **Operating Margin %** | | | | | | | | | | | |
| **Net Income** ($M) | | | | | | | | | | | |
| **Net Margin %** | | | | | | | | | | | |
| **EPS (diluted)** | | | | | | | | | | | |
| **Free Cash Flow** ($M) | | | | | | | | | | | |
| **FCF Margin %** | | | | | | | | | | | |
| **Owner Earnings** ($M) | | | | | | | | | | | |
| **ROE %** | | | | | | | | | | | |
| **ROIC %** | | | | | | | | | | | |
| **Total Debt** ($M) | | | | | | | | | | | |
| **Net Debt/(Cash)** ($M) | | | | | | | | | | | |
| **Debt/Equity** | | | | | | | | | | | |
| **Book Value/Share** | | | | | | | | | | | |
| **Shares Outstanding** (M) | | | | | | | | | | | |
| **Dividends/Share** | | | | | | | | | | | |
| **Payout Ratio %** | | | | | | | | | | | |
| **CapEx** ($M) | | | | | | | | | | | |
| **CapEx/Revenue %** | | | | | | | | | | | |

---

## 3. Income Statement Analysis

### Revenue
- **Growth rate**: Calculate 1-yr, 3-yr, 5-yr, and 10-yr CAGRs
- **Quality of growth**: Organic vs. acquisition-driven? (Organic >> Acquired)
- **Stability**: Look for consistent growth vs. lumpy/cyclical patterns
- **Geographic concentration**: Any single market > 50% of revenue? (risk)

**Benchmarks:**
- Exceptional: > 15% organic CAGR over 10 years
- Good: 8–15% CAGR
- Adequate: 3–8% (inflation + modest real growth)
- Concerning: < 3% or declining — is the business in structural decline?

### Gross Margin
Gross margin reveals the inherent economics of the product/service.

- **Stable or expanding**: Strong pricing power or improving mix
- **Compressing**: Competitive pressure, rising input costs, commoditization
- **Industry context**: Software (60–90%), Consumer brands (40–60%), Retail (20–40%), Manufacturing (20–40%), Services (30–60%)

**Key question**: Has gross margin trended up, down, or sideways over 10 years? Why?

### Operating Margin
Operating margin shows the efficiency of the business model after overhead.

- High and stable: Excellent operating leverage
- Expanding: Business scale is helping (good)
- Compressing: Either competitive pressure or cost discipline failure

**Watch for**: Companies that show improving gross margin but compressing operating margin — often a sign of excessive SG&A growth (empire-building management).

### Net Margin vs. Operating Margin
If net margin is significantly below operating margin, investigate:
- High interest expense (excessive debt)
- High tax rate (watch for "non-recurring" tax benefits inflating earnings)
- Minority interest charges
- Restructuring charges (if recurring, they are not "non-recurring")

---

## 4. Balance Sheet Analysis

### Debt Analysis

**Debt/Equity Ratio:**
- < 0.3: Conservative (Graham-approved)
- 0.3–0.7: Moderate
- 0.7–1.5: Elevated — scrutinize cash flow coverage
- > 1.5: High — requires exceptional cash flow or specific justification (utilities, real estate)

**Interest Coverage Ratio = EBIT / Interest Expense:**
- > 10x: Very comfortable
- 5–10x: Comfortable
- 3–5x: Adequate but watch
- < 3x: Concerning; < 2x: Distressed

**Net Debt / EBITDA:**
- < 1x: Very conservative
- 1–2x: Reasonable
- 2–3x: Elevated
- > 3x: High risk — vulnerable in downturns

**Debt Maturity**: When does the debt mature? Near-term refinancing risk?

### Working Capital
- **Current ratio** (Current Assets / Current Liabilities): Should be ≥ 1.5 (Graham: ≥ 2.0)
- **Quick ratio** (Cash + Receivables / Current Liabilities): ≥ 1.0 preferred
- **Inventory turns**: Higher = better capital efficiency (compare to industry peers)
- **Days Sales Outstanding (DSO)**: Rising DSO = customer payment problems or channel stuffing

### Goodwill & Intangibles
- Goodwill = premium paid in acquisitions
- Goodwill > 50% of total assets: Company is primarily an acquisition vehicle — scrutinize
- Check for **goodwill impairment charges**: a sign that past acquisitions were overpriced
- Capitalized intangibles rising without clear explanation: potential accounting manipulation

### Book Value Per Share
- BVPS CAGR should roughly track ROE minus payout ratio
- If BVPS is shrinking while the company claims high ROE: check for buybacks at premium prices or hidden losses
- For financial companies (banks, insurance), book value is the primary valuation anchor

---

## 5. Cash Flow Analysis

### Free Cash Flow (FCF)
```
FCF = Operating Cash Flow − Capital Expenditures

FCF Conversion = FCF / Net Income
```

**FCF Conversion interpretation:**
- FCF Conversion > 1.0: Exceptional (better than reported earnings suggest)
- FCF Conversion 0.8–1.0: Good
- FCF Conversion 0.5–0.8: Moderate — investigate why (working capital build? High capex?)
- FCF Conversion < 0.5: Red flag — earnings quality issue or capital-intensive period

**Persistent FCF < Net Income** is one of the most reliable red flags in accounting. It often signals:
- Aggressive revenue recognition
- Working capital deterioration
- Underreporting of capex (capitalizing operating expenses)

### Owner Earnings
More conservative than FCF for capital-intensive businesses:
```
Owner Earnings = Net Income + D&A − Maintenance CapEx ± Working Capital Changes

Maintenance CapEx ≈ CapEx × [% needed to maintain current capacity]
(vs. Growth CapEx which generates future earnings)
```

For asset-light businesses (software, consumer brands), maintenance capex is minimal — owner earnings ≈ net income or FCF.
For heavy industry, maintenance capex can be 60–80% of total capex.

### Cash Flow Priorities (what management does with FCF)
Rank from best to worst for shareholders (depends on return opportunities):
1. Reinvestment into the business at high returns (ROIC > WACC) — best if available
2. Acquisitions at reasonable prices with demonstrated synergies
3. Dividends (predictable, creates discipline)
4. Share buybacks at undervalued prices
5. Debt repayment (good if debt is excessive)
6. Share buybacks at overvalued prices — destroys value
7. Cash hoarding without plan — opportunity cost

---

## 6. Return Metrics (Most Important)

These are the most important metrics in value investing. A business that consistently earns high returns on capital is almost always a good business.

### Return on Equity (ROE)
```
ROE = Net Income / Average Shareholders' Equity
```

- > 20%: Exceptional — world-class business
- 15–20%: Excellent
- 10–15%: Good
- 5–10%: Mediocre
- < 5%: Poor — destroys value at most costs of capital

**Critical caveat**: ROE can be inflated by leverage. Always decompose with DuPont:
```
ROE = Net Margin × Asset Turnover × Financial Leverage
     (profitability) × (efficiency) × (leverage)
```

Buffett wants high ROE driven by net margin and asset turnover, NOT leverage.

### Return on Invested Capital (ROIC)
```
ROIC = NOPAT / Invested Capital
NOPAT = Operating Income × (1 − Tax Rate)
Invested Capital = Total Equity + Total Debt − Cash − Non-operating Assets
```

ROIC is more meaningful than ROE because it:
- Includes both equity and debt funding
- Excludes financial leverage effects
- Measures returns on all capital deployed

**Rule of thumb**: ROIC > WACC = value creation. ROIC < WACC = value destruction.

For most value investments: target ROIC > 15% consistently.

### Return on Assets (ROA)
```
ROA = Net Income / Average Total Assets
```

Useful for capital-intensive industries. Target > 10% for non-financial companies.
For banks: ROA > 1% is good; ROE > 12% is good.

### 10-Year Average Returns
Calculate the 10-year average and trend for ROE, ROIC, ROA:
- Is the trend improving or declining?
- Compare to cost of capital (rough WACC estimate: 8–10% for most businesses)
- Compare to industry peers

---

## 7. Earnings Quality Assessment

High-quality earnings are:
1. **Consistent**: Low variance year to year (unless cyclical by nature)
2. **Cash-backed**: FCF closely tracks net income
3. **Conservative**: No aggressive revenue recognition or expense deferral
4. **Transparent**: Easy to understand from filings

### Red Flag Checklist
- [ ] **Accruals ratio** rising: `(Net Income − FCF) / Average Net Assets` — rising = deteriorating quality
- [ ] **Channel stuffing**: Revenue spiking at quarter-end with rising DSO
- [ ] **Non-recurring charges** that recur every year: restructuring, impairments
- [ ] **Pension assumptions** that are too aggressive (discount rate too high)
- [ ] **"Adjusted EBITDA"** that adds back legitimate recurring costs
- [ ] **Revenue recognized before delivery**: common in software, construction
- [ ] **Related party transactions**: sales to affiliated entities at non-market terms
- [ ] **Big bath accounting**: enormous write-downs followed by "recovery"
- [ ] **Auditor change** without clear explanation: very serious warning sign
- [ ] **Multiple restatements**: reliability of reported numbers is questionable

### Fraud Red Flags (Beneish M-Score indicators)
While you don't need to formally calculate the M-Score, be alert to:
- Days Sales Outstanding growing faster than revenue
- Gross margin improving while revenue slows (price gouging / recognition issues)
- Asset quality deteriorating (non-current assets growing as % of total assets)
- Sales growth accelerating while expenses lag (too good to be true)

---

## 8. Industry-Specific Adjustments

### Banks & Insurance
- Use Price/Book instead of P/E as primary valuation
- Focus on Net Interest Margin, Loan Loss Provisions, Capital Ratios (Tier 1)
- Insurance: Combined Ratio (< 100% = profitable underwriting)
- Don't use debt metrics the same way — leverage is inherent to banking

### Real Estate (REITs)
- Use FFO (Funds From Operations) and AFFO instead of EPS
- Dividend yield and payout ratio are critical
- Debt/Assets and interest coverage are key metrics

### Resource Companies (Mining, Oil & Gas)
- Normalize earnings across the commodity price cycle
- Focus on cost of production vs. commodity price
- Reserve life and replacement cost are critical
- Avoid companies that need high commodity prices to survive

### Technology
- High capex for some (semiconductors), zero capex for others (software)
- Focus on recurring revenue %, churn rate, customer acquisition cost
- R&D is an investment — some analysts add back for owner earnings
- Patent cliff risk for hardware/semiconductor companies

### Consumer Staples / Brands
- Gross margin stability is paramount (pricing power)
- Market share data is as important as financial data
- Brand value not on balance sheet — qualitative assessment critical

---

## 9. Financial Health Scorecard

After completing the analysis, score the business on financial quality:

| Category | Score (1–5) | Notes |
|----------|------------|-------|
| Revenue growth consistency | | |
| Margin stability/trend | | |
| FCF conversion quality | | |
| Return on capital (ROE/ROIC) | | |
| Balance sheet strength | | |
| Earnings quality (no manipulation) | | |
| Capital allocation record | | |
| **Total Financial Quality** | **/35** | |

**Interpretation:**
- 28–35: Financial excellence — exceptional business
- 21–27: Strong financials — good business
- 14–20: Adequate — needs strong moat or price to compensate
- 7–13: Weak financials — Graham-style only at extreme discounts
- < 7: Avoid
