# Investment Research Report Template

Use this template to produce every investment report. Fill in every section — if data is unavailable, state so explicitly rather than omitting the section.

---

## ⚠️ Deliverables at a glance — THREE per analysis, not two

| # | Deliverable | File | Language | Job it does | Reader |
|---|---|---|---|---|---|
| 1 | **Markdown report** | `report_<ticker>_<YYYY-MM-DD>.md` | **English**, bilingual headers | Audit trail + reasoning record. Every number traceable. | The analyst — you now, or a future session doing a refresh |
| 2 | **HTML dashboard** | `report_<ticker>_<YYYY-MM-DD>.html` | **English**, bilingual headers | Browsing surface. Charts, tabs, interactivity. | Anyone exploring the analysis visually |
| 3 | **Bilingual summary** | `summary_<ticker>_<YYYY-MM-DD>_EN-CN.md` | **Full EN + 简体中文**, interleaved | Communication + fast reload of the thesis. | Anyone being sent the conclusion; you, six months later |

Plus **Stage 6**: `command-center.md` and `command-center.html` are *revised in place* — same filenames forever, one copy in existence, written back to Project Knowledge. They are not per-analysis artifacts and do not accumulate.

**Delivery convention:** deliver deliverables 1–3 plus `command-center.html` into the conversation. Write both command-center files to Project Knowledge. Do **not** deliver `command-center.md` into the chat — it is a ~280KB record meant to be read by the next session, not by a human in a chat panel.

> **Why three and not a single bilingual report.** Language follows the document's *job*, not applied uniformly. The full report is an audit document — nobody reads a reconciliation table bilingually, and translating it would double the length of exactly the sections where length hurts most and helps least. Worse, a bilingual full report doubles every number's surface area *inside one file*, which is the Xtep-#14 failure mode by construction. The summary is short enough that interleaving stays readable, and it is the artifact that actually gets forwarded and re-read.

---

```
═══════════════════════════════════════════════════════════════
INVESTMENT RESEARCH REPORT
[COMPANY NAME] ([TICKER] : [EXCHANGE])
Date: [DATE]   Analyst: Value Investing Research
═══════════════════════════════════════════════════════════════

RECOMMENDATION:  [BUY / ACCUMULATE / WATCHLIST / HOLD / PASS / AVOID]
Current Price:   [CURRENCY + PRICE]
Intrinsic Value: [CURRENCY + RANGE] (Conservative: X | Base: X | Optimistic: X)
Margin of Safety: [X%] (at base case intrinsic value)
Target Horizon:  5–10 years
Risk Rating:     [Low / Medium / High]
Conviction:      [High / Medium / Low]
```

---

## Section 1: Executive Summary

*2–4 sentences maximum. State the investment case clearly.*

[COMPANY] is a [brief business description] with a [wide/narrow] competitive moat based on [moat type]. The business has compounded earnings at [X%] over 10 years with consistently high returns on capital (average ROE: [X%], ROIC: [X%]). At current prices of [PRICE], the stock offers a [X%] margin of safety to our base-case intrinsic value of [VALUE]. We rate the stock [RECOMMENDATION] for long-term value investors.

**Key investment merits (bullet form):**

- [Merit 1]
- [Merit 2]
- [Merit 3]

**Key risks:**

- [Risk 1]
- [Risk 2]

---

## Section 2: Business Overview

### What Does the Company Do?
[2–3 paragraphs describing the business in plain language. What does it sell? To whom? In which markets? How does it make money?]

### Revenue Breakdown
| Segment / Geography | Revenue ($M) | % of Total | Growth YoY |
|--------------------|-------------|-----------|-----------|
| [Segment 1] | | | |
| [Segment 2] | | | |
| [Geography 1] | | | |
| **Total** | | 100% | |

### Business Model Characteristics
- Revenue type: [Recurring/Transactional/Project/Mixed] — [% recurring]
- Customer concentration: [Top customer = X% of revenue?]
- Pricing model: [Premium/Value/Variable]
- Capital intensity: [Asset-light/Moderate/Capital-intensive]

### Industry Context
[1–2 paragraphs on the industry: size, growth rate, competitive dynamics, secular trends. Is the industry growing, stable, or in structural decline?]

---

## Section 3: Management Assessment

### Leadership
| Name | Role | Tenure | Background |
|------|------|--------|-----------|
| [CEO] | CEO | X years | [brief background] |
| [CFO] | CFO | X years | [brief background] |
| [Founder/Chairman if relevant] | | | |

### Ownership & Alignment
- Insider ownership: [X%] — [High/Moderate/Low]
- CEO compensation: $[X]M total; [X%] performance-based
- Buyback history: [$X]M repurchased over last 5 years at avg price of $[X] vs. current $[X]
- Dividend history: [X years consecutive] dividends; current yield [X%]

### Capital Allocation Scorecard (last 5 years)
| Use of Capital | Amount | Quality Assessment |
|---------------|--------|-------------------|
| Organic reinvestment | | [Excellent/Good/Poor — ROIC of projects?] |
| Acquisitions | | [Accretive/Dilutive? Price paid fair?] |
| Dividends | | [Sustainable? Growing?] |
| Buybacks | | [At undervalued prices?] |
| Debt management | | |

### Red Flags Check
- [ ] No material related-party transactions of concern
- [ ] Compensation reasonable and aligned
- [ ] Communication with shareholders is transparent
- [ ] No significant investigations or regulatory actions
- Notes: [any concerns]

---

## Section 4: Competitive Moat Analysis

### Moat Summary
**Overall Moat Rating**: [Wide / Narrow / None]
**Durability**: [High (20+ years) / Medium (10–20 years) / Low (<10 years)]

### Moat Type(s) and Evidence

**[Moat Type 1]:** [e.g., Brand/Switching Costs/Network Effects/Cost Advantage/Efficient Scale]
[2–3 sentences explaining the moat and the evidence for it. What makes this durable?]

**[Moat Type 2 if applicable]:**
[Same structure]

### Competitive Position
| Competitor | Market Share | Key Differentiation | Threat Level |
|-----------|-------------|--------------------|-----------|
| [Company] (subject) | [X%] | | |
| [Competitor 1] | [X%] | | Low/Med/High |
| [Competitor 2] | [X%] | | |

### Moat Stress Test (Munger Inversion)
*What would have to happen for this moat to be destroyed within 10 years?*

- Scenario 1: [e.g., "A well-funded competitor enters with superior technology..."]
- Scenario 2: [e.g., "Regulatory change eliminates the pricing advantage..."]
- Assessment: [Why these scenarios are/aren't likely]

---

## Section 5: Financial Analysis

### 10-Year Financial Summary

| Metric | FY15 | FY16 | FY17 | FY18 | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 | 10yr CAGR |
|--------|------|------|------|------|------|------|------|------|------|------|-----------|
| Revenue ($M) | | | | | | | | | | | |
| Gross Margin % | | | | | | | | | | | |
| Operating Margin % | | | | | | | | | | | |
| Net Margin % | | | | | | | | | | | |
| EPS (diluted) | | | | | | | | | | | |
| FCF ($M) | | | | | | | | | | | |
| ROE % | | | | | | | | | | | |
| ROIC % | | | | | | | | | | | |
| Debt/Equity | | | | | | | | | | | |
| Book Value/Share | | | | | | | | | | | |
| Shares Out. (M) | | | | | | | | | | | |

*Sources: [List sources — e.g., "SEC 10-K filings 2015–2024, Macrotrends.net"]*

### Key Financial Observations

**Strengths:**

- [Observation 1: e.g., "Gross margins have expanded from 40% to 55% over the decade, evidence of growing pricing power"]
- [Observation 2]
- [Observation 3]

**Concerns:**

- [Concern 1: e.g., "Debt/Equity has risen from 0.2x to 0.8x due to acquisitions — worth monitoring"]
- [Concern 2]

### Earnings Quality Assessment
- FCF/Net Income ratio (10yr avg): [X%] — [Excellent >90% / Good 70-90% / Concerning <70%]
- Revenue recognition policy: [Conservative / Aggressive / Normal]
- Non-recurring charges pattern: [e.g., "Company has taken restructuring charges in 3 of last 5 years — treat as recurring"]
- Earnings quality rating: [High / Medium / Low]

### Quarterly Profit Bridge *(required when the bridge was triggered — see `references/quarterly-profit-bridge.md`)*

| Driver | Δ NI ($M) | O / N | Recurring? |
|---|---|---|---|
| Organic operating profit | | O | |
| One-offs this quarter / prior-year quarter | | N | |
| Non-operating (associates, investment marks, FX, interest) | | N | |
| Tax (rate change / discrete item) | | N | |
| **Reported Δ NI** | | | |

Conclusion: "Of the [X]-point gap, [Y] points are non-recurring; [Z] points are operational, from [segment]."

---

## Section 6: Intrinsic Value Calculation

### Method 1: Owner Earnings DCF

**Normalized Owner Earnings (TTM):** $[X]M = $[X] per share

*Calculation:*
- Net Income: $[X]M
- Add: D&A: $[X]M
- Add: Other non-cash: $[X]M
- Less: Estimated Maintenance CapEx: $[X]M
- **Owner Earnings: $[X]M**

**Growth Assumptions:**
- Years 1–5: [X%] (based on [justification])
- Years 6–10: [X%] (haircut from recent growth)
- Terminal growth: [X%]

**Discount Rate:** [X%] ([justification: e.g., "high-quality, predictable business"])

| Year | Owner Earnings | Discount Factor | PV |
|------|---------------|-----------------|-----|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |
| 10 | | | |
| Terminal Value | | | |
| **Enterprise Value** | | | |
| Less: Net Debt | | | |
| **Equity Value** | | | |
| Shares Outstanding | | | |
| **Intrinsic Value / Share** | | | |

### Method 2: Earnings Power Value (EPV)

- Normalized EBIT (5-yr avg): $[X]M
- Tax Rate: [X%]
- After-tax operating earnings: $[X]M
- Discount rate: [X%]
- EPV (enterprise): $[X]M
- Less: Net Debt: $[X]M
- **Equity EPV: $[X]M = $[X] per share**

### Valuation Summary

| Method | Intrinsic Value/Share | Premium/Discount to Market |
|--------|----------------------|---------------------------|
| Owner Earnings DCF | $[X] | [+X% / -X%] |
| EPV | $[X] | [+X% / -X%] |
| Graham Formula | $[X] | [+X% / -X%] |
| **Weighted Average** | **$[X]** | **[+X% / -X%]** |

**Intrinsic Value Range:**
- Conservative: $[X] — [Margin of Safety: X%]
- Base Case: $[X] — [Margin of Safety: X%]
- Optimistic: $[X] — [Margin of Safety: X%]

**Current Price: $[X]**

### Disruption Scenarios *(required when Step 4 flagged a revenue-line threat — see `references/disruption-scenarios.md`)*

| Scenario | Probability | g1 / g2 / tg | Value/share | MoS | Tripwire (operational AND valuation) |
|---|---|---|---|---|---|
| Disruption | | | | | |
| Bear | | | | | |
| Base | | | | | |
| Bull | | | | | |
| **Weighted** | 100% | | | | |

Reverse-DCF implied growth: [X%] · EPV floor: $[X] · Source: `scenario_dcf.py` output, [date]

### Plausibility Tests (Step 6.5)

| Test | Result | Pass / Flag |
|---|---|---|
| Too good to be true | | |
| Peer multiples | | |
| Reverse DCF | | |
| Consensus divergence (consensus dated [ ]) | | |

---

## Section 7: Risk Factors

### Key Risks

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| [Risk 1] | Low/Med/High | Low/Med/High | |
| [Risk 2] | | | |
| [Risk 3] | | | |
| [Risk 4] | | | |

### Risk Deep Dives

**Risk 1: [Name]**
[2–3 sentences explaining the risk and how it could materially affect intrinsic value]

**Risk 2: [Name]**
[Same structure]

### Downside Scenario Analysis
*If the thesis is wrong and risks materialize:*

- Bear case owner earnings: $[X]
- Bear case intrinsic value: $[X]
- Downside from current price: [-X%]
- Comment on downside protection: [e.g., "Even in bear case, strong balance sheet limits permanent capital loss"]

---

## Section 8: Investment Thesis

### Why Own This Business?

[3–5 paragraphs. This is the heart of the investment case. Explain in plain language:
1. Why this is a great business (moat, returns, management)
2. Why it is available at a reasonable or undervalued price
3. What the 5–10 year path looks like for earnings and value creation
4. Why this is better than the index or other available investments]

### The One-Sentence Thesis
*Distill the entire investment case to a single sentence. If you can't, the thesis is probably unclear.*

[e.g., "Coca-Cola is the world's most recognized beverage brand with unparalleled global distribution, consistently high returns on capital, and a business model that requires minimal reinvestment — available today at a fair price."]

### Key Metrics to Monitor
| Metric | Current | Warning Level | Why it Matters |
|--------|---------|--------------|----------------|
| Gross margin | [X%] | < [X%] | Pricing power indicator |
| ROIC | [X%] | < [X%] | Moat quality |
| Revenue growth | [X%] | < [X%] | Business momentum |
| Debt/Equity | [X] | > [X] | Financial risk |
| [Market-specific metric] | | | |

---

## Section 9: Portfolio Recommendation

*(Complete this section if integrating into the model portfolio)*

**Suggested Action**: [Initiate / Add to / Monitor / Hold / Trim / Exit]
**Suggested Weight**: [X%] of portfolio
**Entry Range**: $[X] – $[X] (represents adequate margin of safety)
**Position Sizing Rationale**: [Why this weight? High/moderate conviction?]
**How it fits the portfolio**: [Geographic/sector diversification contribution]

---

## Section 10: Conclusion

[1–2 paragraph summary of the full analysis. State the recommendation with conviction and explain what would change your view.]

**Revisit Triggers:**

- Reassess if price falls below $[X] (add opportunity)
- Reassess if price rises above $[X] (consider trimming)
- Reassess if [specific business event, e.g., "market share falls below 30%"]
- Next scheduled review: [DATE]

---

## Sources & References

| Source | Document | Date | Key Data Used |
|--------|----------|------|--------------|
| SEC EDGAR | 10-K Annual Report | FY2024 | Financial statements |
| [Exchange] | Annual Report | FY2024 | Business overview |
| Company IR | Earnings Presentation | Q4 2024 | Management commentary |
| Macrotrends | Historical financials | — | 10-year ratio data |
| [Other] | | | |

**Fiscal-year convention:** [e.g., FY ends 31 July]

### Data Gaps

| Field | Why missing | Resolution (re-sourced from / estimated on / left blank) |
|---|---|---|
| | | |

---

**DISCLAIMER**: *This report is for informational and educational purposes only. It does not constitute personalized investment advice or a solicitation to buy or sell any security. All investments involve risk, including possible loss of principal. Past performance does not guarantee future results. Investors should conduct their own due diligence and consult a qualified financial advisor before making investment decisions.*

---

# Deliverable 2 — HTML Dashboard

> ### ⚠️ Authoritative spec lives elsewhere — do not duplicate it here
>
> The HTML dashboard is fully specified in **`web-report/references/single-stock-report.md`**:
> the complete HTML skeleton, the twelve tab definitions, required content per tab, `Charts Required`
> lists, JS data-object schemas, stat-card and sensitivity-table layouts. Load that file, plus
> `web-report/references/design-system.md`, before writing any HTML. Routing is in
> `web-report/SKILL.md`.
>
> **The canonical twelve tabs are:**
> `summary` · `business` · `management` · `financials` · `valuation` · `moat` ·
> `industry` · `risk` · `monitoring` · `verdict` · `sources` · `screener`
>
> This list is reproduced here **for cross-checking only**. If it ever disagrees with
> `web-report/references/single-stock-report.md`, that file wins and this note is the thing to correct.

**Mapping — Markdown section → dashboard tab**

| Markdown §  | Dashboard tab |
|---|---|
| 1 Executive Summary | `summary` |
| 2 Business Overview | `business` |
| 3 Management Assessment | `management` |
| 4 Financial Analysis | `financials` |
| 5 Valuation | `valuation` |
| 6 Moat Assessment | `moat` |
| 7 Industry Context | `industry` |
| 8 Risk & Trap Diagnostic | `risk` |
| 9 Monitoring & Catalysts | `monitoring` |
| 10 Verdict / Sources | `verdict`, `sources` |
| Step 0 output | `screener` |

**Do not invent tabs.** A thesis-specific analysis (an SOTP walk-through, a named hypothesis test)
belongs *inside* the tab it bears on — SOTP in `valuation`, a moat-durability test in `moat` — not in
an additional tab. Deviating from the twelve produces dashboards that look bespoke and read
inconsistently across the coverage book.

---

# Deliverable 3 — Bilingual Executive Summary (EN + 简体中文)

**Filename:** `summary_<ticker>_<YYYY-MM-DD>_EN-CN.md`
**Produced:** AFTER the Markdown report is finished. It is **derived from** the report, never authored in parallel with it.
**Length target:** 35–50KB. If it exceeds ~60KB it has stopped being a summary — cut, do not translate less.

## Purpose

The full report is an **audit document**; this is a **communication document**. It is what gets forwarded, and what gets re-read six months later to reload the thesis quickly. It must stand alone: a reader who has never opened the full report should finish it knowing the verdict, why, what would change it, and what to watch.

## Layout rule — interleaved by block

Each heading, paragraph, callout and bullet appears in **English immediately followed by 中文**. Never a full English document followed by a full Chinese one — that makes cross-checking a translation against its source impossible.

**Tables are bilingual *within cells*** (`Moat 护城河`, `Base fair value 基准内在价值`), not duplicated as two tables. Duplicating tables doubles the length for no added clarity, and side-by-side EN | 中文 columns wrap badly on a phone.

**Translate the argument, not the words.** Where a literal rendering would go flat, translate for force. The Chinese reader should get the same emphasis, not a gloss.

## Required sections — the fixed list

Produce these, in this order. Omit one only if the analysis genuinely has no content for it, and say so.

| # | Section | 中文 | Must contain |
|---|---|---|---|
| 1 | Header + verdict box | 标题与结论 | Verdict, conviction, price (+vintage), base FV with bear/bull, MoS, entry zone, aggressive, floor, position cap, next review |
| 2 | **Anchoring / framing correction** | **锚定偏差修正** | **Mandatory whenever the request arrived with a frame attached** ("crash", "plummeted", "cheap"). State the correction and the chronology table. Skip only if no frame was supplied |
| 3 | One-sentence thesis | 一句话论点 | The single sentence from §8, both languages, as a blockquote |
| 4 | What the business is | 业务本质 | 2–4 paragraphs. Plain language. How it actually makes money |
| 5 | **The decisive finding** | **分析核心** | The one analytical result the verdict turns on, with its comparison table. Name it explicitly |
| 6 | Headline decomposition | 拆解财报标题 | Check 19 or equivalent — operating vs non-operating split, wherever the headline and the business disagree |
| 7 | Valuation | 估值 | Method set stated explicitly (including what was NOT used and why) · any gate that fired · **the mandatory fade/sensitivity ladder** · triangulation table · reverse valuation |
| 8 | **The ±20% verdict-mover** | **决定性敏感性分析** | The sensitivity table that decides the call, and a plain statement of which variable actually matters |
| 9 | Quality scorecard | 质量评分 | Moat /30 with pillars, EQ /40, franchise test, value trap, 4-framework, quick-kill result, sector flags |
| 10 | Risk and downside | 风险与下行 | Risk register, Munger inversion one-liner, bear case, floor, and the risk/reward ratio at spot vs at the entry price |
| 11 | Entry discipline + portfolio | 建仓纪律与组合定位 | Entry/aggressive/trim/cap, sleeve rules, whether the entry has historically been available |
| 12 | Why this verdict and not the adjacent one | 为何是此结论 | The precedent invoked, and the specific reasons for and against |
| 13 | Pre-committed watch bar | 预设检验标准 | Downgrade triggers, upgrade triggers, metrics table with warning levels |
| 14 | Data discipline | 数据纪律 | Four anchors, classification gate, RF hits, plausibility Test 4 (consensus divergence) |
| 15 | Key figures | 关键数据 | The period's headline table + segment table |
| 16 | Legend + sources + disclaimer | 图例、来源与免责声明 | ▲ / ▲▲ meanings, acronym glosses, data vintage, bilingual disclaimer |

**What NOT to carry over:** the 10-year financial table, the full data trail, the complete RF-1→RF-8 scan narrative, the pre-verdict checklist, per-method arithmetic. Those are audit content and belong only in the full report.

## Chinese conventions — 简体, mainland finance usage

Use Simplified throughout. Match the coverage book, which is 简体. Gloss each acronym once in the legend, then use it freely.

| EN | 中文 | EN | 中文 |
|---|---|---|---|
| Embedded value (EV) | 内含价值 | Value of new business (VONB/NBV) | 新业务价值 |
| Contractual service margin (CSM) | 合同服务边际 | Margin of safety (MoS) | 安全边际 |
| Intrinsic / base fair value | 内在价值 / 基准内在价值 | Earnings power value (EPV) | 盈利能力价值 |
| Operating profit after tax (OPAT) | 营运利润 | Operating ROE | 营运净资产收益率 |
| Operating ROEV | 内含价值营运回报率 | Free surplus generation | 自由盈余生成 |
| Moat | 护城河 | Franchise | 特许经营 |
| Value trap | 价值陷阱 | Earnings quality | 盈利质量 |
| Persistency | 保单继续率 | Solvency ratio | 偿付能力充足率 |
| Agency channel | 代理人渠道 | Bancassurance | 银保渠道 |
| Discount rate | 折现率 | Risk discount rate | 风险贴现率 |
| Fade | 衰减 | Appraisal value | 评估价值 |
| Watchlist / Accumulate / Pass | 观察名单 / 逐步买入 / 放弃 | Conviction | 信心度 |
| Position cap | 仓位上限 | Entry zone | 建仓区间 |
| Sum-of-the-parts (SOTP) | 分部估值 | Owner earnings | 所有者收益 |
| Combined ratio | 综合成本率 | Net interest margin (NIM) | 净息差 |
| Book value per share | 每股账面价值 | Free cash flow | 自由现金流 |
| Cum-dividend / ex-dividend | 含息 / 除息 | Basis point | 基点 |

Extend this table whenever a new sector enters the book; do not invent a second rendering for a term already listed.

## Anti-drift controls — all three are mandatory

The summary is a fourth place a number can be wrong. These are what stop it becoming one.

1. **Derived, never parallel-authored.** Write it from the finished report, at the end. If the report changes, regenerate the summary — do not patch it.
2. **Mechanical figure cross-check before delivery.** Extract every headline figure (verdict, conviction, price, base FV, bear, bull, MoS, entry, aggressive, floor, cap, and the 8–12 numbers the thesis turns on) and assert each appears identically in the full report. Takes seconds; it is the control that actually works. Report the result.
3. **One canonical figure block.** Verdict, conviction, base FV, MoS, entry zone, floor and cap come from **the command-center JSON row** — so the report, the dashboard, the command center and the summary cannot disagree. This is rule 3 below, extended to a fourth artifact.

---

## Rules That Apply to All Three Deliverables

1. **Presentation order: HTML dashboard first, then the Markdown report, then the bilingual summary.**
   Then command-center.md, then command-center.html.
2. **Never fabricate a number to fill a cell.** An empty cell marked "not disclosed" is correct; an
   invented one is not. ▲ marks anything approximate and ▲▲ anything derived-not-disclosed, in **all
   three** files.
3. **The verdict, conviction, fair value and entry zone must be identical** across report, dashboard,
   bilingual summary and command center. A mismatch is the most common source of downstream drift —
   check before presenting. *(This is the rule the Xtep #14 error violated for eleven weeks: the JSON
   was right, the master table was stale, and the dashboard — which reads the JSON — was never wrong.
   Derive from one source; do not retype.)*
4. **Bilingual EN/ZH headers in the report and dashboard; full bilingual body in the summary only.**
   Chart axis labels may be English-only.
5. **A cross-boundary CAGR is never printed as a number.** Mark it non-meaningful and say why — see
   the accounting-standard transition rule in
   `references/earnings-quality-and-distortions.md`.
6. **Deliver deliverables 1–3 plus `command-center.html`.** Write both command-center files to
   Project Knowledge. `command-center.md` is not delivered into the conversation.

---

## Scope Variations

| Scope | Markdown report | HTML dashboard | **Bilingual summary** | Stage 6 |
|---|---|---|---|---|
| Full deep dive | All 10 sections | Full 12 tabs | **Yes — all 16 sections** | Yes |
| Quick thesis | §1, 2, 5, 6, 7, 9, 10 | Skip | **Yes — §1–3, 5, 7–8, 10–13, 15–16** | Yes |
| Thesis refresh | Refresh structure (what changed / does verdict hold / updated FV / updated entry / what to watch) | Skip | **Yes — mirrors the refresh structure** | Yes |
| Earnings reaction | §1 + delta analysis + §6–7 revised + §10 | Skip | **Yes — §1–3, 6–8, 10, 13, 15** | Yes |
| Comparison | Side-by-side across §3, 5, 6, 7, 8 | Optional | **Yes — one summary covering both names** | Yes, both names |

**The bilingual summary runs at every scope.** It is the one deliverable that always makes sense: a
refresh or an earnings reaction is *mostly* conclusion, which is exactly what the summary carries.

Stage 6 runs for every scope that produces or changes a verdict. No exceptions.
