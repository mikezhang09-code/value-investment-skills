# Value Investment Skills

A Claude Code skill for deep fundamental research and value investing analysis, inspired by the principles of Benjamin Graham, Warren Buffett, Charlie Munger, and Philip Fisher.

## What This Skill Does

When installed, this skill gives Claude the ability to:

- Research any publicly listed company as a seasoned fundamental analyst
- Perform 10-year financial deep dives (revenue, margins, ROE, ROIC, FCF, etc.)
- Assess competitive moats using Morningstar-style classification
- Calculate intrinsic value using multiple methods (DCF, EPV, Graham Formula, DDM)
- Apply margin of safety analysis and deliver a clear BUY / PASS recommendation
- Generate professional investor-grade research reports
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
├── SKILL.md                          # Main skill definition (8-step workflow)
├── assets/
│   └── report-template.md            # Professional investment report template
├── references/
│   ├── data-sources.md               # Where to find filings for each market
│   ├── financial-analysis.md         # Ratio definitions and scoring framework
│   ├── frameworks.md                 # Graham / Buffett / Munger / Fisher checklists
│   ├── intrinsic-value.md            # Valuation methods (DCF, EPV, Graham Formula)
│   ├── moat-analysis.md              # Competitive moat identification framework
│   └── portfolio-construction.md     # Building a concentrated 10–20 stock portfolio
└── web-report/                       # Interactive HTML web report generation skill
    ├── SKILL.md                      # Skill definition — triggers, workflow, checklist
    └── references/
        ├── design-system.md          # CSS variables, typography, Chart.js, components
        ├── single-stock-report.md    # Full template for single-stock deep dives
        ├── multi-stock-report.md     # Sortable tables, filters, comparison charts
        └── portfolio-report.md       # Portfolio overview with holdings & scenarios
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

Claude will follow an 8-step research process:

1. **Identify & Scope** — clarify company, ticker, market, and research depth
2. **Data Collection** — fetch filings from primary sources (SEC, HKEx, SGX, etc.)
3. **Financial Analysis** — 10-year quantitative deep dive
4. **Moat Assessment** — competitive advantage quality and durability
5. **Intrinsic Valuation** — multiple methods triangulated into a fair value range
6. **Margin of Safety** — compare current price to intrinsic value
7. **Investment Decision** — BUY / ACCUMULATE / MONITOR / PASS / AVOID
8. **Report Generation** — professional report + optional Excel model

## Web Report Skill (New)

The `web-report/` subdirectory contains an interactive HTML web report generation skill — the visual counterpart to traditional Word/PDF reports. It produces single-file, self-contained HTML pages with:

- **Chart.js visualizations** — revenue/profit combos, margin trends, moat radar, intrinsic value bars, sensitivity tables, scenario analysis, peer comparisons (7+ charts per report)
- **Three design themes** — Dark Terminal (default), Light Editorial, Dark Luxe — with editorial-grade typography (Playfair Display + Source Sans 3 + IBM Plex Mono)
- **Bilingual English/Chinese** labeling throughout, with full financial glossary
- **Three report types** — single-stock deep dive, multi-stock comparison/screening, portfolio overview
- **Interactive features** — tabbed navigation, sortable tables, filter controls, expandable rows, smooth animations
- **Responsive & print-friendly** — works from 320px mobile to 1440px desktop, with print stylesheet

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
