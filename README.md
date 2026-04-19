# Value Investment Skills

A Claude Code skill for deep fundamental research and value investing analysis, inspired by the principles of Benjamin Graham, Warren Buffett, Charlie Munger, and Philip Fisher.

## What This Skill Does

When installed, this skill gives Claude the ability to:

- Research any publicly listed company as a seasoned fundamental analyst
- **Quick-Kill screen** stocks with an 8-question pass/fail gate before deep analysis
- Perform 10-year financial deep dives (revenue, margins, ROE, ROIC, FCF, etc.)
- Assess competitive moats using Morningstar-style classification **with trend analysis** (widening/stable/narrowing)
- **Apply industry-specific playbooks** for insurance, banking, consumer, media, energy, railroads, and technology
- Calculate intrinsic value using multiple methods (DCF, EPV, Graham Formula, DDM)
- Apply margin of safety analysis and deliver a clear BUY / PASS / SELL recommendation
- **Run sell discipline checks** — 4 explicit criteria for hold/sell decisions
- **Identify value traps** using a 5-type diagnostic framework
- **Assess inflation, goodwill, and derivatives risk** with structured scorecards
- **Detect behavioral biases** in your own analysis with a 5-point self-check
- Generate professional investor-grade research reports (Word, PDF, and interactive HTML)
- Screen for undervalued businesses across **5 markets**: US, Hong Kong, China A-shares, Singapore, and India

## Markets Covered

| Market | Exchange | Filing Source |
|--------|----------|--------------|
| United States | NYSE / NASDAQ | SEC EDGAR (10-K, 10-Q) |
| Hong Kong | HKEx | HKEx News |
| China A-Shares | SSE / SZSE | cninfo.com.cn |
| Singapore | SGX | SGX Announcements |
| India | NSE / BSE | BSE / NSE filings, Screener.in |

## File Structure

```
value-investment-skills/
├── SKILL.md                                    # Main skill definition — 10-step workflow with quick-kill
│                                               #   screener, industry analysis, sell discipline, and
│                                               #   behavioral bias checks
├── assets/
│   └── report-template.md                      # Professional Word/PDF investment report template
│                                               #   (10 sections: exec summary → business overview →
│                                               #   management → moat → financials → valuation →
│                                               #   risk → thesis → portfolio recommendation → conclusion)
├── references/
│   ├── data-sources.md                         # Filing URLs and search strategies for all 5 markets;
│   │                                           #   data quality hierarchy; verdict-moving number rules;
│   │                                           #   red-flag patterns from past analyses (RF-1 to RF-6);
│   │                                           #   data trail audit template; estimation discipline
│   ├── financial-analysis.md                   # 10-year financial summary table; income statement,
│   │                                           #   balance sheet, and cash flow analysis; return metrics
│   │                                           #   (ROE, ROIC, ROA); earnings quality assessment;
│   │                                           #   financial health scorecard (7 categories, /35)
│   ├── frameworks.md                           # Graham defensive checklist + net-net screen;
│   │                                           #   Buffett wonderful-business criteria + owner earnings;
│   │                                           #   Munger mental models + inversion + too-hard pile;
│   │                                           #   Fisher 15-point checklist + scuttlebutt method;
│   │                                           #   combined 4-framework scoring (/10)
│   ├── industry-playbooks.md                   # Sector-specific analysis: insurance (float economics,
│   │                                           #   combined ratio), banking (NIM, NPL, CET1), consumer
│   │                                           #   brands (pricing power, See's Candies case), media
│   │                                           #   (moat destruction case study), energy & utilities,
│   │                                           #   railways, technology (Apple case study); macro
│   │                                           #   sensitivities per sector; industries to avoid;
│   │                                           #   HK/China-specific industry notes
│   ├── inflation-goodwill-derivatives.md       # Economic vs. accounting goodwill (See's Candies
│   │                                           #   paradox); 6-factor inflation scorecard; inflation
│   │                                           #   impact by business type; derivatives risk checklist
│   │                                           #   (7 questions); look-through earnings for holding
│   │                                           #   companies; macro risk overlay framework
│   ├── intrinsic-value.md                      # Valuation methods: Owner Earnings DCF, EPV, Graham
│   │                                           #   Formula, DDM, NCAV; sensitivity tables; reverse
│   │                                           #   DCF; triangulated fair value range
│   ├── moat-analysis.md                        # Competitive moat identification: 5 moat types scored
│   │                                           #   0–3; moat trend assessment (widening/stable/narrowing);
│   │                                           #   franchise vs. commodity test; Fisher scuttlebutt lens;
│   │                                           #   Munger inversion stress test
│   ├── portfolio-construction.md               # Building a concentrated 10–20 stock portfolio;
│   │                                           #   position sizing; geographic & sector diversification;
│   │                                           #   rebalancing rules
│   └── sell-discipline-and-traps.md            # 4 sell criteria (overvaluation, moat destruction,
│                                               #   integrity, better opportunity); 5-type value trap
│                                               #   diagnostic; institutional imperative; 5 behavioral
│                                               #   bias self-checks; monitoring framework with quarterly
│                                               #   review checklist and sell trigger signals
└── web-report/                                 # Interactive HTML web report generation skill
    ├── SKILL.md                                # Skill definition — triggers, workflow, quality
    │                                           #   checklist (25 items); bilingual EN/ZH glossary
    │                                           #   (40+ financial terms); 3 aesthetic themes
    └── references/
        ├── design-system.md                    # Complete CSS design system: 3 themes (Dark Terminal,
        │                                       #   Light Editorial, Dark Luxe); typography (Playfair
        │                                       #   Display + Source Sans 3 + IBM Plex Mono + Noto Sans SC);
        │                                       #   layout grids; card/table/chart components; Chart.js
        │                                       #   global defaults; 7 standard chart types (revenue combo,
        │                                       #   intrinsic value bar, moat radar, margin trend, scenario
        │                                       #   valuation, ROIC/ROE historical, peer comparison);
        │                                       #   animations, print styles, disclaimer footer
        ├── single-stock-report.md              # Full template for single-stock deep dives with 12
        │                                       #   tabbed sections: quick-kill screener, executive summary,
        │                                       #   business overview, management assessment, financial
        │                                       #   scorecard (with qualitative observations), valuation
        │                                       #   analysis, moat analysis (with trend + franchise test),
        │                                       #   industry analysis, risk assessment (value traps, inflation
        │                                       #   scorecard, derivatives, downside scenario), monitoring &
        │                                       #   triggers, investment verdict, sources & data trail
        ├── multi-stock-report.md               # Multi-stock screening/comparison: sortable tables,
        │                                       #   filter controls, expandable rows; 4 chart types
        │                                       #   (P/E vs. ROIC scatter, MoS% ranked bar, allocation
        │                                       #   doughnut, overlay moat radar); cross-market display
        │                                       #   conventions (VIE/SOE/family flags)
        └── portfolio-report.md                 # Portfolio overview: 5-tab layout (overview, holdings,
                                                #   performance, risk & scenarios, watchlist); compound
                                                #   growth projections; scenario impact analysis; per-
                                                #   holding cards with scores and thesis; watchlist with
                                                #   entry targets and triggers; Dark Luxe theme default
```

## Installation

### Option 1 — Ask Claude to install it (easiest)

Open Claude Code and say:

```
Install the value-investing skill from https://github.com/mikezhang09-code/value-investment-skills
```

Claude will run the clone command for you automatically. No terminal needed.

### Option 2 — Clone directly into your Claude skills folder

```bash
git clone https://github.com/mikezhang09-code/value-investment-skills.git \
  ~/.claude/skills/value-investing
```

### Option 3 — Manual copy

1. Clone this repo anywhere:
   ```bash
   git clone https://github.com/mikezhang09-code/value-investment-skills.git
   ```
2. Copy the contents into your Claude skills directory:
   ```bash
   cp -r value-investment-skills/* ~/.claude/skills/value-investing/
   ```

Claude Code auto-discovers skills placed in `~/.claude/skills/`.

## Usage

Once installed, the skill activates automatically when you ask Claude anything investment-related. Examples:

```
"Research BYD as a long-term investment"
"Find undervalued Singapore banks"
"What do you think of Apple stock?"
"Build me a concentrated value portfolio"
"Screen Hong Kong stocks for net-nets"
"Analyze Berkshire Hathaway — full deep dive"
```

Claude will follow a 10-step research process:

0. **Quick-Kill Screener** — 8-question gate (must pass before proceeding)
1. **Identify & Scope** — clarify company, ticker, market, and research depth
2. **Data Collection** — fetch filings from primary sources (SEC, HKEx, SGX, etc.)
3. **Financial Analysis** — 10-year quantitative deep dive
4. **Moat Assessment** — competitive advantage quality, durability, and **trend** (widening/stable/narrowing)
5. **Industry Analysis** — sector-specific metrics and macro sensitivities
6. **Intrinsic Valuation** — multiple methods triangulated into a fair value range
7. **Margin of Safety** — compare current price to intrinsic value
8. **Risk & Sell Check** — value trap diagnostic, inflation scorecard, sell criteria
9. **Investment Decision** — BUY / ACCUMULATE / MONITOR / PASS / SELL / AVOID
10. **Report Generation** — professional report + optional Excel model

## Web Report Skill

The `web-report/` subdirectory contains an interactive HTML web report generation skill — the visual counterpart to traditional Word/PDF reports. It produces single-file, self-contained HTML pages with:

- **Chart.js visualizations** — revenue/profit combos, margin trends, moat radar, intrinsic value bars, sensitivity tables, scenario analysis, peer comparisons (7+ charts per report)
- **Three design themes** — Dark Terminal (default), Light Editorial, Dark Luxe — with editorial-grade typography (Playfair Display + Source Sans 3 + IBM Plex Mono)
- **Bilingual English/Chinese** labeling throughout, with full financial glossary (40+ terms)
- **Three report types** — single-stock deep dive, multi-stock comparison/screening, portfolio overview
- **Interactive features** — tabbed navigation, sortable tables, filter controls, expandable rows, smooth animations
- **Responsive & print-friendly** — works from 320px mobile to 1440px desktop, with print stylesheet
- **Business & management assessment** — plain-language business overview, leadership table, ownership alignment KPIs, capital allocation scorecard, red flags check
- **Risk framework** — downside scenario card, sell criteria check, value trap diagnostic, inflation scorecard, derivatives exposure assessment, monitoring triggers

### Trigger phrases

```
"Create a web report for [stock]"
"Convert this analysis to an HTML page"
"Build an interactive dashboard for [stock]"
"Generate an HTML report"
```

## Investment Philosophy

This skill is grounded in time-tested value investing principles:

- **Never speculate. Never fabricate data.** Every number must come from a verifiable source.
- **Business quality first, price second.** A wonderful company at a fair price beats a fair company at a wonderful price.
- **Think long-term.** The target holding period is 5–10+ years.
- **Be conservative.** Use lower growth rates and higher discount rates when uncertain.
- **Cite everything.** Every key claim needs a source (filing name, page, date).

## Keeping Up to Date

```bash
cd ~/.claude/skills/value-investing
git pull
```

## Contributing

Pull requests are welcome — especially improvements to reference files (new data sources, updated frameworks, additional markets).

## License

MIT
