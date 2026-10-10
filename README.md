# Value Investment Skills

A Claude Code skill for deep fundamental research and value investing analysis, inspired by the principles of Benjamin Graham, Warren Buffett, Charlie Munger, and Philip Fisher.

## What This Skill Does

When installed, this skill gives Claude the ability to:

- Research any publicly listed company as a seasoned fundamental analyst, across **5 markets**: US, Hong Kong, China A-shares, Singapore, and India
- **Route by scope** — full deep dive, quick thesis, thesis refresh, earnings reaction, or comparison — each running a defined set of steps, with the data gates never skipped
- **Quick-Kill screen** stocks with an 8-question pass/fail gate (integrity is an automatic veto) before deep analysis
- **Verify the live price** (timestamp, freshness, 52-week range vs prices on file, move check, two sources) before it enters any calculation
- **Enforce a 4-Anchor Reconciliation Gate** (market cap, EPS back-check, per-share metrics, share-class structure) before any per-share valuation — catches H+A float underreporting, ADR ratio confusion, and perpetual/AT1 capital miscounted as equity
- Perform 10-year financial deep dives (revenue, margins, ROE, ROIC, FCF, etc.) and record a **Data gaps** list — an empty debt, share-count or tax field blocks valuation
- **Run an Earnings Quality Gate** — 8 distortion classes (one-offs, dilution, investment income, SBC and net buybacks, related-party transactions, off-balance-sheet items, acquired growth) normalized before valuation
- **Bridge any surprising quarter** from operating profit through one-offs, non-operating items and tax, so only the operational part moves the thesis
- Assess competitive moats **with trend analysis** (widening/stable/narrowing), and test technology disruption **per segment** with the Deflation Sign Test
- **Apply industry playbooks** — full sector overrides for financials (insurance and banking), plus guidance for consumer, media, energy, railroads and technology
- Calculate intrinsic value with multiple methods (owner-earnings DCF, EPV, Graham Formula, DDM, NCAV, SOTP) and **probability-weighted disruption scenarios** via a reproducible script (`scripts/scenario_dcf.py`)
- **Apply Output Plausibility Checks** ("too good to be true", peer multiples, reverse DCF, analyst consensus divergence)
- Deliver a clear **BUY / ACCUMULATE / MONITOR / PASS / SELL / AVOID** verdict with conviction, margin of safety and tripwires that state both an operational and a valuation condition
- **Run sell discipline and value-trap checks** — 4 sell criteria, a 5-type value-trap diagnostic, inflation/goodwill/derivatives scorecards, and a behavioral-bias self-check
- **Learn from its own mistakes** — `process-lessons.md` records 15 error classes and 20 sanity checks, each derived from a real analysis error
- Produce **three deliverables** per analysis — a Markdown research report, an interactive HTML dashboard, and a bilingual EN/简体中文 executive summary — all derived from one canonical figure block and checked by a final Deliverable Gate

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
│                                               #   behavioral bias checks; includes mandatory Step 2.5
│                                               #   Reconciliation Gate and Step 6.5 Plausibility Checks
├── assets/
│   └── report-template.md                      # Spec for the THREE deliverables: 10-section Markdown
│                                               #   report (exec summary → business → management → moat →
│                                               #   financials + profit bridge → valuation + scenarios +
│                                               #   plausibility → risk → thesis → portfolio → conclusion,
│                                               #   plus data trail and data gaps); HTML dashboard tabs;
│                                               #   16-section bilingual EN/中文 summary; scope variations
├── references/
│   ├── data-sources.md                         # Filing URLs and search strategies for all 5 markets;
│   │                                           #   data quality hierarchy; verdict-moving number rules;
│   │                                           #   red-flag patterns from past analyses (RF-1 to RF-8);
│   │                                           #   data trail + data gaps; estimation discipline;
│   │                                           #   share-class warnings and 4 reconciliation anchors;
│   │                                           #   live price verification gate (P1–P5)
│   ├── disruption-scenarios.md                 # Per-segment Deflation Sign Test → four probability-
│   │                                           #   weighted scenarios (Disruption/Bear/Base/Bull) with
│   │                                           #   evidence rules and dual-condition tripwires
│   ├── earnings-quality-and-distortions.md     # Step 3.5 gate: 8 distortion classes (one-offs, dilution,
│   │                                           #   investment income, SBC + net buybacks, RPTs, off-BS,
│   │                                           #   acquired growth); normalized-earnings bridge
│   ├── financial-analysis.md                   # 10-year financial summary table; income statement,
│   │                                           #   balance sheet, and cash flow analysis; return metrics
│   │                                           #   (ROE, ROIC, ROA); earnings quality assessment;
│   │                                           #   financial health scorecard (7 categories, /35)
│   ├── frameworks.md                           # Graham defensive checklist + net-net screen;
│   │                                           #   Buffett wonderful-business criteria + owner earnings;
│   │                                           #   Munger mental models + inversion + too-hard pile;
│   │                                           #   Fisher 15-point checklist + scuttlebutt method;
│   │                                           #   combined 4-framework scoring (/10)
│   ├── industry-playbooks.md                   # Sector-specific analysis; §F financials overrides the
│   │                                           #   generic workflow (metrics, valuation, distortion
│   │                                           #   classes); insurance (float economics,
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
│   │                                           #   DCF; triangulated fair value range; pre-valuation
│   │                                           #   anchoring and 4 output plausibility checks
│   ├── moat-analysis.md                        # Competitive moat identification: 5 moat types scored
│   │                                           #   0–3; moat trend assessment (widening/stable/narrowing);
│   │                                           #   franchise vs. commodity test; Fisher scuttlebutt lens;
│   │                                           #   Munger inversion stress test
│   ├── portfolio-construction.md               # Building a concentrated 10–20 stock portfolio;
│   │                                           #   position sizing; geographic & sector diversification;
│   │                                           #   rebalancing rules
│   ├── process-lessons.md                      # Self-improvement reference for analytical errors:
│   │                                           #   15 error classes (mechanical / interpretive / omission)
│   │                                           #   and 20 sanity checks, each derived from a real case
│   │                                           #   (BYD, Tencent, China Taiping, GWM, Intuit, ...)
│   ├── quarterly-profit-bridge.md              # Operating vs tax / one-off / non-operating / seasonal
│   │                                           #   decomposition of a quarter's profit change
│   └── sell-discipline-and-traps.md            # 4 sell criteria (overvaluation, moat destruction,
│                                               #   integrity, better opportunity); 5-type value trap
│                                               #   diagnostic; institutional imperative; 5 behavioral
│                                               #   bias self-checks; monitoring framework with quarterly
│                                               #   review checklist and sell trigger signals; error
│                                               #   recognition protocol and speed guidelines
├── scripts/
│   └── scenario_dcf.py                         # Reproducible scenario owner-earnings DCF: weighted IV,
│                                               #   reverse DCF, EPV, sensitivity grid; stops on missing
│                                               #   net debt, warns on an undefended discount rate
├── *_bilingual.md, value_investing_skill_*.md  # EN/中文 records of rule amendments and sweeps, and a
│                                               #   Mermaid architecture diagram (not loaded by the skill)
└── web-report/                                 # Interactive HTML web report generation skill
    ├── SKILL.md                                # Skill definition — triggers, workflow, quality
    │                                           #   checklist; bilingual EN/ZH glossary
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

### Option 4 — Symlink (for contributors editing the skill)

Keep the repo wherever you develop it and link it in, so every saved change takes effect immediately:

```bash
git clone https://github.com/mikezhang09-code/value-investment-skills.git ~/Documents/GitHub/value-investment-skills
ln -s ~/Documents/GitHub/value-investment-skills ~/.claude/skills/value-investing
```

Claude reads whatever is checked out, so keep `main` checked out when you are not mid-edit.

Claude Code auto-discovers skills placed in `~/.claude/skills/`. The scenario script needs only
Python 3 (standard library).

## Usage

Once installed, the skill activates automatically when you ask Claude anything investment-related. Examples:

```
"Research BYD as a long-term investment"
"Find undervalued Singapore banks"
"What do you think of Apple stock?"
"Build me a concentrated value portfolio"
"Screen Hong Kong stocks for net-nets"
"Analyze Berkshire Hathaway — full deep dive"
"Is Tencent still worth holding after this quarter?"   # thesis refresh
"Why did Intuit's profit fall in Q4?"                  # earnings reaction
"Compare ICICI Bank and HDFC Bank"                     # comparison
```

Claude will follow a 10-step research process:

0. **Quick-Kill Screener** — 8-question gate (must pass before proceeding)
1. **Identify & Scope** — clarify company, ticker, market, and research depth
2. **Data Collection** — fetch filings from primary sources (SEC, HKEx, SGX, etc.)
2.5. **Reconciliation Gate** — mandatory 4-anchor check (market cap, EPS back-check, per-share metrics, share-class structure) to prevent calculation and scale errors
3. **Financial Analysis** — 10-year quantitative deep dive
3.5. **Earnings Quality Gate** — 8-distortion check, plus a quarterly profit bridge when a quarter's profit diverges from revenue or surprises consensus
4. **Moat Assessment** — competitive advantage quality, durability, and **trend** (widening/stable/narrowing); per-segment disruption scenarios where technology threatens a revenue line
5. **Industry Analysis** — sector-specific metrics and macro sensitivities
6. **Intrinsic Valuation** — multiple methods triangulated into a fair value range; probability-weighted scenarios via `scripts/scenario_dcf.py`
6.5. **Output Plausibility Checks** — four sanity checks ("Too Good to Be True", peer multiples, reverse DCF, analyst consensus divergence) before publishing
7. **Margin of Safety** — compare current price to intrinsic value
8. **Risk & Sell Check** — value trap diagnostic, inflation scorecard, sell criteria, and behavioral bias/analytical self-checks
9. **Investment Decision** — BUY / ACCUMULATE / MONITOR / PASS / SELL / AVOID
10. **Report Generation** — three deliverables: Markdown report, HTML dashboard, bilingual EN/中文 summary (+ optional Excel model)
10.5. **Deliverable Gate** — every file in the scope's manifest exists and the canonical figures match across them

Reduced scopes (quick thesis, thesis refresh, earnings reaction, comparison) run a defined subset of these steps — see the scope routing table in `SKILL.md`. The live-price gate and Steps 2.5, 6.5 and 10.5 run at every scope.

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
cd ~/.claude/skills/value-investing   # with Option 4, this is your repo; pulling updates both
git pull
```

## Contributing

Pull requests are welcome — especially improvements to reference files (new data sources, updated frameworks, additional markets).

## License

MIT
