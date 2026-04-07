# Design System Reference — Value Investing Web Reports

This document defines the complete visual language for all value investing HTML reports.
Load this file **every time** before creating a web report.

---

## 1. CSS Variables & Theming

### Dark Terminal Theme (Default)

```css
:root {
  /* Backgrounds */
  --bg: #0a1628;
  --bg-card: #0d1117;
  --bg-surface: #161b22;
  --bg-elevated: #1c2333;
  --bg-hover: #21262d;
  
  /* Borders */
  --border: #21262d;
  --border-light: #30363d;
  --border-accent: rgba(201, 168, 76, 0.15);
  
  /* Text */
  --text: #e8e6df;
  --text-secondary: #8b949e;
  --text-dim: #6e7681;
  --text-zh: #6db38a;
  
  /* Semantic Colors */
  --positive: #3fb950;
  --positive-bg: rgba(63, 185, 80, 0.1);
  --negative: #f85149;
  --negative-bg: rgba(248, 81, 73, 0.1);
  --warning: #d29922;
  --warning-bg: rgba(210, 153, 34, 0.1);
  --accent: #c9a84c;
  --accent-bg: rgba(201, 168, 76, 0.1);
  --info: #58a6ff;
  --info-bg: rgba(88, 166, 255, 0.1);
  
  /* Chart-specific */
  --chart-grid: rgba(255, 255, 255, 0.04);
  --chart-label: #8b949e;
}
```

### Light Editorial Theme

```css
:root {
  --bg: #faf9f6;
  --bg-card: #ffffff;
  --bg-surface: #f4f2ee;
  --bg-elevated: #ffffff;
  --bg-hover: #eeecea;
  
  --border: #e0ddd8;
  --border-light: #d5d2cd;
  --border-accent: rgba(26, 82, 118, 0.15);
  
  --text: #1a1a1a;
  --text-secondary: #555555;
  --text-dim: #999999;
  --text-zh: #4A6741;
  
  --positive: #1e8449;
  --positive-bg: rgba(30, 132, 73, 0.08);
  --negative: #c0392b;
  --negative-bg: rgba(192, 57, 43, 0.08);
  --warning: #d4ac0d;
  --warning-bg: rgba(212, 172, 13, 0.08);
  --accent: #1a5276;
  --accent-bg: rgba(26, 82, 118, 0.06);
  --info: #2980b9;
  --info-bg: rgba(41, 128, 185, 0.06);
  
  --chart-grid: rgba(0, 0, 0, 0.06);
  --chart-label: #555555;
}
```

### Dark Luxe Theme (Portfolio / Premium)

```css
:root {
  --bg: #06090f;
  --bg-card: #0d1117;
  --bg-surface: #111820;
  --bg-elevated: #161b22;
  --bg-hover: #1c2333;
  
  --border: #1c2333;
  --border-light: #21262d;
  --border-accent: rgba(201, 168, 76, 0.2);
  
  --text: #e6edf3;
  --text-secondary: #8892a4;
  --text-dim: #6e7681;
  --text-zh: #6db38a;
  
  --positive: #2ecc71;
  --negative: #e74c3c;
  --warning: #e8a832;
  --accent: #c9a84c;
  --info: #5b8def;
  
  --chart-grid: rgba(255, 255, 255, 0.035);
  --chart-label: #8892a4;
}
```

---

## 2. Typography

### Font Stacks (Google Fonts imports)

```css
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Source+Sans+3:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=Noto+Sans+SC:wght@300;400;500;700&display=swap');
```

| Role | Font | Fallback |
|------|------|----------|
| Display / H1 | `Playfair Display` | Georgia, serif |
| Body / UI | `Source Sans 3` | Helvetica Neue, sans-serif |
| Mono / Data | `IBM Plex Mono` | monospace |
| Chinese | `Noto Sans SC` | Microsoft YaHei, sans-serif |

### Type Scale

```css
.display-xl { font-family: 'Playfair Display', serif; font-size: clamp(2rem, 4vw, 3.5rem); font-weight: 900; line-height: 1.1; }
.display-lg { font-family: 'Playfair Display', serif; font-size: clamp(1.5rem, 3vw, 2.5rem); font-weight: 700; line-height: 1.2; }
h1 { font-family: 'Playfair Display', serif; font-size: 1.8rem; font-weight: 700; }
h2 { font-family: 'Source Sans 3', sans-serif; font-size: 1.25rem; font-weight: 600; letter-spacing: -0.01em; }
h3 { font-family: 'Source Sans 3', sans-serif; font-size: 1.05rem; font-weight: 600; }
body { font-family: 'Source Sans 3', sans-serif; font-size: 0.95rem; line-height: 1.65; }
.mono { font-family: 'IBM Plex Mono', monospace; font-size: 0.88rem; }
.zh { font-family: 'Noto Sans SC', 'Microsoft YaHei', sans-serif; color: var(--text-zh); font-size: 0.88em; }
```

### Alternative Font Combinations (vary across reports)

Choose a different display font for variety. Validated options:

| Display Font | Vibe | Import |
|-------------|------|--------|
| `Playfair Display` | Classic editorial | Standard |
| `DM Serif Display` | Modern editorial | `family=DM+Serif+Display:ital@0;1` |
| `Fraunces` | Warm, literary | `family=Fraunces:wght@400;700;900` |
| `Libre Baskerville` | Traditional finance | `family=Libre+Baskerville:wght@400;700` |
| `Cormorant Garamond` | Elegant, European | `family=Cormorant+Garamond:wght@400;600;700` |

Body font alternatives: `DM Sans`, `Work Sans`, `Outfit`, `Plus Jakarta Sans`.

---

## 3. Layout Patterns

### Container

```css
.container { max-width: 1280px; margin: 0 auto; padding: 0 24px; position: relative; z-index: 1; }

@media (max-width: 768px) {
  .container { padding: 0 16px; }
}
```

### Grid Systems

```css
.grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
.grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }

@media (max-width: 900px) {
  .grid-2, .grid-3 { grid-template-columns: 1fr; }
  .grid-4 { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
  .grid-4 { grid-template-columns: 1fr; }
}
```

### Card Component

```css
.card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 24px;
  transition: border-color 0.2s;
}
.card:hover { border-color: var(--border-light); }
```

### Chart Container

```css
.chart-container { position: relative; height: 320px; margin: 16px 0; }
.chart-container-sm { position: relative; height: 240px; margin: 12px 0; }
.chart-container-lg { position: relative; height: 420px; margin: 20px 0; }
```

---

## 4. Hero / Header Patterns

### Pattern A — Full-width gradient header (default for single stock)

```html
<header class="hero">
  <div class="container">
    <div class="hero-eyebrow">VALUE INVESTING ANALYSIS</div>
    <h1 class="display-xl">
      <span class="en">Company Name</span>
      <span class="zh">公司中文名</span>
    </h1>
    <div class="hero-meta">
      <span class="ticker">TICKER · EXCHANGE</span>
      <span class="date">Analysis Date: YYYY-MM</span>
    </div>
    <div class="verdict-badge verdict-buy">BUY — 买入</div>
  </div>
</header>
```

```css
.hero {
  background: linear-gradient(135deg, var(--bg) 0%, var(--bg-surface) 50%, var(--bg) 100%);
  padding: 56px 0 44px;
  border-bottom: 1px solid var(--border);
  position: relative;
  overflow: hidden;
}
.hero::before {
  content: '';
  position: absolute;
  top: -200px; right: -100px;
  width: 600px; height: 600px;
  background: radial-gradient(circle, rgba(201,168,76,0.04) 0%, transparent 70%);
  pointer-events: none;
}
.hero-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: var(--accent-bg);
  border: 1px solid rgba(201,168,76,0.2);
  padding: 5px 14px;
  border-radius: 100px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 16px;
}
```

### Verdict Badge

```css
.verdict-badge {
  display: inline-block;
  padding: 8px 24px;
  border-radius: 6px;
  font-weight: 700;
  font-size: 1.1rem;
  letter-spacing: 1px;
  margin-top: 16px;
}
.verdict-buy { background: var(--positive-bg); color: var(--positive); border: 1px solid rgba(63,185,80,0.3); }
.verdict-hold { background: var(--warning-bg); color: var(--warning); border: 1px solid rgba(210,153,34,0.3); }
.verdict-avoid { background: var(--negative-bg); color: var(--negative); border: 1px solid rgba(248,81,73,0.3); }
```

---

## 5. Navigation Patterns

### Tab Navigation (for dense reports with many sections)

```html
<nav class="tabs">
  <button class="tab-btn active" onclick="showTab('summary')">Executive Summary</button>
  <button class="tab-btn" onclick="showTab('financials')">Financials</button>
  <button class="tab-btn" onclick="showTab('valuation')">Valuation</button>
  <button class="tab-btn" onclick="showTab('moat')">Moat</button>
  <button class="tab-btn" onclick="showTab('risk')">Risk</button>
  <button class="tab-btn" onclick="showTab('verdict')">Verdict</button>
</nav>
```

```javascript
function showTab(tabId) {
  document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
  document.getElementById('tab-' + tabId).classList.add('active');
  event.target.classList.add('active');
  // Destroy and recreate charts for the active tab to fix Chart.js sizing
  window.dispatchEvent(new Event('resize'));
}
```

```css
.tabs {
  display: flex;
  gap: 4px;
  margin-bottom: 24px;
  flex-wrap: wrap;
  border-bottom: 1px solid var(--border);
  padding-bottom: 0;
}
.tab-btn {
  padding: 10px 20px;
  cursor: pointer;
  border: none;
  background: transparent;
  color: var(--text-secondary);
  font-size: 0.9rem;
  font-weight: 500;
  border-bottom: 2px solid transparent;
  transition: all 0.2s;
}
.tab-btn:hover { color: var(--text); }
.tab-btn.active {
  color: var(--accent);
  border-bottom-color: var(--accent);
}
.tab-content { display: none; }
.tab-content.active { display: block; }
```

### Sticky Sidebar ToC (for long scrollable reports)

```css
.toc {
  position: sticky;
  top: 24px;
  max-height: calc(100vh - 48px);
  overflow-y: auto;
  padding-right: 16px;
}
.toc a {
  display: block;
  padding: 6px 12px;
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 0.85rem;
  border-left: 2px solid transparent;
  transition: all 0.2s;
}
.toc a:hover, .toc a.active {
  color: var(--accent);
  border-left-color: var(--accent);
}
```

---

## 6. Table Patterns

### Scorecard Table (pass/fail)

```css
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}
th {
  text-align: left;
  padding: 10px 14px;
  background: var(--bg-surface);
  color: var(--text-secondary);
  font-weight: 600;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  border-bottom: 1px solid var(--border);
}
td {
  padding: 10px 14px;
  border-bottom: 1px solid var(--border);
}
tr:hover { background: var(--bg-hover); }
.pass { color: var(--positive); font-weight: 600; }
.fail { color: var(--negative); font-weight: 600; }
.partial { color: var(--warning); font-weight: 600; }
```

### Sensitivity Table (green/red gradient)

```javascript
function renderSensitivityTable(container, matrix, growthRates, discountRates, currentPrice, currency) {
  let html = '<table class="sensitivity"><tr><th>Growth↓ DR→</th>';
  discountRates.forEach(dr => html += `<th>${dr}%</th>`);
  html += '</tr>';
  
  growthRates.forEach((g, i) => {
    html += `<tr><td class="row-label">${g}%</td>`;
    discountRates.forEach((dr, j) => {
      const val = matrix[i][j];
      const isAbove = val > currentPrice;
      const intensity = Math.min(Math.abs(val - currentPrice) / currentPrice * 3, 1);
      const bg = isAbove
        ? `rgba(63,185,80,${0.08 + intensity * 0.2})`
        : `rgba(248,81,73,${0.08 + intensity * 0.2})`;
      const color = isAbove ? 'var(--positive)' : 'var(--negative)';
      html += `<td style="background:${bg};color:${color};font-weight:600;text-align:center;font-family:'IBM Plex Mono',monospace">${currency}${val.toFixed(0)}</td>`;
    });
    html += '</tr>';
  });
  html += '</table>';
  container.innerHTML = html;
}
```

---

## 7. Chart.js Configuration

### Global Defaults (set once at script top)

```javascript
Chart.defaults.font.family = "'Source Sans 3', 'Noto Sans SC', sans-serif";
Chart.defaults.font.size = 12;
Chart.defaults.color = getComputedStyle(document.documentElement).getPropertyValue('--chart-label').trim() || '#8b949e';
Chart.defaults.plugins.legend.position = 'bottom';
Chart.defaults.plugins.legend.labels.usePointStyle = true;
Chart.defaults.plugins.legend.labels.padding = 16;
Chart.defaults.responsive = true;
Chart.defaults.maintainAspectRatio = false;
```

### Standard Chart Types for Value Investing

#### Revenue & Profit Bar + Growth Line (combo)

```javascript
{
  type: 'bar',
  data: {
    labels: years,
    datasets: [
      { label: 'Revenue (B)', data: revData, backgroundColor: 'rgba(88,166,255,0.6)', borderRadius: 6, yAxisID: 'y' },
      { label: 'Net Profit (B)', data: profitData, backgroundColor: 'rgba(63,185,80,0.6)', borderRadius: 6, yAxisID: 'y' },
      { label: 'Revenue Growth %', data: growthData, type: 'line', borderColor: '#c9a84c', pointRadius: 4, tension: 0.3, yAxisID: 'y1' }
    ]
  },
  options: {
    scales: {
      y: { grid: { color: 'var(--chart-grid)' }, ticks: { callback: v => currency + v + 'B' } },
      y1: { position: 'right', grid: { display: false }, ticks: { callback: v => v + '%' } }
    }
  }
}
```

#### Intrinsic Value Horizontal Bar

```javascript
{
  type: 'bar',
  data: {
    labels: ['Current Price', 'Graham Number', 'EPV', 'DCF Bear', 'DCF Base', 'DCF Bull'],
    datasets: [{
      data: [price, graham, epv, dcfBear, dcfBase, dcfBull],
      backgroundColor: [
        'rgba(248,81,73,0.7)',   // current price — red tone
        'rgba(88,166,255,0.7)',  // graham — blue
        'rgba(88,166,255,0.5)',  // epv — lighter blue
        'rgba(63,185,80,0.4)',   // bear — light green
        'rgba(63,185,80,0.7)',   // base — green
        'rgba(63,185,80,0.9)'   // bull — strong green
      ],
      borderRadius: 6
    }]
  },
  options: {
    indexAxis: 'y',
    plugins: {
      legend: { display: false },
      annotation: {
        annotations: {
          priceLine: {
            type: 'line', xMin: price, xMax: price,
            borderColor: 'rgba(248,81,73,0.8)', borderWidth: 2, borderDash: [6,4],
            label: { content: 'Current Price', enabled: true }
          }
        }
      }
    }
  }
}
```

#### Moat Radar Chart

```javascript
{
  type: 'radar',
  data: {
    labels: [
      'Intangible Assets\n无形资产',
      'Switching Costs\n转换成本',
      'Network Effects\n网络效应',
      'Cost Advantages\n成本优势',
      'Efficient Scale\n规模效益'
    ],
    datasets: [{
      label: companyName,
      data: [moat1, moat2, moat3, moat4, moat5],
      fill: true,
      backgroundColor: 'rgba(201,168,76,0.15)',
      borderColor: '#c9a84c',
      pointBackgroundColor: '#c9a84c',
      pointRadius: 5
    }]
  },
  options: {
    scales: { r: { min: 0, max: 3, ticks: { stepSize: 1, backdropColor: 'transparent' } } }
  }
}
```

#### Margin Trend Line Chart

```javascript
{
  type: 'line',
  data: {
    labels: years,
    datasets: [
      { label: 'Gross Margin %', data: gmData, borderColor: '#58a6ff', fill: false, tension: 0.3 },
      { label: 'EBIT Margin %', data: ebitData, borderColor: '#c9a84c', fill: false, tension: 0.3 },
      { label: 'Net Margin %', data: nmData, borderColor: '#3fb950', fill: false, tension: 0.3 }
    ]
  },
  options: {
    scales: {
      y: { ticks: { callback: v => v + '%' }, grid: { color: 'var(--chart-grid)' } },
      x: { grid: { display: false } }
    }
  }
}
```

#### Scenario Valuation Doughnut / Bar

```javascript
// Probability-weighted scenario chart
{
  type: 'bar',
  data: {
    labels: ['Bear Case\n悲观', 'Base Case\n基准', 'Bull Case\n乐观', 'Expected Value\n期望值'],
    datasets: [{
      data: [bearIV, baseIV, bullIV, expectedIV],
      backgroundColor: ['rgba(248,81,73,0.6)', 'rgba(88,166,255,0.6)', 'rgba(63,185,80,0.6)', 'rgba(201,168,76,0.8)'],
      borderRadius: 8
    }]
  },
  options: {
    plugins: {
      legend: { display: false },
      tooltip: {
        callbacks: {
          afterLabel: (ctx) => {
            const probs = [bearProb, baseProb, bullProb, ''];
            return probs[ctx.dataIndex] ? `Probability: ${probs[ctx.dataIndex]}%` : '';
          }
        }
      }
    }
  }
}
```

#### ROIC / ROE Historical Line with WACC Overlay

```javascript
{
  type: 'line',
  data: {
    labels: years,
    datasets: [
      { label: 'ROIC %', data: roicData, borderColor: '#58a6ff', fill: false, tension: 0.3, pointRadius: 4 },
      { label: 'ROE %', data: roeData, borderColor: '#3fb950', fill: false, tension: 0.3, pointRadius: 4 },
      { label: 'WACC %', data: waccData, borderColor: '#f85149', borderDash: [6,4], fill: false, pointRadius: 0 }
    ]
  }
}
```

#### Peer Comparison Horizontal Bar

```javascript
{
  type: 'bar',
  data: {
    labels: peerNames,
    datasets: [{
      label: 'P/E Ratio',
      data: peerPE,
      backgroundColor: peerNames.map((_, i) => i === targetIdx ? '#c9a84c' : 'rgba(88,166,255,0.5)'),
      borderRadius: 6
    }]
  },
  options: { indexAxis: 'y' }
}
```

---

## 8. Special Components

### KPI Stat Card

```html
<div class="stat-card">
  <div class="stat-label"><span class="en">Revenue</span> <span class="zh">/ 营业收入</span></div>
  <div class="stat-value">¥123.4B</div>
  <div class="stat-change positive">+15.2% YoY</div>
</div>
```

```css
.stat-card {
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 16px 20px;
}
.stat-label { font-size: 0.82rem; color: var(--text-secondary); margin-bottom: 6px; }
.stat-value { font-family: 'IBM Plex Mono', monospace; font-size: 1.6rem; font-weight: 600; }
.stat-change { font-size: 0.82rem; margin-top: 4px; }
.stat-change.positive { color: var(--positive); }
.stat-change.negative { color: var(--negative); }
```

### Risk Meter

```html
<div class="risk-row">
  <span class="risk-label">China Regulatory Risk</span>
  <div class="risk-meter">
    <div class="risk-fill" style="width: 80%; background: var(--negative);"></div>
  </div>
  <span class="risk-score">4/5</span>
</div>
```

```css
.risk-meter {
  flex: 1;
  height: 8px;
  background: var(--bg-surface);
  border-radius: 4px;
  overflow: hidden;
  margin: 0 12px;
}
.risk-fill {
  height: 100%;
  border-radius: 4px;
  transition: width 0.6s ease;
}
```

### Callout / Highlight Box

```css
.callout {
  background: var(--accent-bg);
  border-left: 3px solid var(--accent);
  padding: 16px 20px;
  border-radius: 0 8px 8px 0;
  margin: 16px 0;
}
.callout.positive { background: var(--positive-bg); border-left-color: var(--positive); }
.callout.negative { background: var(--negative-bg); border-left-color: var(--negative); }
```

---

## 9. Animations & Micro-interactions

### Page Load Stagger

```css
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
.card, .stat-card {
  animation: fadeUp 0.5s ease forwards;
  opacity: 0;
}
.card:nth-child(1) { animation-delay: 0.1s; }
.card:nth-child(2) { animation-delay: 0.2s; }
.card:nth-child(3) { animation-delay: 0.3s; }
/* etc */
```

### Hover Effects

```css
.card { transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s; }
.card:hover {
  transform: translateY(-2px);
  border-color: var(--border-light);
  box-shadow: 0 8px 24px rgba(0,0,0,0.15);
}
```

---

## 10. Background Atmospheric Effects

### Radial Gradient Glow

```css
.bg-pattern {
  position: fixed; top: 0; left: 0; right: 0; bottom: 0; z-index: 0;
  background:
    radial-gradient(ellipse at 20% 50%, rgba(201,168,76,0.04) 0%, transparent 60%),
    radial-gradient(ellipse at 80% 20%, rgba(88,166,255,0.03) 0%, transparent 50%),
    linear-gradient(180deg, var(--bg) 0%, var(--bg-surface) 50%, var(--bg) 100%);
  pointer-events: none;
}
```

### Noise Texture Overlay

```css
.noise {
  position: fixed; top: 0; left: 0; width: 100%; height: 100%;
  pointer-events: none; z-index: 9999; opacity: 0.3;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");
}
```

---

## 11. Print Styles

```css
@media print {
  body { background: #fff !important; color: #000 !important; }
  .tabs, .toc, .bg-pattern, .noise { display: none !important; }
  .tab-content { display: block !important; break-inside: avoid; }
  .card { border: 1px solid #ddd !important; break-inside: avoid; }
  .hero { background: none !important; border-bottom: 2px solid #1a5276 !important; }
}
```

---

## 12. Disclaimer Footer

Always include:

```html
<footer class="disclaimer">
  <div class="container">
    <p>
      <span class="en">This report is for informational and educational purposes only and does not constitute investment advice.
      Always conduct your own research and consult a licensed financial advisor before making investment decisions.</span>
      <br>
      <span class="zh">本报告仅供参考和教育用途，不构成投资建议。在做出投资决定之前，请务必进行独立研究并咨询持牌财务顾问。</span>
    </p>
    <p class="meta">Generated with Claude · Data vintage: [DATE] · Analysis framework: Graham-Buffett</p>
  </div>
</footer>
```

```css
.disclaimer {
  margin-top: 60px;
  padding: 24px 0;
  border-top: 1px solid var(--border);
  font-size: 0.78rem;
  color: var(--text-dim);
  text-align: center;
}
```
