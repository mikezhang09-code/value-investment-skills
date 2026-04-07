---
name: value-investing-web-report
description: >
  Creates stunning, interactive single-file HTML web page reports for value investing analysis —
  the web counterpart to the finance-documents (.docx/.pdf) skill. Use this skill whenever the user
  wants to: generate an HTML report for a stock analysis, convert an existing analysis to a web page,
  create an interactive investment dashboard with Chart.js visualizations, build a bilingual
  (English/Chinese) equity research page, produce a portfolio overview as a web report, or export
  analysis as an interactive HTML file. Triggers include: "create a web report", "generate an HTML
  report", "convert to web page", "make an interactive report", "build a web dashboard for [stock]",
  "HTML analysis", any request for a visually rich stock analysis deliverable, or whenever the user
  says "report" and the output should be an HTML file rather than Word/PDF. Also trigger proactively
  when the user has completed a value investing analysis and would benefit from an interactive
  HTML presentation — especially for analyses with charts, sensitivity tables, or moat radar data.
  Always use alongside the value-investing skill for analytical content and the hk-china-us-india-equities
  skill for market-specific context.
---

# Value Investing Web Report Skill

Produces institutional-quality, interactive HTML web reports for value investing analysis. These are
single-file, self-contained HTML pages with Chart.js visualizations, bilingual English/Chinese
labeling, and editorial-grade typography — ready for local viewing or GitHub Pages deployment.

**Always read the relevant reference file(s) before writing any HTML:**

| Report Type | Reference File |
|------------|---------------|
| Single stock analysis (full report) | `references/single-stock-report.md` |
| Multi-stock screening / comparison | `references/multi-stock-report.md` |
| Portfolio overview / review | `references/portfolio-report.md` |
| Design system (colors, typography, components) | `references/design-system.md` |

Load `references/design-system.md` **every time** — it contains the CSS variables, Chart.js
defaults, component patterns, and aesthetic guidelines that ensure visual consistency.

---

## Report Types

### 1. Single Stock Analysis Report (most common)
The flagship output — a comprehensive, tabbed or scrollable analysis page for one company.
Sections: Executive Summary → Business Overview → Financial Scorecard → Valuation Analysis →
Moat Analysis → Risk Assessment → Investment Verdict.
**Read**: `references/single-stock-report.md` + `references/design-system.md`

### 2. Multi-Stock Comparison Report
Side-by-side or ranked comparison of multiple companies — used after screening.
Features: sortable tables, filter controls, expandable rows, comparison charts.
**Read**: `references/multi-stock-report.md` + `references/design-system.md`

### 3. Portfolio Overview Report
Full portfolio snapshot with allocation, performance, risk metrics, and per-holding summaries.
**Read**: `references/portfolio-report.md` + `references/design-system.md`

---

## Core Technical Stack

| Layer | Choice | CDN |
|-------|--------|-----|
| Charts | Chart.js 4.x | `https://cdn.jsdelivr.net/npm/chart.js` or `https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js` |
| Fonts | Google Fonts (display + body + CJK) | Google Fonts API |
| JS | Vanilla JS — no frameworks, no build step | — |
| Format | Single self-contained `.html` file | — |
| CJK | Noto Sans SC or Microsoft YaHei fallback | Google Fonts |

---

## Aesthetic Direction

These reports aim for **editorial financial journalism** meets **dark-mode data terminal** —
the visual feel of a Bloomberg Terminal crossed with a Long Now Foundation essay. Not generic
dashboard UI. Not corporate PowerPoint. The reports should feel like they were designed by a
financial publication's art director.

**Three validated aesthetic themes** (choose per report context):

| Theme | When to Use | Feel |
|-------|-----------|------|
| **Dark Terminal** | Default for single-stock deep dives, HK/China equities | Dark navy/charcoal bg, gold accents, editorial serif headers |
| **Light Editorial** | Clean comparison reports, educational content | Warm white bg, deep navy accents, classic financial publication feel |
| **Dark Luxe** | Portfolio overviews, high-conviction picks | Black bg, gold typography, premium feel |

---

## Bilingual Convention

| Element | English | Chinese |
|---------|---------|---------|
| Section headers | Primary, larger | Secondary, smaller, muted green |
| Chart labels | Left or primary | Right or subtitle |
| KPI labels | Bold standard | Appended with `/` separator |
| CSS class | `.en` | `.zh` |
| Color | `#333333` (light) or `#e8e6df` (dark) | `#4A6741` (light) or `#6db38a` (dark) |

Pattern:
```html
<h2><span class="en">Intrinsic Value Range</span> <span class="zh">/ 内在价值区间</span></h2>
```

---

## Key Chinese Financial Terms

| English | Chinese |
|---------|---------|
| Margin of Safety | 安全边际 |
| Intrinsic Value | 内在价值 |
| Economic Moat | 经济护城河 |
| Graham Number | 格雷厄姆数 |
| Owner Earnings | 所有者收益 |
| ROIC | 投入资本回报率 |
| FCF Yield | 自由现金流收益率 |
| Earnings Yield | 盈利收益率 |
| Price-to-Book | 市净率 |
| Price-to-Earnings | 市盈率 |
| Circle of Competence | 能力圈 |
| Dividend Yield | 股息收益率 |
| Net Asset Value | 净资产值 |
| Revenue | 营业收入 |
| Net Profit | 净利润 |
| Gross Margin | 毛利率 |
| Debt-to-Equity | 资产负债率 |
| Current Ratio | 流动比率 |
| Risk Assessment | 风险评估 |
| Investment Verdict | 投资判定 |
| Position Sizing | 仓位管理 |
| Bear / Base / Bull | 悲观 / 基准 / 乐观 |

---

## Workflow

1. **Load design system**: Always read `references/design-system.md` first
2. **Load report template**: Read the appropriate template reference
3. **Gather data**: From prior analysis, user input, or web search
4. **Build HTML**: Create the single-file HTML in `/home/claude/`
5. **Copy to outputs**: `cp /home/claude/report.html /mnt/user-data/outputs/[name].html`
6. **Present**: Use `present_files` tool

---

## Quality Checklist

Before delivering, verify:
- [ ] Single self-contained HTML file (no external dependencies except CDN)
- [ ] Chart.js loads from CDN, not inline
- [ ] All fonts load from Google Fonts
- [ ] Responsive: looks good on 320px mobile through 1440px desktop
- [ ] Bilingual labels on all section headers and key metrics
- [ ] Verdict badge prominently displayed (BUY green / HOLD amber / AVOID red)
- [ ] Disclaimer footer present
- [ ] Data vintage noted (TTM, FY year, date of analysis)
- [ ] At least 5 Chart.js visualizations for single-stock reports
- [ ] Color-coded pass/fail on scorecard tables
- [ ] Sensitivity table with green/red cell shading
- [ ] Smooth scrolling and/or tab navigation
- [ ] Print-friendly (media query hides nav, forces light background)
