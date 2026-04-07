# Portfolio Overview — Web Report Template

A comprehensive portfolio snapshot showing allocation, performance, risk metrics, and per-holding
summaries. Used for portfolio reviews, annual snapshots, and watchlist presentations.

---

## Page Structure

### Navigation: Tabbed (recommended for portfolios with 8+ holdings)

```
Tabs: Overview | Holdings | Performance | Risk & Scenarios | Watchlist
```

---

## Tab 1: Overview

### Required Content
- Portfolio value and date
- Asset allocation summary (equity / fixed income / cash / alternatives)
- Geographic allocation breakdown
- Sector allocation breakdown
- Top 5 holdings with weight, return, contribution
- Overall portfolio metrics: weighted P/E, weighted ROIC, avg MoS%, dividend yield

### Charts Required
1. **Asset Allocation Doughnut** — equity/bond/cash/alts split
2. **Geographic Allocation Doughnut** — US / HK-China / India / Other
3. **Sector Allocation Horizontal Bar** — ranked by weight

### KPI Stat Cards Row
```javascript
const portfolioStats = [
  { label: 'Total Value', labelZh: '总市值', value: '$127,450', change: '+12.3% YTD' },
  { label: 'Weighted P/E', labelZh: '加权市盈率', value: '16.8×' },
  { label: 'Weighted ROIC', labelZh: '加权ROIC', value: '22.4%' },
  { label: 'Avg Margin of Safety', labelZh: '平均安全边际', value: '+18%' },
  { label: 'Dividend Yield', labelZh: '股息收益率', value: '2.1%' },
  { label: 'Cash Position', labelZh: '现金仓位', value: '15%' },
];
```

---

## Tab 2: Holdings Detail

### Per-Holding Card Pattern

Each holding gets a condensed card with:
- Company name (EN/ZH), ticker, exchange
- Weight in portfolio (% bar)
- Cost basis → Current price → Unrealized P&L
- Graham Score / Buffett Score (mini badges)
- Moat rating (mini icon)
- MoS% with color indicator
- Verdict badge
- 1-line thesis

```html
<div class="holding-card">
  <div class="holding-header">
    <div>
      <h3><span class="en">Alphabet Inc.</span> <span class="zh">谷歌母公司</span></h3>
      <span class="ticker-badge">GOOGL · NASDAQ</span>
    </div>
    <div class="verdict-mini verdict-buy">BUY</div>
  </div>
  <div class="holding-metrics grid-4">
    <div class="metric">
      <span class="label">Weight <span class="zh">/ 仓位</span></span>
      <span class="value">12.5%</span>
      <div class="weight-bar"><div class="weight-fill" style="width:12.5%"></div></div>
    </div>
    <div class="metric">
      <span class="label">Cost → Price</span>
      <span class="value">$142 → $168</span>
      <span class="pnl positive">+18.3%</span>
    </div>
    <div class="metric">
      <span class="label">Scores</span>
      <span class="value">G: 5/7 · B: 8/10</span>
    </div>
    <div class="metric">
      <span class="label">MoS%</span>
      <span class="value mos-positive">+22%</span>
    </div>
  </div>
  <p class="thesis">Dominant search moat + Cloud growth trajectory + YouTube monetization at 18× forward P/E.</p>
</div>
```

### Holding Card CSS

```css
.holding-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px 24px;
  margin-bottom: 16px;
  transition: border-color 0.2s, transform 0.2s;
}
.holding-card:hover {
  border-color: var(--border-light);
  transform: translateY(-1px);
}
.holding-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 14px;
}
.ticker-badge {
  display: inline-block;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.78rem;
  color: var(--text-dim);
  background: var(--bg-surface);
  padding: 2px 8px;
  border-radius: 4px;
  margin-top: 4px;
}
.verdict-mini {
  padding: 4px 12px;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 1px;
}
.weight-bar {
  width: 100%;
  height: 4px;
  background: var(--bg-surface);
  border-radius: 2px;
  margin-top: 6px;
}
.weight-fill {
  height: 100%;
  background: var(--accent);
  border-radius: 2px;
}
.pnl { font-size: 0.85rem; font-weight: 600; }
.pnl.positive { color: var(--positive); }
.pnl.negative { color: var(--negative); }
.thesis {
  font-size: 0.85rem;
  color: var(--text-secondary);
  margin-top: 10px;
  line-height: 1.5;
  border-top: 1px solid var(--border);
  padding-top: 10px;
}
```

---

## Tab 3: Performance

### Charts Required
4. **Compound Growth Projection** (line chart — 5/10/20 year scenarios)
5. **Holding-Level Return Bar** (horizontal bar, sorted by return %)
6. **Dividend Income Projection** (bar chart — annual dividends over time)

### Compound Growth Projection

```javascript
function projectGrowth(initial, rate, years) {
  return Array.from({length: years + 1}, (_, i) => initial * Math.pow(1 + rate, i));
}

const projections = {
  labels: Array.from({length: 21}, (_, i) => `Year ${i}`),
  datasets: [
    { label: 'Conservative (7%)', data: projectGrowth(100000, 0.07, 20), borderColor: '#58a6ff', borderDash: [6,4] },
    { label: 'Base (10%)', data: projectGrowth(100000, 0.10, 20), borderColor: '#c9a84c' },
    { label: 'Optimistic (13%)', data: projectGrowth(100000, 0.13, 20), borderColor: '#3fb950' },
  ]
};
```

---

## Tab 4: Risk & Scenarios

### Required Content
- Portfolio-level risk metrics (concentration, geographic, sector)
- Correlation overview (which holdings move together)
- Bear case scenarios (3–5 macro scenarios with portfolio impact)
- Stress test results

### Charts Required
7. **Scenario Impact Bar** (bear scenarios showing portfolio drawdown %)
8. **Concentration Risk Treemap or Bar** (top 5 holdings as % of total)

### Scenario Card Pattern

```html
<div class="scenario-card">
  <div class="scenario-header">
    <span class="scenario-name">US-China Cold War Escalation</span>
    <span class="scenario-prob">Probability: 20%</span>
  </div>
  <div class="scenario-impact negative">Portfolio Impact: -22%</div>
  <p class="scenario-detail">HK/China holdings (Tencent, Alibaba, BYD) face -40 to -60% drawdown.
  US tech partially insulated. India holdings benefit from supply chain reallocation.</p>
  <div class="scenario-recovery">Expected Recovery: 18–24 months</div>
</div>
```

---

## Tab 5: Watchlist

### Required Content
- Stocks being monitored but not yet in portfolio
- Entry price targets
- Current price vs. target gap
- Trigger conditions for adding

### Watchlist Table

```html
<table class="watchlist">
  <thead>
    <tr>
      <th>Company</th>
      <th>Ticker</th>
      <th>Current Price</th>
      <th>Entry Target</th>
      <th>Gap</th>
      <th>Trigger</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Taiwan Semiconductor <span class="zh">/ 台积电</span></td>
      <td class="mono">TSM</td>
      <td class="mono">$168</td>
      <td class="mono">$140–$150</td>
      <td class="mono negative">-12%</td>
      <td>AI capex cycle correction or P/E < 18×</td>
    </tr>
  </tbody>
</table>
```

---

## Portfolio Data Schema

```javascript
const portfolio = {
  name: 'Global Value Portfolio',
  date: '2026-04',
  totalValue: 127450,
  currency: 'USD',
  
  allocation: {
    equity: 82,
    fixedIncome: 3,
    cash: 15,
    alternatives: 0
  },
  
  geographic: {
    us: 45,
    hkChina: 30,
    india: 15,
    other: 10
  },
  
  holdings: [
    {
      ticker: 'GOOGL',
      name: { en: 'Alphabet Inc.', zh: '谷歌母公司' },
      exchange: 'NASDAQ',
      weight: 12.5,
      shares: 9,
      costBasis: 142,
      currentPrice: 168,
      pnlPercent: 18.3,
      grahamScore: 5,
      buffettScore: 8,
      mosPercent: 22,
      moatRating: 'Wide',
      verdict: 'BUY',
      sector: 'Technology',
      market: 'us',
      thesis: 'Dominant search moat + Cloud growth at 18× forward P/E.'
    },
    // ... more holdings
  ],
  
  watchlist: [
    {
      ticker: 'TSM',
      name: { en: 'Taiwan Semiconductor', zh: '台积电' },
      currentPrice: 168,
      entryTarget: { low: 140, high: 150 },
      trigger: 'AI capex cycle correction or P/E < 18×'
    },
    // ...
  ],
  
  scenarios: [
    {
      name: 'US-China Cold War Escalation',
      probability: 20,
      impact: -22,
      detail: 'HK/China holdings face -40 to -60% drawdown...',
      recovery: '18–24 months'
    },
    // ...
  ],
  
  projections: {
    conservative: 0.07,
    base: 0.10,
    optimistic: 0.13
  }
};
```

---

## Color Scheme for Portfolio Reports

Portfolio reports typically use the **Dark Luxe** theme for a premium, Bloomberg-terminal feel:
- Background: `#06090f`
- Cards: `#0d1117`
- Accent: Gold `#c9a84c` for headers, highlights
- Positive: `#2ecc71` / `#3fb950`
- Negative: `#e74c3c` / `#f85149`

Alternatively, use **Dark Terminal** for a more analytical feel.
