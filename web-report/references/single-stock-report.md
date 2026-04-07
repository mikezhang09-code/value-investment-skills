# Single Stock Analysis — Web Report Template

The flagship report type: a comprehensive, interactive analysis of one company. This template
defines the section structure, data requirements, and Chart.js visualizations for each section.

---

## Full HTML Skeleton

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[COMPANY] ([TICKER]) — Value Investing Analysis | [中文公司名]价值投资分析</title>
<link href="https://fonts.googleapis.com/css2?family=[FONTS]&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
  /* Load CSS from design-system.md */
  /* Choose theme: Dark Terminal / Light Editorial / Dark Luxe */
  /* Include all component styles needed */
</style>
</head>
<body>
  <div class="bg-pattern"></div>
  <div class="noise"></div>

  <!-- HERO -->
  <header class="hero">...</header>

  <!-- NAVIGATION -->
  <div class="container">
    <nav class="tabs">...</nav>
  </div>

  <!-- CONTENT SECTIONS -->
  <main class="container">
    <div id="tab-summary" class="tab-content active">...</div>
    <div id="tab-financials" class="tab-content">...</div>
    <div id="tab-valuation" class="tab-content">...</div>
    <div id="tab-moat" class="tab-content">...</div>
    <div id="tab-risk" class="tab-content">...</div>
    <div id="tab-verdict" class="tab-content">...</div>
  </main>

  <!-- DISCLAIMER -->
  <footer class="disclaimer">...</footer>

  <!-- SCRIPTS -->
  <script>
    // Tab navigation
    // Chart.js global defaults
    // All chart initializations
    // Interactive components
  </script>
</body>
</html>
```

---

## Section 1: Executive Summary (tab-summary)

### Required Content
- Company name (EN + ZH), ticker, exchange, analysis date
- Verdict badge (BUY / HOLD / AVOID) — prominent, color-coded
- Investment thesis in 3–4 sentences
- Key bull points (3)
- Key bear points (3)
- KPI stat cards (4–6): Current Price, Intrinsic Value (base), MoS%, Graham Score, Buffett Score, Moat Rating

### Layout
```
┌─────────────────────────────────────────────────┐
│  VERDICT BADGE (BUY / HOLD / AVOID)              │
├─────────────────────────────────────────────────┤
│  Investment Thesis (3-4 sentence narrative)       │
├──────────┬──────────┬──────────┬────────────────┤
│ Price    │ IV Range │ MoS %    │ Moat Rating     │
│ $178.50  │ $155-195 │ +12%     │ ████░  2.4/3    │
├──────────┴──────────┴──────────┴────────────────┤
│  Bull Case (3 points)  │  Bear Case (3 points)   │
└─────────────────────────────────────────────────┘
```

### Stat Cards Data
```javascript
const summaryStats = [
  { label: 'Current Price', labelZh: '当前价格', value: '$178.50', change: '+2.3% MTD', positive: true },
  { label: 'Intrinsic Value', labelZh: '内在价值', value: '$155–195', sublabel: 'Base: $172' },
  { label: 'Margin of Safety', labelZh: '安全边际', value: '+12%', color: mosColor(12) },
  { label: 'Graham Score', labelZh: '格雷厄姆评分', value: '5/7', color: scoreColor(5,7) },
  { label: 'Buffett Score', labelZh: '巴菲特评分', value: '8/10', color: scoreColor(8,10) },
  { label: 'Moat Rating', labelZh: '护城河评级', value: '2.4/3', sublabel: 'Wide Moat' },
];
```

---

## Section 2: Financial Scorecard (tab-financials)

### Required Content
- Graham Defensive Criteria table (7 items, pass/fail)
- Buffett Quality Criteria table (8 items, pass/fail with point scoring)
- Combined score summary
- Historical financial charts (5-10 year)

### Charts Required
1. **Revenue & Net Profit Bar + Growth Line** (combo chart)
2. **Margin Trends** (line chart: gross, EBIT, net margin)
3. **Revenue Segment Breakdown** (doughnut or stacked bar)
4. **ROIC / ROE Historical** (line chart with WACC overlay)

### Scorecard Table Pattern
```html
<table>
  <thead>
    <tr>
      <th>#</th>
      <th>Criterion <span class="zh">/ 评估标准</span></th>
      <th>Value</th>
      <th>Threshold</th>
      <th>Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>P/E Ratio <span class="zh">/ 市盈率</span></td>
      <td class="mono">22.3×</td>
      <td class="mono">&lt;15×</td>
      <td><span class="fail">FAIL ✕</span></td>
    </tr>
    <!-- ... more rows ... -->
  </tbody>
</table>
<div class="score-summary">
  <span class="en">Graham Score: 4/7</span> <span class="zh">| 格雷厄姆评分</span>
  · <span class="en">Buffett Score: 8/10</span> <span class="zh">| 巴菲特评分</span>
</div>
```

---

## Section 3: Valuation Analysis (tab-valuation)

### Required Content
- Graham Number calculation + comparison to price
- EPV (Earnings Power Value)
- Owner Earnings DCF: Bear / Base / Bull cases
- Reverse DCF (implied growth rate at current price)
- Sensitivity table (discount rate × growth rate matrix)
- Intrinsic value range visualization

### Charts Required
5. **Intrinsic Value Horizontal Bar** (showing price vs. Graham, EPV, DCF range)
6. **Scenario Valuation Comparison** (bear/base/bull bar chart with probability weights)

### DCF Assumptions Panel
```html
<div class="card assumptions">
  <h3><span class="en">DCF Assumptions</span> <span class="zh">/ 现金流折现假设</span></h3>
  <div class="grid-3">
    <div>
      <div class="assumption-label">Growth Phase 1 (Yr 1-5)</div>
      <div class="assumption-range">
        <span class="bear">Bear: 3%</span>
        <span class="base">Base: 8%</span>
        <span class="bull">Bull: 12%</span>
      </div>
    </div>
    <div>
      <div class="assumption-label">Growth Phase 2 (Yr 6-10)</div>
      <div class="assumption-range">Bear: 2% | Base: 5% | Bull: 8%</div>
    </div>
    <div>
      <div class="assumption-label">Terminal Growth / Discount Rate</div>
      <div class="assumption-range">g = 3% | r = 10%</div>
    </div>
  </div>
</div>
```

### Sensitivity Table Data
```javascript
// Matrix: growthRates (rows) × discountRates (columns) = intrinsic value
const growthRates = [2, 4, 6, 8, 10]; // %
const discountRates = [8, 9, 10, 11, 12]; // %
const matrix = [
  [145, 128, 114, 103, 93],
  [168, 148, 131, 117, 106],
  [195, 170, 150, 133, 119],
  [228, 197, 172, 152, 135],
  [268, 229, 199, 174, 154]
];
renderSensitivityTable(container, matrix, growthRates, discountRates, currentPrice, '$');
```

---

## Section 4: Moat Analysis (tab-moat)

### Required Content
- Five moat dimensions scored 0–3
- Moat radar chart
- Narrative for each moat dimension (2–3 sentences)
- Overall moat rating + durability assessment
- Competitive landscape summary

### Charts Required
7. **Moat Radar Chart** (5 dimensions)

### Moat Dimension Cards
```html
<div class="moat-dimension">
  <div class="moat-header">
    <span class="en">Switching Costs</span>
    <span class="zh">/ 转换成本</span>
    <span class="moat-score score-high">2.5 / 3</span>
  </div>
  <p>Ecosystem lock-in through iCloud, Apple ID, purchased content, and device interoperability
  creates massive switching friction. Users would lose years of accumulated data and familiarity.</p>
</div>
```

---

## Section 5: Risk Assessment (tab-risk)

### Required Content
- 5–8 risk factors with severity ratings (1–5)
- Visual risk meters for each factor
- Impact probability matrix (optional)
- Mitigation / monitoring checklist

### Risk Table Pattern
```javascript
const risks = [
  { name: 'China Revenue Concentration', nameZh: '中国收入集中度', level: 4, description: '~19% of revenue from China...' },
  { name: 'Regulatory Pressure', nameZh: '监管压力', level: 3, description: 'App Store antitrust...' },
  { name: 'Growth Deceleration', nameZh: '增长放缓', level: 2, description: 'iPhone upgrade cycles lengthening...' },
  // ...
];
```

---

## Section 6: Investment Verdict (tab-verdict)

### Required Content
- Final verdict: BUY / HOLD / AVOID with large badge
- Position sizing recommendation (Full / Half / Watch)
- Target price range (bear/base/bull)
- Entry zone and exit zone
- Key catalysts (what to watch)
- Monitoring checklist (quarterly triggers for re-evaluation)

### Verdict Layout
```
┌───────────────────────────────────────────┐
│  ████████████████████████████████████████  │
│  ██      BUY — Half Position      ██     │
│  ██      买入 — 半仓位            ██     │
│  ████████████████████████████████████████  │
├────────────┬────────────┬────────────────┤
│ Target Low │ Target Mid │ Target High     │
│ $155       │ $172       │ $195            │
├────────────┴────────────┴────────────────┤
│  Entry Zone: $148–$158                    │
│  Exit Zone:  $195+                        │
├───────────────────────────────────────────┤
│  Key Catalysts:                           │
│  • Q2 earnings (margin expansion?)        │
│  • Services revenue growth acceleration   │
│  • China policy clarity                   │
├───────────────────────────────────────────┤
│  Re-evaluation Triggers:                  │
│  ☐ Gross margin drops below 40%          │
│  ☐ FCF conversion falls below 75%        │
│  ☐ ROIC drops below 20%                  │
└───────────────────────────────────────────┘
```

---

## Minimum Chart Count by Report Type

| Report Context | Minimum Charts |
|---------------|---------------|
| Full single-stock deep dive | 7–10 |
| Quick analysis (1-pager web) | 3–5 |
| Earnings update / revision | 4–6 |

### Recommended 7-Chart Set (for a full single stock report)

1. Revenue & Profit trend (combo bar + line)
2. Margin trends (multi-line)
3. Revenue composition (doughnut or stacked bar)
4. ROIC/ROE history (line with WACC)
5. Intrinsic value range (horizontal bar)
6. Moat radar (5-dimension)
7. Peer comparison (horizontal bar)

Optional extras: Sensitivity heatmap (rendered as HTML table), scenario bar chart,
cash flow waterfall, dividend history, segment growth rates.

---

## Data Object Convention

When building the report, structure all company data in a single JavaScript object at the top of
the script section for clarity and maintainability:

```javascript
const company = {
  name: { en: 'Apple Inc.', zh: '苹果公司' },
  ticker: 'AAPL',
  exchange: 'NASDAQ',
  currency: 'USD',
  currencySymbol: '$',
  analysisDate: '2026-04',
  dataVintage: 'FY2025 (Dec 2025)',
  
  // Current market data
  price: 178.50,
  marketCap: 2800e9,
  
  // Graham metrics
  grahamScore: { score: 4, max: 7, details: [...] },
  
  // Buffett metrics
  buffettScore: { score: 8, max: 10, details: [...] },
  
  // Financials (historical)
  financials: {
    years: ['2016','2017','2018','2019','2020','2021','2022','2023','2024','2025'],
    revenue: [...],  // in billions, local currency
    netProfit: [...],
    grossMargin: [...],  // percentages
    ebitMargin: [...],
    netMargin: [...],
    roic: [...],
    roe: [...],
    fcf: [...],
    eps: [...],
    bvps: [...]
  },
  
  // Valuation
  valuation: {
    grahamNumber: 92.50,
    epv: 140,
    dcf: { bear: 120, base: 155, bull: 195 },
    probability: { bear: 25, base: 50, bull: 25 },
    sensitivity: {
      growthRates: [2,4,6,8,10],
      discountRates: [8,9,10,11,12],
      matrix: [[...],[...],...]
    },
    reverseDCF: { impliedGrowth: 8.2 },
    mosPercent: 12  // (IV base - price) / IV base × 100
  },
  
  // Moat
  moat: {
    intangibleAssets: { score: 3, narrative: '...' },
    switchingCosts: { score: 2.5, narrative: '...' },
    networkEffects: { score: 2, narrative: '...' },
    costAdvantages: { score: 1, narrative: '...' },
    efficientScale: { score: 0.5, narrative: '...' },
    total: 9,  // out of 15
    rating: 'Wide'  // None / Narrow / Wide
  },
  
  // Risks
  risks: [...],
  
  // Verdict
  verdict: {
    action: 'BUY',  // BUY, HOLD, AVOID
    position: 'Half',  // Full, Half, Watch
    targetRange: { low: 155, mid: 172, high: 195 },
    entryZone: { low: 148, high: 158 },
    exitZone: 195,
    catalysts: [...],
    monitoringTriggers: [...]
  },
  
  // Thesis
  thesis: { bull: '...', bear: '...' },
  
  // Segment breakdown
  segments: [
    { name: 'iPhone', revenue: 200.6, pct: 52 },
    { name: 'Services', revenue: 85.2, pct: 22 },
    // ...
  ]
};
```

This convention keeps data separate from rendering logic, making it easy to update figures
without modifying chart code.

---

## Currency & Market Conventions

| Market | Currency | Symbol | Format Example |
|--------|----------|--------|----------------|
| US | USD | $ | $178.50 |
| HK | HKD | HK$ | HK$105.80 |
| China A-shares | CNY | ¥ | ¥42.30 |
| India | INR | ₹ | ₹2,450 |
| Singapore | SGD | S$ | S$12.50 |

For HK/China cross-listing: show both HKD and CNY where relevant, with exchange rate noted.
