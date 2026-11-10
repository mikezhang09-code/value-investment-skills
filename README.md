# Value Investment Skills

A Claude Code skill for deep fundamental research and value investing analysis, inspired by the principles of Benjamin Graham, Warren Buffett, Charlie Munger, and Philip Fisher.

## What This Skill Does

When installed, this skill gives Claude the ability to:

- Research any publicly listed company as a seasoned fundamental analyst, across **5 markets**: US, Hong Kong, China A-shares, Singapore, and India
- **Route by scope** — full deep dive, quick thesis, thesis refresh, earnings reaction, or comparison — each running a defined set of steps, with the data gates never skipped
- **Quick-Kill screen** stocks with an 8-question pass/fail gate (integrity is an automatic veto) before deep analysis
- **Run every number through a data gate** — each verdict-moving figure is recorded in an inputs file with its document, page and the line as printed, then checked by `scripts/validate_inputs.py` (11 checks: provenance with quote matching, units, share count, live price, net cash, statement articulation, owner-earnings tie, history, matched windows, FX, stake containment) and read a second time independently
- **Analyse on what is in hand, and say so plainly** — the gate returns VERIFIED, QUALIFIED (gaps: verdict marked provisional, conviction capped at 6/10, +10 points margin of safety) or UNRESOLVED (a figure disagrees with its cross-check: value shown under each reading, no verdict). The analysis is never withheld
- **Take history from structured sources first** (SEC company facts, the annual report's multi-year summary), with the latest three years tied to the filing
- Perform 10-year financial deep dives (revenue, margins, ROE, ROIC, FCF, etc.) and keep a **Data gaps** list that becomes the next refresh's fetch list
- **Run an Earnings Quality Gate** — 8 distortion classes (one-offs, dilution, investment income, SBC and net buybacks, related-party transactions, off-balance-sheet items, acquired growth) normalized before valuation
- **Bridge any surprising quarter** from operating profit through one-offs, non-operating items and tax, so only the operational part moves the thesis
- Assess competitive moats **with trend analysis** on an anchored /30 scorecard, and test technology disruption **per segment** with the Deflation Sign Test
- **Apply industry playbooks** — full sector overrides for financials (insurance and banking), plus guidance for consumer, media, energy, railroads and technology
- **Value on one owner-earnings definition** — operating profit after normal tax + D&A − maintenance capex, pre-interest, stock compensation never added back — so net cash and debt are counted exactly once
- **Charge growth for the capital it needs** (g ÷ return on new capital, with a moat-set terminal return), and use a **mid-cycle base** for cyclicals
- **State one fair value** from the primary method for the business type — for non-financials the lower of the Base and probability-weighted DCF; residual income with an explicit fade for banks and insurers (`scripts/residual_income.py`) — with other methods as cross-checks, never averaged in
- **Apply Output Plausibility Checks** ("too good to be true", peer multiples, reverse DCF, analyst consensus divergence)
- Deliver a clear **BUY / ACCUMULATE / WATCHLIST / HOLD / PASS / AVOID** verdict with conviction, margin of safety, and tripwires that state both an operational and a valuation condition
- **Run sell discipline and value-trap checks** — 4 sell criteria, a 5-type value-trap diagnostic, inflation/goodwill/derivatives scorecards, and a behavioral-bias self-check
- **Learn from its own mistakes** — `process-lessons.md` records 16 error classes and 27 checks, each derived from a real analysis error
- Produce **three deliverables** per analysis — a Markdown research report, an interactive HTML dashboard, and a bilingual EN/简体中文 executive summary — each opening with the data-status box, all derived from one canonical figure block and checked by a final Deliverable Gate

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
│                                               #   behavioral bias checks; Step 2.5 data gate (three
│                                               #   outcomes), Step 6 one fair value per business type,
│                                               #   Step 6.5 Plausibility Checks
├── assets/
│   ├── inputs-template.json                    # A passing synthetic inputs file to copy for a new name
│   └── report-template.md                      # Spec for the THREE deliverables: data-status box, then a
│                                               #   10-section Markdown report (exec summary → business →
│                                               #   management → moat → financials + profit bridge →
│                                               #   valuation: drivers, owner earnings, scenarios, fair
│                                               #   value + cross-checks, dated falsifiable forecasts →
│                                               #   risk → thesis → portfolio → conclusion, plus generated
│                                               #   data trail and data gaps); HTML dashboard tabs;
│                                               #   16-section bilingual EN/中文 summary; scope variations
├── references/
│   ├── data-inputs.md                          # The data gate: inputs-file layout, checks D1–D11, GAP vs
│   │                                           #   CONFLICT, the three outcomes and what each does to the
│   │                                           #   report, tolerance ladder, source-tier ladder,
│   │                                           #   independent second read
│   ├── data-sources.md                         # Structured sources first (SEC company facts, HKEXnews
│   │                                           #   lookups, multi-year summaries); filing URLs for all 5
│   │                                           #   markets; one source-tier ladder; verdict-moving number
│   │                                           #   rules; red-flag patterns (RF-1 to RF-10); share-class
│   │                                           #   warnings and 4 reconciliation anchors; live price
│   │                                           #   verification gate (P1–P5)
│   ├── discount-rate-draft_2026-10-13.md       # Validation record for the Step 3b business-risk rate
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
│   ├── intrinsic-value.md                      # Valuation: operating owner earnings (one definition,
│   │                                           #   mid-cycle for cyclicals); currency discount-rate table
│   │                                           #   + business-risk add-on; growth charged at g / RONIC;
│   │                                           #   bridge to equity; scenarios; one fair value per
│   │                                           #   business type with cross-checks; EPV, Graham, DDM,
│   │                                           #   NCAV, SOTP; financials fade rule; 4 plausibility checks
│   ├── moat-analysis.md                        # Competitive moat identification: 5 moat types; anchored
│   │                                           #   /30 scorecard (sets the discount-rate add-on and the
│   │                                           #   terminal return); moat trend (widening/stable/narrowing);
│   │                                           #   franchise vs. commodity test; Fisher scuttlebutt lens;
│   │                                           #   Munger inversion stress test
│   ├── portfolio-construction.md               # Building a concentrated 10–20 stock portfolio;
│   │                                           #   position sizing; geographic & sector diversification;
│   │                                           #   rebalancing rules
│   ├── process-lessons.md                      # Self-improvement reference for analytical errors:
│   │                                           #   16 error classes (mechanical / interpretive / omission)
│   │                                           #   and 27 checks, each derived from a real case
│   │                                           #   (BYD, Tencent, China Taiping, GWM, Intuit, ...)
│   ├── quarterly-profit-bridge.md              # Operating vs tax / one-off / non-operating / seasonal
│   │                                           #   decomposition of a quarter's profit change
│   ├── sell-discipline-and-traps.md            # 4 sell criteria (overvaluation, moat destruction,
│                                               #   integrity, better opportunity); 5-type value trap
│                                               #   diagnostic; institutional imperative; 5 behavioral
│                                               #   bias self-checks; monitoring framework with quarterly
│                                               #   review checklist and sell trigger signals; error
│                                               #   recognition protocol and speed guidelines
│   └── working-conventions.md                  # Stage 0 read list, fetch budgets by document type,
│                                               #   thesis-refresh structure, presentation order, Stage 6
│                                               #   command-center procedure, final chat summary
├── scripts/
│   ├── validate_inputs.py                      # Data gate → VERIFIED / QUALIFIED / UNRESOLVED (the analysis
│   │                                           #   is always produced, labelled by what is missing or
│   │                                           #   disagrees): checks D1–D11 on inputs_<ticker>_<date>.json
│   │                                           #   (provenance, units, share count, price, net cash,
│   │                                           #   statement articulation, owner-earnings tie, history,
│   │                                           #   windows, FX, stakes); --status-box prints the box that
│   │                                           #   opens every deliverable, --trail the Data Trail; also
│   │                                           #   reports measured ROIC (all capital and organic)
│   ├── scenario_dcf.py                         # Scenario DCF on operating (pre-interest) owner earnings,
│   │                                           #   growth charged at g / RONIC, one fair_value; weighted
│   │                                           #   value, reverse DCF, implied return, terminal-value
│   │                                           #   share, per-share bridge, sensitivity grid; takes its
│   │                                           #   inputs from the validation and stamps the data status
│   ├── residual_income.py                      # Banks / insurers: residual income with explicit fade,
│   │                                           #   fade ladder, justified-P/B validity test
│   └── tests/                                  # python3 -m unittest discover -s scripts/tests
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

Claude Code auto-discovers skills placed in `~/.claude/skills/`. The scripts need only Python 3
(standard library). Run the tests with:

```bash
python3 -m unittest discover -s scripts/tests
```

The SEC filing archive (`www.sec.gov/Archives/...`) rejects downloads that do not declare a contact
address in the User-Agent header; Claude asks you which address to use before fetching from it. The
`data.sec.gov` structured-data API works without one.

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
2. **Data Collection** — structured sources first for the history, then the filings; every number recorded with its page and quoted line in `inputs_<ticker>_<date>.json`
2.5. **Data Gate** — `validate_inputs.py` checks the inputs file and an independent second read confirms each verdict-moving number. Outcome: **VERIFIED**, **QUALIFIED** (gaps — the analysis goes ahead, labelled) or **UNRESOLVED** (a conflict — the analysis goes ahead, with no verdict)
3. **Financial Analysis** — 10-year quantitative deep dive
3.5. **Earnings Quality Gate** — 8-distortion check, plus a quarterly profit bridge when a quarter's profit diverges from revenue or surprises consensus
4. **Moat Assessment** — anchored /30 scorecard, durability and **trend** (widening/stable/narrowing); per-segment disruption scenarios where technology threatens a revenue line
5. **Industry Analysis** — sector-specific metrics and macro sensitivities
6. **Intrinsic Valuation** — operating owner earnings, growth charged for reinvestment, one fair value from the primary method for the business type (`scripts/scenario_dcf.py`, or `scripts/residual_income.py` for financials); other methods as cross-checks
6.5. **Output Plausibility Checks** — four sanity checks ("Too Good to Be True", peer multiples, reverse DCF, analyst consensus divergence) before publishing
7. **Margin of Safety** — current price against the fair value (25% required; 40%+ for turnarounds; +10 points when the data is QUALIFIED)
8. **Risk & Sell Check** — value trap diagnostic, inflation scorecard, sell criteria, and behavioral bias/analytical self-checks
9. **Investment Decision** — BUY / ACCUMULATE / WATCHLIST / HOLD / PASS / AVOID (marked PROVISIONAL on QUALIFIED data; no verdict on UNRESOLVED data)
10. **Report Generation** — three deliverables, each opening with the data-status box: Markdown report, HTML dashboard, bilingual EN/中文 summary (+ optional Excel model)
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

- **Never speculate. Never fabricate data.** Every number must come from a verifiable source, recorded with the line it was read from.
- **Be frank about what is not known.** An analysis built on incomplete data is published with its gaps stated and its verdict qualified, never presented as verified.
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
