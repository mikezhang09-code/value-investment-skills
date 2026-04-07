# Multi-Stock Comparison — Web Report Template

For screening dashboards, sector comparisons, and ranked stock lists. Supports 3–50 stocks
in a single report with sortable tables, filter controls, and comparison charts.

---

## Layout Patterns

### Pattern A: Ranked Table with Expandable Rows (up to 50 stocks)

Best for dividend dashboards, screening results, and large lists.

```
┌──────────────────────────────────────────────────────────┐
│  HEADER: Title | Date | Filter dropdowns | Sort controls  │
├──────┬──────────┬──────────────────────────────────────────┤
│ Rank │ Company  │ Key Metrics (horizontally scrollable)     │
│      │ Ticker   │ Graham | Buffett | MoS% | P/E | ROIC    │
├──────┼──────────┼──────────────────────────────────────────┤
│  1   │ BRK.B    │ ██████ 6/7  │ █████████ 9/10 │ 28%     │
│  ▼ expanded details: mini radar, thesis snippet, etc.     │
│  2   │ GOOGL    │ █████░ 5/7  │ ████████░ 8/10 │ 22%     │
└──────┴──────────┴──────────────────────────────────────────┘
```

### Pattern B: Card Grid with Side-by-Side Compare (3–10 stocks)

Best for sector comparisons, portfolio candidates, and moat analysis.

```
┌──────────┐  ┌──────────┐  ┌──────────┐
│ Stock A  │  │ Stock B  │  │ Stock C  │
│ Ticker   │  │ Ticker   │  │ Ticker   │
│ Score    │  │ Score    │  │ Score    │
│ MoS %    │  │ MoS %    │  │ MoS %    │
│ Verdict  │  │ Verdict  │  │ Verdict  │
│ [Detail] │  │ [Detail] │  │ [Detail] │
└──────────┘  └──────────┘  └──────────┘
```

---

## Interactive Features

### Sortable Table Headers

```javascript
let sortCol = 'mosPercent';
let sortDir = 'desc';

function sortTable(col) {
  if (sortCol === col) sortDir = sortDir === 'asc' ? 'desc' : 'asc';
  else { sortCol = col; sortDir = 'desc'; }
  renderTable();
}

function renderTable() {
  const sorted = [...stocks].sort((a, b) => {
    const va = a[sortCol], vb = b[sortCol];
    return sortDir === 'asc' ? va - vb : vb - va;
  });
  // Rebuild table rows...
}
```

### Filter Controls

```html
<div class="filters">
  <select id="sectorFilter" onchange="filterTable()">
    <option value="all">All Sectors</option>
    <option value="tech">Technology</option>
    <option value="finance">Financials</option>
    <!-- ... -->
  </select>
  <select id="marketFilter" onchange="filterTable()">
    <option value="all">All Markets</option>
    <option value="us">US (NYSE/NASDAQ)</option>
    <option value="hk">Hong Kong (HKEx)</option>
    <option value="india">India (NSE/BSE)</option>
  </select>
  <div class="range-filter">
    <label>Min MoS%: <input type="range" min="-50" max="50" value="0" oninput="filterTable()"></label>
  </div>
</div>
```

### Expandable Row

```javascript
function toggleRow(ticker) {
  const detail = document.getElementById('detail-' + ticker);
  if (detail.style.display === 'none') {
    detail.style.display = 'table-row';
    // Lazy-init chart if needed
    if (!detail.chartInit) {
      initMiniRadar(ticker);
      detail.chartInit = true;
    }
  } else {
    detail.style.display = 'none';
  }
}
```

---

## Comparison Charts

### 1. Multi-Stock Valuation Scatter (P/E vs. ROIC)

```javascript
{
  type: 'scatter',
  data: {
    datasets: stocks.map(s => ({
      label: s.ticker,
      data: [{ x: s.pe, y: s.roic }],
      pointRadius: Math.max(6, Math.min(20, s.marketCap / 100e9)),  // size by market cap
      backgroundColor: s.mosPercent > 20 ? 'rgba(63,185,80,0.6)' :
                        s.mosPercent > 0  ? 'rgba(210,153,34,0.6)' :
                                            'rgba(248,81,73,0.6)'
    }))
  },
  options: {
    scales: {
      x: { title: { display: true, text: 'P/E Ratio' } },
      y: { title: { display: true, text: 'ROIC %' } }
    }
  }
}
```

### 2. MoS% Horizontal Bar (ranked)

```javascript
{
  type: 'bar',
  data: {
    labels: stocks.map(s => s.ticker),
    datasets: [{
      data: stocks.map(s => s.mosPercent),
      backgroundColor: stocks.map(s =>
        s.mosPercent > 20 ? 'rgba(63,185,80,0.7)' :
        s.mosPercent > 0  ? 'rgba(210,153,34,0.7)' :
                            'rgba(248,81,73,0.7)'
      ),
      borderRadius: 6
    }]
  },
  options: {
    indexAxis: 'y',
    plugins: { legend: { display: false } },
    scales: {
      x: {
        ticks: { callback: v => v + '%' },
        grid: { color: 'var(--chart-grid)' }
      }
    }
  }
}
```

### 3. Sector / Market Allocation Doughnut

For portfolio-style comparisons showing market or sector distribution.

### 4. Moat Comparison Radar (overlay 2–4 stocks)

```javascript
{
  type: 'radar',
  data: {
    labels: ['Intangible Assets', 'Switching Costs', 'Network Effects', 'Cost Advantages', 'Efficient Scale'],
    datasets: selectedStocks.map((s, i) => ({
      label: s.ticker,
      data: [s.moat.ia, s.moat.sc, s.moat.ne, s.moat.ca, s.moat.es],
      fill: true,
      backgroundColor: `rgba(${chartColors[i]}, 0.1)`,
      borderColor: chartColorsSolid[i]
    }))
  }
}
```

---

## Data Schema for Multi-Stock

```javascript
const stocks = [
  {
    ticker: 'AAPL', name: { en: 'Apple Inc.', zh: '苹果公司' },
    exchange: 'NASDAQ', sector: 'Technology', market: 'us',
    price: 178.50, marketCap: 2800e9, currency: 'USD',
    pe: 28.5, pb: 42, roic: 38, roe: 145, grossMargin: 44,
    grahamScore: 4, buffettScore: 8,
    mosPercent: -7, verdict: 'HOLD',
    moat: { ia: 3, sc: 2.5, ne: 2, ca: 1, es: 0.5 },
    thesis: 'Ecosystem moat is impenetrable but fully priced.',
  },
  // ... more stocks
];
```

---

## Cross-Market Display Conventions

When comparing stocks across US, HK, and India markets:

- Show currency in each stock's local currency
- Include a "Normalized P/E" column that adjusts for market risk premium
- Flag VIE structures, SOEs, and family-controlled groups with icons:
  - 🏛️ SOE  · ⚠️ VIE  · 👨‍👩‍👦 Family  · 🔄 ADR/Dual-listed
- Sort by MoS% descending by default (most undervalued first)
