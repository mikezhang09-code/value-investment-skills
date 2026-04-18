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
    <div id="tab-screener" class="tab-content active">...</div>
    <div id="tab-summary" class="tab-content">...</div>
    <div id="tab-business" class="tab-content">...</div>
    <div id="tab-management" class="tab-content">...</div>
    <div id="tab-financials" class="tab-content">...</div>
    <div id="tab-valuation" class="tab-content">...</div>
    <div id="tab-moat" class="tab-content">...</div>
    <div id="tab-industry" class="tab-content">...</div>
    <div id="tab-risk" class="tab-content">...</div>
    <div id="tab-monitoring" class="tab-content">...</div>
    <div id="tab-verdict" class="tab-content">...</div>
    <div id="tab-sources" class="tab-content">...</div>
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

## Section 1b: Business Overview (tab-business) — NEW

The HTML report previously assumed segment data alone was sufficient. For institutional-grade output, every report must explain **what the business does in plain language** before any numbers appear.

### Required Content

- **Plain-language business description** — 2–3 paragraphs explaining what the company sells, to whom, in which markets, and how it makes money. Written for someone who has never heard of the company.
- **Revenue breakdown** — segment + geography table with YoY growth
- **Business model characteristics** — recurring vs. transactional, customer concentration, pricing model, capital intensity
- **Industry context** — 1–2 paragraphs on industry size, growth, dynamics, secular trends

### Layout Pattern

```html
<div id="tab-business" class="tab-content">
  <div class="card">
    <h2><span class="en">What Does the Company Do?</span> <span class="zh">/ 公司业务概述</span></h2>
    <p class="business-narrative">[2-3 paragraphs of plain-language description]</p>
  </div>

  <div class="grid-2">
    <div class="card">
      <h3><span class="en">Revenue Breakdown</span> <span class="zh">/ 收入构成</span></h3>
      <table>
        <thead>
          <tr><th>Segment / Geography</th><th>Revenue</th><th>% of Total</th><th>YoY</th></tr>
        </thead>
        <tbody>
          <!-- Render from company.segments and company.geography -->
        </tbody>
      </table>
    </div>

    <div class="card">
      <h3><span class="en">Business Model</span> <span class="zh">/ 商业模式</span></h3>
      <div class="business-model-grid">
        <div><span class="label">Revenue Type</span><span class="value">[Recurring/Transactional/Mixed — X%]</span></div>
        <div><span class="label">Customer Concentration</span><span class="value">[Top customer = X%]</span></div>
        <div><span class="label">Pricing Model</span><span class="value">[Premium/Value/Variable]</span></div>
        <div><span class="label">Capital Intensity</span><span class="value">[Asset-light/Moderate/Heavy]</span></div>
      </div>
    </div>
  </div>

  <div class="card">
    <h3><span class="en">Industry Context</span> <span class="zh">/ 行业背景</span></h3>
    <p>[1-2 paragraphs on industry size, growth, dynamics, secular trends]</p>
  </div>
</div>
```

### Charts Required (optional)

If revenue mix is significant, include:
- **Revenue by Segment** doughnut or stacked bar (also shown in financials section — pick one location)

### Data Object Additions

```javascript
company.businessOverview = {
  description: '[2-3 paragraph plain-language explanation]',
  industryContext: '[1-2 paragraph industry narrative]',
  businessModel: {
    revenueType: 'Recurring',
    revenueRecurringPct: 75,
    customerConcentration: 'Top 10 customers = 18% of revenue',
    pricingModel: 'Premium',
    capitalIntensity: 'Asset-light'
  },
  geography: [
    { region: 'Greater China', revenue: 415, pct: 60, growthYoY: 18 },
    { region: 'Overseas', revenue: 280, pct: 40, growthYoY: 35 }
  ]
};
```

---

## Section 2: Management Assessment (tab-management) — NEW

This is the largest content gap previously absent from the HTML report. Buffett-style analysis cannot exist without explicit assessment of leadership quality, ownership alignment, and capital allocation track record.

### Required Content

- **Leadership table** — CEO, CFO, founder/chairman with tenure and background
- **Ownership & alignment KPI cards** — insider ownership %, CEO comp structure, buyback history at average price, dividend track record
- **Capital allocation scorecard** — 5-year breakdown of how cash was deployed and quality of each use
- **Red flags checklist** — explicit pass/concern check on related-party transactions, compensation, transparency, regulatory issues

### Layout Pattern

```html
<div id="tab-management" class="tab-content">
  <!-- Leadership -->
  <div class="card">
    <h2><span class="en">Leadership</span> <span class="zh">/ 管理层</span></h2>
    <table>
      <thead>
        <tr><th>Name</th><th>Role</th><th>Tenure</th><th>Background</th></tr>
      </thead>
      <tbody>
        <!-- Render from company.management.leadership -->
      </tbody>
    </table>
  </div>

  <!-- Ownership & Alignment -->
  <div class="card">
    <h2><span class="en">Ownership & Alignment</span> <span class="zh">/ 持股与利益绑定</span></h2>
    <div class="grid-4">
      <div class="stat-card">
        <div class="stat-label"><span class="en">Insider Ownership</span> <span class="zh">/ 内部人持股</span></div>
        <div class="stat-value">12.4%</div>
        <div class="stat-change positive">High alignment</div>
      </div>
      <div class="stat-card">
        <div class="stat-label"><span class="en">CEO Performance Pay</span> <span class="zh">/ CEO绩效薪酬比例</span></div>
        <div class="stat-value">85%</div>
        <div class="stat-change positive">Well-aligned</div>
      </div>
      <div class="stat-card">
        <div class="stat-label"><span class="en">5Y Buybacks</span> <span class="zh">/ 五年回购</span></div>
        <div class="stat-value">$48B</div>
        <div class="stat-change">Avg price $145 vs current $178</div>
      </div>
      <div class="stat-card">
        <div class="stat-label"><span class="en">Dividend Streak</span> <span class="zh">/ 股息连续年数</span></div>
        <div class="stat-value">12 yrs</div>
        <div class="stat-change">Yield 0.5%</div>
      </div>
    </div>
  </div>

  <!-- Capital Allocation Scorecard -->
  <div class="card">
    <h2><span class="en">Capital Allocation Scorecard (5-year)</span> <span class="zh">/ 资本配置评估</span></h2>
    <table>
      <thead>
        <tr><th>Use of Capital</th><th>Amount</th><th>Quality Assessment</th><th>Rating</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Organic Reinvestment <span class="zh">/ 内部再投资</span></td>
          <td class="mono">$120B</td>
          <td>R&D and capex generated avg incremental ROIC of 28%</td>
          <td><span class="pass">Excellent</span></td>
        </tr>
        <tr>
          <td>Acquisitions <span class="zh">/ 并购</span></td>
          <td class="mono">$8B</td>
          <td>Bolt-on tech acquisitions; small but accretive</td>
          <td><span class="pass">Good</span></td>
        </tr>
        <tr>
          <td>Dividends <span class="zh">/ 股息</span></td>
          <td class="mono">$72B</td>
          <td>Sustainable payout ratio at 18%, growing 7% CAGR</td>
          <td><span class="pass">Good</span></td>
        </tr>
        <tr>
          <td>Buybacks <span class="zh">/ 股票回购</span></td>
          <td class="mono">$48B</td>
          <td>Repurchased at avg $145 vs current $178 — value-creating</td>
          <td><span class="pass">Excellent</span></td>
        </tr>
        <tr>
          <td>Debt Management <span class="zh">/ 债务管理</span></td>
          <td class="mono">Net cash $62B</td>
          <td>Conservative balance sheet; ample optionality</td>
          <td><span class="pass">Excellent</span></td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Red Flags Check -->
  <div class="card">
    <h2><span class="en">Red Flags Check</span> <span class="zh">/ 风险信号检查</span></h2>
    <div class="checklist">
      <div class="check-item"><span class="pass">✓</span> No material related-party transactions of concern</div>
      <div class="check-item"><span class="pass">✓</span> Compensation reasonable and performance-aligned</div>
      <div class="check-item"><span class="pass">✓</span> Shareholder communication transparent and consistent</div>
      <div class="check-item"><span class="pass">✓</span> No significant investigations or regulatory actions</div>
      <div class="check-item"><span class="partial">⚠</span> [Note any concerns here, or leave checklist clean]</div>
    </div>
  </div>
</div>
```

### Data Object Additions

```javascript
company.management = {
  leadership: [
    { name: 'Tim Cook', role: 'CEO', tenure: '13 yrs', background: 'Former COO; joined 1998 from Compaq' },
    { name: 'Luca Maestri', role: 'CFO', tenure: '10 yrs', background: 'Former Xerox CFO; joined 2013' },
    { name: 'Arthur Levinson', role: 'Chairman', tenure: '13 yrs', background: 'Former Genentech CEO' }
  ],
  ownership: {
    insiderPct: 12.4,
    ceoPerformancePayPct: 85,
    buybacks5Y: { totalUSD: 48e9, avgPrice: 145, currentPrice: 178 },
    dividendStreakYears: 12,
    currentYieldPct: 0.5
  },
  capitalAllocation: [
    { use: 'Organic Reinvestment', amount: '$120B', assessment: '...', rating: 'Excellent' },
    { use: 'Acquisitions', amount: '$8B', assessment: '...', rating: 'Good' },
    { use: 'Dividends', amount: '$72B', assessment: '...', rating: 'Good' },
    { use: 'Buybacks', amount: '$48B', assessment: '...', rating: 'Excellent' },
    { use: 'Debt Management', amount: 'Net cash $62B', assessment: '...', rating: 'Excellent' }
  ],
  redFlags: {
    relatedParty: 'CLEAR',
    compensation: 'CLEAR',
    transparency: 'CLEAR',
    regulatory: 'CLEAR',
    notes: ''
  }
};
```

---

## Section 3: Financial Scorecard (tab-financials) — UPDATED

### Required Content

- Graham Defensive Criteria table (7 items, pass/fail)
- Buffett Quality Criteria table (8 items, pass/fail with point scoring)
- Combined score summary
- Historical financial charts (5-10 year)
- **Qualitative observations narrative** (NEW — required) — Strengths, Concerns, Earnings Quality assessment

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

### Qualitative Observations (NEW — required)

Charts without narrative are pretty but uninformative. After the charts and scorecard tables, every financial section must include a two-column callout pairing **Strengths** and **Concerns**, plus an **Earnings Quality** assessment.

```html
<div class="grid-2">
  <div class="callout positive">
    <h3><span class="en">Financial Strengths</span> <span class="zh">/ 财务优势</span></h3>
    <ul>
      <li>Gross margins expanded from 38% to 46% over the decade — pricing power evidence</li>
      <li>FCF/Net Income avg 108% — earnings quality is exceptional</li>
      <li>ROIC sustained above 25% for 8 of 10 years — durable competitive advantage</li>
    </ul>
  </div>
  <div class="callout negative">
    <h3><span class="en">Financial Concerns</span> <span class="zh">/ 财务隐忧</span></h3>
    <ul>
      <li>Debt/Equity rose from 0.4x to 1.6x driven by buyback financing — monitor leverage</li>
      <li>Services growth decelerated to 8% YoY in latest quarter from 16% trend — watch closely</li>
      <li>China revenue concentration at 19% remains a geopolitical risk vector</li>
    </ul>
  </div>
</div>

<div class="card">
  <h3><span class="en">Earnings Quality Assessment</span> <span class="zh">/ 盈利质量评估</span></h3>
  <div class="grid-3">
    <div class="stat-card">
      <div class="stat-label">FCF / Net Income (10yr avg)</div>
      <div class="stat-value">108%</div>
      <div class="stat-change positive">Excellent (>90%)</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Revenue Recognition</div>
      <div class="stat-value" style="font-size:1rem">Conservative</div>
      <div class="stat-change positive">Standard policies</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Non-Recurring Pattern</div>
      <div class="stat-value" style="font-size:1rem">Clean</div>
      <div class="stat-change positive">No serial restructuring</div>
    </div>
  </div>
  <p style="margin-top:16px"><strong>Overall Earnings Quality Rating: HIGH</strong> — [1-2 sentence narrative explanation]</p>
</div>
```

### Data Object Additions

```javascript
company.financialObservations = {
  strengths: [
    'Gross margins expanded from 38% to 46% over the decade — pricing power evidence',
    'FCF/Net Income avg 108% — earnings quality is exceptional',
    'ROIC sustained above 25% for 8 of 10 years — durable competitive advantage'
  ],
  concerns: [
    'Debt/Equity rose from 0.4x to 1.6x driven by buyback financing — monitor leverage',
    'Services growth decelerated to 8% YoY in latest quarter from 16% trend',
    'China revenue concentration at 19% remains a geopolitical risk vector'
  ],
  earningsQuality: {
    fcfToNetIncomePct: 108,
    revenueRecognition: 'Conservative',
    nonRecurringPattern: 'Clean',
    overallRating: 'HIGH',
    narrative: 'Cash conversion exceeds net income consistently; no aggressive accounting flags identified.'
  }
};
```

---

## Section 4: Valuation Analysis (tab-valuation)

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

## Section 5: Moat Analysis (tab-moat)

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

### Moat Trend Indicator (required)

Show the moat's direction alongside its strength. This is critical — a narrowing wide moat is more dangerous than a widening narrow moat.

```html
<div class="moat-trend-panel">
  <div class="moat-score-badge">9/15 — <span class="moat-wide">Wide Moat</span></div>
  <div class="moat-trend-arrow trend-stable">● Stable <span class="zh">/ 稳定</span></div>
  <div class="moat-trend-evidence">Gross margins stable at 44%, NRR >120%, no significant competitive erosion.</div>
</div>
```

Trend arrow styling: `▲ Widening` = green, `● Stable` = amber, `▼ Narrowing` = red.

### Franchise vs. Commodity Classification

```html
<div class="business-model-badge franchise">
  <span class="en">Franchise Business</span> <span class="zh">/ 特许经营型企业</span>
</div>
```

Badge colors: Franchise = deep green background, Commodity = gray, Hybrid = amber.

---

## Section 5b: Industry Analysis (tab-industry)

### Required Content

- Industry-specific key metrics (varies by sector) in a KPI card grid
- Macro sensitivity assessment table
- Sector-specific risk factors
- Buffett case study reference (success or failure in this industry)

### Industry KPI Cards Pattern

```javascript
// Insurance example
const industryKPIs = [
  { label: 'Combined Ratio', labelZh: '综合成本率', value: '95.2%', benchmark: '< 100%', status: 'good' },
  { label: 'Float Size', labelZh: '浮存金', value: '$164B', benchmark: 'Growing', status: 'good' },
  { label: 'Underwriting Profit', labelZh: '承保利润', value: '$2.8B', benchmark: '> 0', status: 'good' },
];
// Banking example
const bankingKPIs = [
  { label: 'ROA', labelZh: '资产回报率', value: '1.3%', benchmark: '> 1.2%', status: 'good' },
  { label: 'NPL Ratio', labelZh: '不良贷款率', value: '0.8%', benchmark: '< 1%', status: 'good' },
  { label: 'CET1 Ratio', labelZh: '核心一级资本', value: '12.5%', benchmark: '> 10%', status: 'good' },
  { label: 'NIM', labelZh: '净利差', value: '2.8%', benchmark: 'vs peers', status: 'ok' },
];
```

### Macro Sensitivity Table

```html
<table class="macro-sensitivity">
  <tr><th>Macro Factor / 宏观因素</th><th>Impact / 影响</th><th>Severity</th></tr>
  <tr><td>Rising Interest Rates</td><td>[sector-specific impact]</td><td class="moderate">Moderate</td></tr>
  <tr><td>Inflation</td><td>[sector-specific impact]</td><td class="low">Low</td></tr>
  <tr><td>Economic Recession</td><td>[sector-specific impact]</td><td class="high">High</td></tr>
</table>
```

---

## Section 6: Risk Assessment (tab-risk)

### Required Content

- 5–8 risk factors with severity ratings (1–5)
- Visual risk meters for each factor
- **Sell Criteria Check** (4 criteria — mandatory for HOLD/SELL)
- **Value Trap Diagnostic** (5-type check)
- **Inflation Scorecard** (6-factor, if macro relevant)
- **Derivatives Exposure Check** (if applicable)
- **Downside Scenario card** (NEW — required)

### Risk Table Pattern

```javascript
const risks = [
  { name: 'China Revenue Concentration', nameZh: '中国收入集中度', level: 4, description: '~19% of revenue from China...' },
  { name: 'Regulatory Pressure', nameZh: '监管压力', level: 3, description: 'App Store antitrust...' },
  { name: 'Growth Deceleration', nameZh: '增长放缓', level: 2, description: 'iPhone upgrade cycles lengthening...' },
  // ...
];
```

### Sell Criteria Check Table (required for HOLD/SELL verdicts)

```javascript
const sellCriteria = [
  { num: 1, criterion: 'Severely Overvalued?', criterionZh: '严重高估？',
    triggered: false, basis: 'Trading at 15% below base IV estimate' },
  { num: 2, criterion: 'Moat Destroyed?', criterionZh: '护城河被摧毁？',
    triggered: false, basis: 'Moat stable; ecosystem lock-in intact, NRR >120%' },
  { num: 3, criterion: 'Integrity Issue?', criterionZh: '诚信问题？',
    triggered: false, basis: 'No concerns; transparent reporting, consistent commentary' },
  { num: 4, criterion: 'Better Opportunity?', criterionZh: '更好的机会？',
    triggered: false, basis: 'No materially superior alternatives identified at present' },
];
// Render as table: green "✓ No" or red "⚠ YES" in the status column
```

### Value Trap Diagnostic Table

```javascript
const valueTrapCheck = [
  { type: 'Structural Decline', typeZh: '结构性衰退',
    question: 'Will this industry exist in meaningful form in 10 years?', result: 'CLEAR' },
  { type: 'Commodity Business', typeZh: '大宗商品型企业',
    question: 'If prices raised 5%, what % of customers leave?', result: 'CLEAR' },
  { type: 'Poor Capital Allocation', typeZh: '资本配置不良',
    question: '10-year M&A track record: value-creating or destroying?', result: 'CLEAR' },
  { type: 'Heavy Assets, Low Returns', typeZh: '重资产低回报',
    question: 'Is ROIC persistently below WACC?', result: 'CLEAR' },
  { type: 'Accounting Quality', typeZh: '会计质量问题',
    question: 'Cash conversion ratio persistently below 70%?', result: 'CLEAR' },
];
// Result values: 'CLEAR' (green), 'WARNING' (orange), 'TRAPPED' (red)
```

### Inflation Scorecard (include when macro overlay is relevant)

```javascript
const inflationFactors = [
  { factor: 'Pricing Power', factorZh: '定价权', score: +1, rationale: 'Can raise prices 5%+ without volume loss' },
  { factor: 'Capital Intensity', factorZh: '资本密集度', score: +1, rationale: 'Capex/Rev < 5%' },
  { factor: 'ROIC Level', factorZh: 'ROIC水平', score: +1, rationale: 'ROIC >15% sustained' },
  { factor: 'Inventory Exposure', factorZh: '库存敞口', score: +1, rationale: 'Minimal inventory risk' },
  { factor: 'Debt Structure', factorZh: '债务结构', score: 0, rationale: 'Mixed — some floating rate exposure' },
  { factor: 'Input Cost Sensitivity', factorZh: '投入成本敏感度', score: 0, rationale: 'Moderate component cost sensitivity' },
];
const inflationTotal = 4; // +4 to +6 = resistant, +1 to +3 = moderate, ≤0 = vulnerable
```

### Downside Scenario Card (NEW — required)

If the thesis is wrong and the principal risks materialize, what's the floor? This is the explicit stress test that prevents over-confidence in the verdict.

```html
<div class="card">
  <h3><span class="en">Downside Scenario — If The Thesis Is Wrong</span> <span class="zh">/ 悲观情景分析</span></h3>
  <div class="grid-3">
    <div class="stat-card">
      <div class="stat-label"><span class="en">Bear-Case Owner Earnings</span> <span class="zh">/ 悲观所有者收益</span></div>
      <div class="stat-value">$5.20</div>
      <div class="stat-change">vs Base $7.80</div>
    </div>
    <div class="stat-card">
      <div class="stat-label"><span class="en">Bear-Case Intrinsic Value</span> <span class="zh">/ 悲观内在价值</span></div>
      <div class="stat-value">$120</div>
      <div class="stat-change negative">−33% vs current $178</div>
    </div>
    <div class="stat-card">
      <div class="stat-label"><span class="en">Downside from Current Price</span> <span class="zh">/ 当前价格下行空间</span></div>
      <div class="stat-value negative">−33%</div>
      <div class="stat-change">Permanent capital loss zone</div>
    </div>
  </div>
  <div class="callout">
    <strong><span class="en">Downside Protection Commentary</span> <span class="zh">/ 下行保护分析</span>:</strong>
    <p>Even in the bear case, [explain why downside is bounded — strong balance sheet? brand value? recurring revenue floor? contractual cash flows? — or honestly state where downside protection is weak].</p>
  </div>
</div>
```

### Data Object Additions

```javascript
company.downsideScenario = {
  bearOwnerEarningsPerShare: 5.20,
  bearIntrinsicValue: 120,
  downsidePct: -33,
  protectionCommentary: 'Net cash position of $62B and 60%+ recurring revenue base limit permanent loss exposure. Even in bear case, distressed-buyer floor likely above $100.'
};
```

---

## Section 6b: Monitoring & Triggers (tab-monitoring)

### Required Content

- Quarterly review checklist (5–7 items to check each quarter)
- Specific sell trigger signals (conditions that would trigger a position review or exit)
- Key assumptions that must remain true for the thesis to hold
- Next review date

### Monitoring Checklist Pattern

```html
<div class="monitoring-section">
  <h3><span class="en">Quarterly Review Checklist</span> <span class="zh">/ 季度审查清单</span></h3>
  <div class="checklist">
    <div class="check-item">☐ Revenue trend — accelerating, stable, or decelerating?</div>
    <div class="check-item">☐ Gross margin trend — widening, stable, or narrowing?</div>
    <div class="check-item">☐ Cash conversion — still above 80%?</div>
    <div class="check-item">☐ Management tone — more or less honest than prior quarters?</div>
    <div class="check-item">☐ Competitive landscape — any new threats or moat changes?</div>
    <div class="check-item">☐ Capital allocation decisions — value-creating or destroying?</div>
  </div>

  <h3><span class="en">Sell Trigger Signals</span> <span class="zh">/ 卖出触发信号</span></h3>
  <div class="trigger-list">
    <div class="trigger-item trigger-red">⚠ ROIC falls below WACC for 2 consecutive years</div>
    <div class="trigger-item trigger-red">⚠ Cash conversion drops below 60%</div>
    <div class="trigger-item trigger-red">⚠ Management integrity scandal — sell immediately</div>
    <div class="trigger-item trigger-orange">⚡ Moat score drops by 2+ points on the 0–15 scale</div>
    <div class="trigger-item trigger-orange">⚡ Industry enters structural decline (not cyclical)</div>
    <div class="trigger-item trigger-orange">⚡ Position appreciated beyond 2× intrinsic value</div>
  </div>
</div>
```

---

## Section 7: Investment Verdict (tab-verdict)

### Required Content
- Final verdict: BUY / HOLD / SELL / AVOID with large badge
- Position sizing recommendation (Full / Half / Watch)
- Target price range (bear/base/bull)
- Entry zone and exit zone
- Key catalysts (what to watch)
- Monitoring checklist (quarterly triggers for re-evaluation)

### Verdict Layout

```
┌───────────────────────────────────────────┐
│  ████████████████████████████████████████  │
│  ██     BUY — Half Position           ██  │
│  ██     买入 — 半仓位                   ██  │
│  ████████████████████████████████████████  │
├────────────┬────────────┬────────────────┤
│ Target Low │ Target Mid │ Target High     │
│ $155       │ $172       │ $195            │
├────────────┴────────────┴────────────────┤
│ Entry Zone:  $148–$158                    │
│ Exit Zone:   $195+                        │
├───────────────────────────────────────────┤
│ Key Catalysts:                            │
│ • Q2 earnings (margin expansion?)         │
│ • Services revenue growth acceleration    │
│ • China policy clarity                    │
├───────────────────────────────────────────┤
│ Re-evaluation Triggers:                   │
│  ☐ Gross margin drops below 40%           │
│  ☐ FCF conversion falls below 75%         │
│  ☐ ROIC drops below 20%                   │
└───────────────────────────────────────────┘
```

---

## Section 8: Sources & Data Trail (tab-sources) — NEW

This section is mandatory for every report. It is the connective tissue between the analytical output and the data discipline established in `value-investing/references/data-sources.md`. Without it, the report cannot be re-audited and verdict-moving numbers cannot be traced back to primary sources.

Maps directly to:
- `report-template.md` Section "Sources & References"
- `references/data-sources.md` § Data Trail (Metric | Value | Source | Date | Vintage)
- `references/data-sources.md` § Pre-Verdict Checklist

### Required Content

- **Data Trail table** — top 5–10 verdict-moving inputs with full source lineage
- **General sources** — filings, IR materials, aggregators used
- **Pre-Verdict Checklist status** — explicit confirmation each box was ticked
- **Data vintage notice** — when data was retrieved and as-of date

### Layout Pattern

```html
<div id="tab-sources" class="tab-content">
  <!-- Data Trail — verdict-moving inputs -->
  <div class="card">
    <h2><span class="en">Data Trail — Verdict-Moving Inputs</span> <span class="zh">/ 关键数据溯源</span></h2>
    <p style="color:var(--text-secondary);font-size:0.88rem;margin-bottom:16px">
      Every input below would shift the Buy / Hold / Avoid verdict if changed by ±20%, and has been verified against a Tier 1 or Tier 2 primary source per the data-sourcing protocol.
    </p>
    <table>
      <thead>
        <tr>
          <th>Metric</th>
          <th>Value</th>
          <th>Source</th>
          <th>Retrieved</th>
          <th>Vintage</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Revenue FY2025</td>
          <td class="mono">$391.0B</td>
          <td>Apple 10-K FY2025, Item 8</td>
          <td class="mono">2026-04-10</td>
          <td>FY2025 reported</td>
        </tr>
        <tr>
          <td>Owner Earnings (TTM)</td>
          <td class="mono">$108.5B</td>
          <td>Derived from 10-K — NI + D&A − maint. capex</td>
          <td class="mono">2026-04-10</td>
          <td>TTM Q1 2026</td>
        </tr>
        <tr>
          <td>Net cash position</td>
          <td class="mono">$62B</td>
          <td>10-K FY2025 balance sheet, p.34</td>
          <td class="mono">2026-04-10</td>
          <td>As of 2025-09-30</td>
        </tr>
        <tr>
          <td>Diluted shares outstanding</td>
          <td class="mono">15.31B</td>
          <td>10-K FY2025, share count footnote</td>
          <td class="mono">2026-04-10</td>
          <td>FY2025 weighted avg</td>
        </tr>
        <tr>
          <td>Services segment revenue</td>
          <td class="mono">$96.2B</td>
          <td>10-K FY2025 segment disclosure</td>
          <td class="mono">2026-04-10</td>
          <td>FY2025 reported</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- General Sources -->
  <div class="card">
    <h2><span class="en">Sources Consulted</span> <span class="zh">/ 信息源清单</span></h2>
    <table>
      <thead>
        <tr><th>Source</th><th>Document</th><th>Date</th><th>Purpose</th></tr>
      </thead>
      <tbody>
        <tr><td>SEC EDGAR</td><td>10-K Annual Report</td><td>FY2025</td><td>Primary financials, MD&A, risk factors</td></tr>
        <tr><td>SEC EDGAR</td><td>10-Q Quarterly</td><td>Q1 2026</td><td>Latest quarterly update</td></tr>
        <tr><td>Apple IR</td><td>Q1 2026 Earnings Presentation</td><td>Feb 2026</td><td>Management commentary, segment color</td></tr>
        <tr><td>Apple IR</td><td>Q1 2026 Earnings Call Transcript</td><td>Feb 2026</td><td>Forward guidance, capital allocation</td></tr>
        <tr><td>Macrotrends</td><td>10-year historical financials</td><td>—</td><td>Long-run ratio trends, cross-check</td></tr>
        <tr><td>StockAnalysis.com</td><td>Per-share statistics</td><td>—</td><td>EPS / BVPS / FCF/share verification</td></tr>
      </tbody>
    </table>
  </div>

  <!-- Pre-Verdict Checklist Status -->
  <div class="card">
    <h2><span class="en">Pre-Verdict Checklist Status</span> <span class="zh">/ 发布前检查清单</span></h2>
    <p style="color:var(--text-secondary);font-size:0.88rem;margin-bottom:16px">
      Per <code>references/data-sources.md</code> Section "Pre-Verdict Checklist" — confirmed before publishing this verdict:
    </p>
    <div class="checklist">
      <div class="check-item"><span class="pass">✓</span> Every verdict-moving number has a Tier 1 or Tier 2 source</div>
      <div class="check-item"><span class="pass">✓</span> No pending M&A is embedded in current SOTP <span class="text-dim">(RF-1)</span></div>
      <div class="check-item"><span class="pass">✓</span> Headline losses/gains decomposed into cash vs. non-cash <span class="text-dim">(RF-3)</span></div>
      <div class="check-item"><span class="pass">✓</span> Data vintage labeled per line for time-sensitive figures <span class="text-dim">(RF-4)</span></div>
      <div class="check-item"><span class="pass">✓</span> Currency and share-class conversions verified <span class="text-dim">(RF-5, RF-6)</span></div>
      <div class="check-item"><span class="pass">✓</span> Data trail table present for top inputs</div>
      <div class="check-item"><span class="pass">✓</span> Estimates flagged with basis and sensitivity tested if verdict-moving</div>
    </div>
  </div>

  <!-- Vintage Notice -->
  <div class="callout">
    <strong>Data Vintage:</strong> All financial figures reflect Apple FY2025 (fiscal year ended September 2025) unless otherwise labeled. Quarterly data is Q1 FY2026 (calendar Oct–Dec 2025). Price as of 2026-04-15. Next scheduled refresh: post-Q2 FY2026 earnings (~May 2026).
  </div>
</div>
```

### Data Object Additions

```javascript
company.sources = {
  dataTrail: [
    { metric: 'Revenue FY2025', value: '$391.0B', source: 'Apple 10-K FY2025, Item 8', retrieved: '2026-04-10', vintage: 'FY2025 reported' },
    { metric: 'Owner Earnings (TTM)', value: '$108.5B', source: 'Derived from 10-K', retrieved: '2026-04-10', vintage: 'TTM Q1 2026' },
    // ... 5-10 verdict-moving inputs total
  ],
  generalSources: [
    { source: 'SEC EDGAR', document: '10-K Annual Report', date: 'FY2025', purpose: 'Primary financials' },
    // ...
  ],
  preVerdictChecklist: {
    tier1Verified: true,
    noPendingMAinSOTP: true,
    cashVsNonCashDecomposed: true,
    vintageLabeled: true,
    currencyVerified: true,
    dataTrailPresent: true,
    estimatesFlagged: true
  },
  vintage: {
    asOfDate: '2026-04-15',
    primaryFiscalYear: 'FY2025 (Sep 2025)',
    latestQuarter: 'Q1 FY2026',
    nextRefresh: 'Post-Q2 FY2026 earnings (~May 2026)'
  }
};
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

### Required Visual Components (non-Chart.js)

8. Quick-Kill Screener grid (8-cell pass/fail)
9. Moat Trend indicator (strength badge + directional arrow)
10. Sell Criteria Check table (4-row traffic light)
11. Value Trap Diagnostic table (5-row status check)
12. Inflation Scorecard card (6-factor +1/0/−1)
13. Industry KPI cards (sector-specific metrics)
14. Monitoring checklist & sell triggers panel
15. **Capital Allocation Scorecard table** (NEW — 5-row, in tab-management)
16. **Financial Strengths / Concerns dual callout** (NEW — in tab-financials)
17. **Downside Scenario card** (NEW — 3 stat cards + commentary, in tab-risk)
18. **Data Trail table** (NEW — 5–10 row verdict-moving inputs, in tab-sources)
19. **Pre-Verdict Checklist** (NEW — 7-item, in tab-sources)

Optional extras: Sensitivity heatmap (rendered as HTML table), scenario bar chart,
cash flow waterfall, dividend history, segment growth rates.

---

## Data Object Convention — UPDATED

When building the report, structure all company data in a single JavaScript object at the top of
the script section for clarity and maintainability. The object now includes business overview, management, financial observations, downside scenario, and sources blocks.

```javascript
const company = {
  name: { en: 'Apple Inc.', zh: '苹果公司' },
  ticker: 'AAPL',
  exchange: 'NASDAQ',
  currency: 'USD',
  currencySymbol: '$',
  analysisDate: '2026-04',
  dataVintage: 'FY2025 (Sep 2025)',

  // Current market data
  price: 178.50,
  marketCap: 2800e9,

  // Graham metrics
  grahamScore: { score: 4, max: 7, details: [...] },

  // Buffett metrics
  buffettScore: { score: 8, max: 10, details: [...] },

  // Business overview (NEW)
  businessOverview: {
    description: '[2-3 paragraph plain-language explanation]',
    industryContext: '[1-2 paragraph industry narrative]',
    businessModel: {
      revenueType: 'Mixed',
      revenueRecurringPct: 25,
      customerConcentration: 'Highly diversified — no single customer >5%',
      pricingModel: 'Premium',
      capitalIntensity: 'Asset-light'
    },
    geography: [
      { region: 'Americas', revenue: 167.0, pct: 43, growthYoY: 4 },
      { region: 'Europe', revenue: 102.0, pct: 26, growthYoY: 6 },
      { region: 'Greater China', revenue: 74.0, pct: 19, growthYoY: -8 },
      { region: 'Japan', revenue: 25.0, pct: 6, growthYoY: 3 },
      { region: 'Rest of Asia Pacific', revenue: 23.0, pct: 6, growthYoY: 12 }
    ]
  },

  // Management assessment (NEW)
  management: {
    leadership: [
      { name: 'Tim Cook', role: 'CEO', tenure: '13 yrs', background: 'Former COO; joined 1998' },
      // ...
    ],
    ownership: {
      insiderPct: 0.07,
      ceoPerformancePayPct: 85,
      buybacks5Y: { totalUSD: 480e9, avgPrice: 145, currentPrice: 178 },
      dividendStreakYears: 12,
      currentYieldPct: 0.5
    },
    capitalAllocation: [
      { use: 'Organic Reinvestment', amount: '$120B', assessment: '...', rating: 'Excellent' },
      // ...
    ],
    redFlags: { relatedParty: 'CLEAR', compensation: 'CLEAR', transparency: 'CLEAR', regulatory: 'CLEAR', notes: '' }
  },

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

  // Financial observations (NEW)
  financialObservations: {
    strengths: ['...', '...', '...'],
    concerns: ['...', '...', '...'],
    earningsQuality: {
      fcfToNetIncomePct: 108,
      revenueRecognition: 'Conservative',
      nonRecurringPattern: 'Clean',
      overallRating: 'HIGH',
      narrative: '...'
    }
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

  // Downside scenario (NEW)
  downsideScenario: {
    bearOwnerEarningsPerShare: 5.20,
    bearIntrinsicValue: 120,
    downsidePct: -33,
    protectionCommentary: '...'
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
  moatTrend: 'Stable',  // 'Widening' / 'Stable' / 'Narrowing'
  businessModelType: 'Franchise',  // 'Franchise' / 'Commodity' / 'Hybrid'

  // Quick-Kill Screener
  quickKill: {
    circleOfCompetence: 'PASS',
    durability: 'PASS',
    moat: 'PASS',
    pricingPower: 'PASS',
    earningsQuality: 'PASS',
    debtSafety: 'CONDITIONAL',
    managementIntegrity: 'PASS',
    reasonablePrice: 'CONDITIONAL',
    failCount: 0,
    conditionalCount: 2
  },

  // Sell Criteria
  sellCriteria: [
    { num: 1, criterion: 'Severely Overvalued?', triggered: false, basis: '...' },
    { num: 2, criterion: 'Moat Destroyed?', triggered: false, basis: '...' },
    { num: 3, criterion: 'Integrity Issue?', triggered: false, basis: '...' },
    { num: 4, criterion: 'Better Opportunity?', triggered: false, basis: '...' },
  ],

  // Value Trap Check
  valueTrapCheck: {
    structuralDecline: 'CLEAR',
    commodityBusiness: 'CLEAR',
    poorCapitalAllocation: 'CLEAR',
    heavyAssetsLowReturns: 'CLEAR',
    accountingQuality: 'CLEAR'
  },

  // Inflation Scorecard
  inflationScore: { pricingPower: 1, capitalIntensity: 1, roicLevel: 1,
                    inventoryExposure: 1, debtStructure: 0, inputCosts: 0, total: 4 },

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
  ],

  // Sources & Data Trail (NEW)
  sources: {
    dataTrail: [
      { metric: 'Revenue FY2025', value: '$391.0B', source: 'Apple 10-K FY2025, Item 8', retrieved: '2026-04-10', vintage: 'FY2025 reported' },
      // ... 5-10 verdict-moving inputs
    ],
    generalSources: [
      { source: 'SEC EDGAR', document: '10-K', date: 'FY2025', purpose: 'Primary financials' },
      // ...
    ],
    preVerdictChecklist: {
      tier1Verified: true,
      noPendingMAinSOTP: true,
      cashVsNonCashDecomposed: true,
      vintageLabeled: true,
      currencyVerified: true,
      dataTrailPresent: true,
      estimatesFlagged: true
    },
    vintage: {
      asOfDate: '2026-04-15',
      primaryFiscalYear: 'FY2025 (Sep 2025)',
      latestQuarter: 'Q1 FY2026',
      nextRefresh: 'Post-Q2 FY2026 earnings (~May 2026)'
    }
  }
};
```

This convention keeps data separate from rendering logic, making it easy to update figures
without modifying chart code.

---

## Currency & Market Conventions

| Market | Currency | Symbol | Format Example |
| --- | --- | --- | --- |
| US | USD | $ | $178.50 |
| HK | HKD | HK$ | HK$105.80 |
| China A-shares | CNY | ¥ | ¥42.30 |
| India | INR | ₹ | ₹2,450 |
| Singapore | SGD | S$ | S$12.50 |

For HK/China cross-listing: show both HKD and CNY where relevant, with exchange rate noted.

---

## Cross-References to Sister Skills

This template enforces the analytical scaffolding from:

- **`value-investing/SKILL.md`** — 10-step workflow (steps 1–10 map to tab structure)
- **`value-investing/references/data-sources.md`** — Source hierarchy, ±20% verdict-moving rule, RF-1 through RF-6 red flags, Data Trail format, Pre-Verdict Checklist (rendered in tab-sources)
- **`value-investing/references/sell-discipline-and-traps.md`** — Sell criteria check, value trap diagnostic (rendered in tab-risk)
- **`value-investing/references/inflation-goodwill-derivatives.md`** — Inflation scorecard (rendered in tab-risk)
- **`value-investing/references/industry-playbooks.md`** — Industry KPI cards (rendered in tab-industry)
- **`value-investing/references/portfolio-construction.md`** — Position sizing rationale (rendered in tab-verdict)

The HTML report is the visual surface for the analytical work done via these references. If a section in this template ever drifts from the underlying reference, the reference is canonical.
