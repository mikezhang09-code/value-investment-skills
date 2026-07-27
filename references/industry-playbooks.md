# Industry Analysis Playbooks

> When to read this file: When analyzing companies in a specific industry — look up the sector-specific evaluation framework, key metrics, historical case studies, and macro sensitivities. Different industries operate on fundamentally different economic logic; using the wrong analytical lens produces wrong conclusions.

---

## §F — Financials Cross-Cutting Rules (Insurance + Banking)

> **Validated 2026-07-26** against two live deep dives — PICC P&C (2328.HK) and PICC Group (1339.HK).
> These rules **override the generic workflow** for any insurer, reinsurer, insurance holding company,
> bank, or holding company whose earnings are mostly a regulated financial subsidiary. They apply in
> addition to the sector narratives in §Insurance and §Banking below, which remain the primary
> qualitative frameworks.

## How This File Overrides the Generic Workflow

| Step | Override status |
|---|---|
| Step 0 quick-kill screener | **Partial override** — specific questions are substituted per sector (see §F.1). Q7 (integrity) is never overridden. |
| Step 2.5 reconciliation gate | **No override.** All four anchors apply unchanged to every sector. |
| Step 3 metric table | **Full override** where a sector section specifies substitutions. |
| Step 3.5 earnings quality | **Additive.** Core Classes 1–8 and the /40 composite are unchanged. Sector classes are additional binary gating flags. |
| Step 6 valuation | **Full override** of method selection where specified. |
| Step 6.5 plausibility | **No override**, one conditioning note (see §F.6). |

**Rule:** if a sector section is silent on something, the generic workflow governs. Sector sections
narrow the generic template; they never loosen the gates.

## §F.0 Why the Generic Template Misfires on Financials

For a financial, taking deposits or premiums and investing the proceeds *is* the business. The
generic template reads that structure as distress:

- **Leverage is the product, not the risk.** Regulatory leverage of 8–15× equity is structural for a
  bank and an insurer. The generic "Debt/Equity > 1.0 = red flag" fires on every healthy financial.
- **There is no cost of goods sold.** Gross margin does not exist. Operating margin has no
  comparable construction.
- **Operating cash flow is a growth signal, not a quality signal.** Premiums and deposits arrive
  before claims and withdrawals leave. A strong operating cash-flow print usually means the book is
  *growing*. The generic "FCF > NI = high earnings quality" is not merely unhelpful here — it is
  inverted, and will read balance-sheet expansion as earnings integrity.
- **Risk is recognised on a lag.** Underwriting losses and credit losses show up years after the
  business was written. Current-period profit is substantially a management estimate.

The last point is the one that matters most. For an industrial, the main earnings-quality question is
whether reported profit converts to cash. For a financial, it is **whether the reserve or provision
against future losses is adequate** — a question cash conversion cannot answer.

## §F.1 Step 0 — Quick-Kill Screener Substitutions

Six of the eight questions apply unchanged. Two misfire and are substituted. **Q7 (management
integrity) remains an automatic veto and is never substituted** — for a financial it arguably carries
more weight than elsewhere, because reserve and provision adequacy is unverifiable from outside and
rests on management honesty.

| # | Generic question | Financials substitution |
|---|---|---|
| 5 | Does profit genuinely convert to cash? | **Insurance:** is the combined ratio earned by current underwriting, or flattered by prior-year reserve releases? **Banking:** is the credit cost normalized, or is the current year benefiting from provision write-backs? |
| 6 | In a worst case (revenue −30%), can it survive without dilution? | **Insurance:** does the solvency ratio hold above the regulatory intervention threshold under a stress scenario (1-in-200 catastrophe for P&C; a 100bp+ rate move plus equity drawdown for life)? **Banking:** does CET1 hold above requirement plus buffer under stressed credit costs? |

Q6's substitution is the reason the generic version fails: an insurer does not fail from a revenue
decline, it fails from a capital shortfall against liabilities it already wrote.

## §F.2 Step 3 — Metric Substitutions (all financials)

| Generic metric | Status | Replacement |
|---|---|---|
| Gross margin % | **Delete** | Does not exist |
| Operating margin % | **Delete** | Insurance: combined ratio (综合成本率) — inverse sense, below 100% = underwriting profit. Banking: cost-to-income ratio (成本收入比) |
| Debt/Equity > 1.0 = red flag | **Delete** | Insurance: solvency ratio (偿付能力充足率), both comprehensive and core, under C-ROSS II. Banking: CET1 / total capital adequacy ratio. Regulatory leverage is structural, not a warning |
| FCF persistently < NI = red flag | **Delete — actively misleading** | Operating cash flow is dominated by premium/deposit timing and reserve/provision movement. Track book value growth and reserve or provision adequacy instead |
| FCF > NI = quality green flag | **Delete — actively misleading** | Usually signals a growing book, not clean earnings |
| ROE % | **Keep — primary** | The core compounding measure. **Always decompose** — insurance: underwriting vs. investment contribution; banking: NIM vs. fee vs. credit cost |
| ROIC % | **Delete** | Invested capital has no clean construction when the liability side is the funding source |
| Book value / share | **Keep — promote to primary** | BVPS growth (plus dividends) is the core long-run scorecard, especially for P&C |
| EPS (diluted) | **Keep** | Unchanged |
| Revenue | **Keep, redefine** | Insurance: gross written premium *and* net earned premium — state which. Banking: net interest income + non-interest income |

> ⚠️ **Book-value quality caveat (amendment, 2026-07-26).** BVPS is promoted to a primary metric
> above, and for financials it is usually the P/B denominator — but **book value is itself
> mark-to-market** for any institution carrying a large equity or FVTPL portfolio. Striking P/B at a
> market high therefore re-imports the exact cyclicality that normalizing the ROE numerator was meant
> to remove, and the error compounds: the numerator is normalized while the denominator is not.
> **Where the equity weight exceeds ~15% of investment assets, state the equity weight next to the
> P/B, and sanity-check fair value against a normalized book value as well as the reported one.**
> PICC P&C carried a 27.9% equity weight into a market high; its Q1 FY26 net profit fell 24% on
> mark-to-market losses, which hits earnings *and* book simultaneously.

**The undecomposed-ROE rule.** Never report a financial's ROE as a single number. An insurer earning
its ROE from investment gains while underwriting at a loss is a leveraged bond fund with a
distribution network, and should be valued as one. The same logic applies to a bank whose ROE is
carried by trading income rather than net interest margin.

### The post-merger funding-mix rule (banking) — amendment 2026-07-26

Whenever a bank's margin is compressed following a merger, **decompose the compression before
assuming any of it reverses**:

| Component | Side | Nature | Reverses? |
|---|---|---|---|
| Credit-deposit ratio normalization, loan-book re-gearing | **Asset** | Transitional | **Yes** — with balance-sheet growth |
| High-cost acquired borrowings rolling off | **Liability** | Transitional | **Yes** — with maturity schedule |
| **CASA / deposit-mix change** | **Liability** | **Structural** | **No** — the funding franchise itself changed |

**Never assume a merged bank recovers to the acquirer's pre-merger NIM.** The acquirer's margin was
a function of its *own* liability mix. Absorbing a wholesale-funded balance sheet permanently dilutes
that mix, and no amount of asset-side normalization restores it.

**Track the CASA ratio as the deciding series** — and specifically whether CASA growth is running
ahead of or behind time-deposit growth. A CASA ratio that is falling *while* the CD ratio normalizes
is the signature of a thesis that will half-deliver: growth returns, margin does not.

*Live case (HDFC Bank, 2026-07-26):* CASA 44% (FY23, pre-merger) → 34.1% (FY26) → **32.3% (Q1 FY27)**,
with time deposits +17.4% against CASA +9.4%. Gross advances grew **+15.4%** — the asset-side thesis
delivered in full — while NIM fell to a **record-low 3.26%**. The May-2026 analysis had treated 100%
of the compression as transitional and carried a BUY at a fair value ~48% above the refreshed number.
**This rule is the direct output of that error.**

> **Numbering note (2026-07-26).** The 2026-07-26 (b) change log entries reference "§F.3" for the
> float-cost and life new-business amendments, but **no §F.3 or §F.4 header exists in this file** —
> the sections run §F.2 → §F.5, and that content sits inside §F.2. This rule is therefore placed in
> §F.2 with the rest of the metric substitutions. Either create §F.3/§F.4 headers or correct the
> dangling references on next touch; do not add more of them.

## §F.5 Step 6 — Valuation Adaptations

| Method | Insurance | Banking |
|---|---|---|
| **P/B calibrated to sustainable ROE** | **Conditional — see #11-R.** Justified P/B ≈ (ROE − g)/(r − g) is **VOID where g ≥ r** and may not carry primary weight where ROE × (1 − payout) ≥ r − 1pp | **Conditional — same construction, same constraint.** Most high-quality Asian banks fail the condition unconditionally (IBN: g 13.5% vs r 12% → negative output) |
| **Residual income with explicit moat-calibrated fade** | **Primary anchor** (replaced P/B, 2026-07-26 (d)) | **Primary anchor.** Fade-sensitivity ladder mandatory per #11-R |
| **EPV on normalized underwriting profit** | **Floor.** Establishes the no-growth downside per house discipline | **Floor**, on normalized pre-provision profit less normalized credit cost |
| **SOTP** | **Mandatory for holdcos.** Now defined as Method 6 in `intrinsic-value.md` | Mandatory for holdcos |
| **Embedded value** | **Life only.** Dense with management assumptions (discount rate, mortality, lapse). Stress-test each; never accept as reported | N/A |
| **DDM** | Usable for mature, stable-payout insurers | Usable — often the cleanest method for a mature bank |
| **Owner Earnings DCF** | **Degrades badly.** "Owner earnings" require float adjustment; the maintenance-capex construction has no clean analogue. If used at all, use as a cross-check, never as the primary anchor | Same caveat |
| **Graham Formula** | **Do not use.** Close to meaningless on an insurer | **Do not use** |
| **NCAV / asset-based** | Not applicable | Not applicable |

> ⚠️ **P/B and EPV are NOT independent methods (amendment, 2026-07-26).** Justified P/B is
> (ROE − g)/(r − g) and EPV is E/r. As normalized ROE approaches r, the two converge by construction —
> they are the same statement about earning power expressed against different denominators.
> **Triangulating on both and calling it two confirmations overstates confidence.** On PICC P&C the
> base case produced a P/B fair value of HK$17.52 and an EPV of HK$16.55; that 6% agreement is
> arithmetic, not corroboration. Where both are used, say so explicitly and treat them as **one**
> method for the purpose of the probability weighting, then reach for a genuinely independent third —
> DDM, SOTP, or a peer multiple cross-check.

This means a financial will usually triangulate on **P/B-on-sustainable-ROE + EPV + DDM or SOTP**,
not on the DCF-led combination used elsewhere. State the method set explicitly in the report — a
reader who sees no DCF should be told why, not left to assume it was skipped.

> ⚠️ **Fade disclosure is mandatory (amendment 2026-07-26, UNVALIDATED).** Justified P/B and
> residual income are both dominated by the terminal fade assumption. The full rule — print the
> fade-sensitivity ladder, and demote justified P/B to corroborative where **(r − g) < 3pp** — is in
> `intrinsic-value.md`. Note that for a healthy bank the narrow-spread condition is the *normal*
> case, not an edge case, since sustainable g = ROE × (1 − payout). Pending validation on ICICI (IBN).

## §F.6 Step 6.5 — One Conditioning Note

Test 1 ("too good to be true") conditions its skepticism on heavy analyst coverage, and correctly so.
Several financials in the relevant markets are structurally under-covered. **On a name with thin
coverage, Test 1 does not fire by default** — a wide MoS there is not automatically a model error.
Substitute Tests 2 and 3 (peer multiple cross-check and reverse DCF) as the primary discipline, and
say in the report which test set was applied. Tests 2–4 otherwise apply unchanged.

## §F.7 Sector Distortion Classes (Step 3.5 add-on)

**Numbering rule.** The core earnings-quality classes 1–8 in `earnings-quality-and-distortions.md`
are universal and are **not** renumbered. Sector classes carry a sector prefix — I-n for insurance,
B-n for banking — so that a bare "Class 3" always means the universal class, and so these never
collide with the separately-numbered error classes in `process-lessons.md`.

**Scoring rule.** These do **not** enter the /40 earnings-quality composite. The composite stays at
8 dimensions × 5 so that scores remain comparable across the whole coverage book. Sector classes are
**binary gating flags**: each is either clear or flagged. Any flag raised must appear in the
executive summary. **Two or more flags raised caps conviction at 6/10** and requires normalized
figures throughout the valuation, mirroring the core gate condition.

### I-1 — Prior-year reserve development
The single largest discretionary earnings lever in P&C. Favourable development releases prior
reserves into current-year income; adverse development does the reverse. A combined ratio flattered
by releases is not the same as one earned by underwriting.
*Check (harvesting):* Is the current-year result dependent on prior-year releases? What is the multi-year pattern?
Persistent favourable development may indicate systematic over-reserving (conservative, benign) or
reserve harvesting to smooth results (not benign). Distinguish by whether releases are stable in size
or conveniently sized to hit a target.

*Check (strengthening — the positive case, amendment 2026-07-26):* **This class is not only a
detector of bad news.** Run the test in both directions:

| Signal | Reading |
|---|---|
| Reserve ratio **falling**, reserves growing slower than earned premium | Possible harvesting — the reported CoR is flattered. Investigate |
| Reserve ratio **rising**, reserves growing faster than earned premium | **Strengthening.** The reported CoR is *understated* relative to a constant-reserving peer, and its credibility is enhanced |

A rising reserve ratio is a **credibility multiplier on every other underwriting number in the
report**, and should be stated as such rather than passed over. On PICC P&C, reserves grew 7.6%
against revenue of +5.4% with the reserve ratio up 1.6pp — which is what allowed the §F.8 expense-only
finding to be read as a genuine operating fact rather than a possible reserving artifact. Without
clearing I-1 in the positive direction, that conclusion would have been unsafe.

### I-2 — Long-tail discount rate assumptions
Under IFRS 17, discount rates on long-duration liabilities materially affect reported profit and
equity. Small assumption changes move large numbers.
*Check:* Disclosed discount rate vs. peers. Direction of assumption change vs. direction of the
earnings surprise — if they move together, the surprise is partly manufactured.

### I-3 — IFRS 17 / CAS 25 comparability break
The insurance instance of the universal transition-break rule now in
`earnings-quality-and-distortions.md` ("Accounting-Standard Transition Breaks"). Adopted 2023 by HK
and mainland listed insurers. **A ten-year table spanning that boundary is not comparable, and any
CAGR computed straight through it is invalid.** Compute pre- and post-transition series separately,
or use restated figures only. State the basis in the Data Trail.
*Open question — **RESOLVED 2026-07-26** (PICC P&C):* pre-2023 series are **not** usable. HKFRS 17 and
HKFRS 9 were adopted 1 January 2023 with **only FY2022 restated**, so the comparable window is
FY2022(restated) → present. For a 2026 analysis that is **four years, not ten.** The constraint is
more severe than originally anticipated:

- **A ten-year table is impossible for any HK/mainland insurer.** Do not build one. State the
  four-year limit explicitly in the report rather than silently truncating.
- Pre-transition figures may be shown for context **only** if labelled non-comparable and excluded
  from every growth calculation.
- Combined ratio specifically is redefined by the standard (the HKFRS 17 formula includes insurance
  finance income/expense), so pre-2023 CoR is not merely differently-based — it is a different
  measure.

*Bonus resolution:* the comprehensive-vs-core solvency labelling ambiguity is settled by convention —
**comprehensive > core** always. Verified on PICC Group (249.9% / 201.3%) and applied to PICC P&C
(232.4% / 213.4%).

### B-1 — Provisioning and ECL discretion
The banking analogue of I-1. Expected-credit-loss provisioning under IFRS 9 / CECL is
management-estimated and cycle-sensitive. Write-backs flatter current earnings; front-loading
depresses them.
*Check (harvesting):* Credit cost in bps vs. the bank's own 10-year range and vs. peers. Is the
current year's profit growth explained by lower provisions rather than higher pre-provision profit?
Compute pre-provision operating profit growth separately — it is the cleaner series.

*Check (integrity — the positive case, amendment 2026-07-26):* **Like I-1, this class is not only a
detector of bad news.** Run it in both directions:

| Signal | Reading |
|---|---|
| Provisions **falling**, credit cost below the bank's own range, profit growth tracking the release | Possible harvesting — reported profit is flattered. Investigate |
| Provisions **rising**, credit cost rising, and a **discretionary buffer left unreleased through a consensus miss** | **Reporting integrity demonstrated.** A credibility multiplier on every other figure in the release |

**Two branches (refined on IBN, 2026-07-26 (d)) — the original construction assumed a miss:**

| Situation | Test |
|---|---|
| **On a MISS** | Did management decline to release a buffer that would have converted it? Compare the size of the miss to the size of the unreleased buffer. *(HDB: 3.0% of the buffer would have sufficed; declined.)* |
| **On a BEAT** | Was the beat **earned or manufactured**? Test whether PAT growth is matched by **pre-provision / core operating profit growth**, and whether the buffer is intact. *(IBN: PAT +15.95% vs core operating profit +15.6%, ₹13,100cr buffer held → **earned**.)* |

**The miss branch is the stronger signal** — it required management to accept a visible cost. The
beat branch is confirmatory rather than probative.

**On the miss branch, the diagnostic is a ratio, not a direction: compare the size of the consensus
miss to the size of the unreleased buffer.** A management that could have converted a miss into a beat by releasing a
trivial fraction of a discretionary buffer, and did not, has told you something about the reliability
of the whole release — and the signal is strongest precisely when the incentive to release was
highest.

*Live case (HDFC Bank, Q1 FY27, 2026-07-26):* provisions **+17.3% QoQ**, credit cost 35bp → 40bp,
against a consensus miss of **₹272cr** while carrying a **~₹9,000cr** floating/contingency buffer
built a year earlier and never released. Releasing **3.0%** of it would have produced a beat. The
bank declined — during a governance crisis, with the CEO's reappointment before the RBI. That
finding set the verdict floor at HOLD rather than AVOID and lifted conviction from ~4 to 6. **No
sell-side note surfaced it.**

> ⚠️ **Buffer figures are frequently not restated in the quarterly presentation.** Where the
> unreleased balance is inferred rather than confirmed, mark it ▲, log it under RF-1, and state the
> positive reading as *conditional*. If the buffer was quietly drawn down, the finding inverts.

## §F.8 The Underwriting-Improvement Signature (monitoring rule)

Applies whenever a thesis, a management narrative, or a sell-side note claims an insurer's
underwriting is structurally improving — from technology, data, pricing discipline, or anything else.

**Cost improvements hit the expense ratio first and the loss ratio later.**

- **Expense ratio improvement alone = cost-cutting.** Anyone can do it, it competes away, and it
  proves nothing about risk selection.
- **Loss ratio improvement at constant business mix = risk selection genuinely improved.** That is
  the real claim.

**The test is the divergence, not either series alone.** If only the expense ratio moves, the claim
is unproven regardless of how compelling the narrative sounds.

**Monitoring procedure:**
1. Track expense ratio and loss ratio as separate quarterly series.
2. Control for business mix — a loss-ratio shift caused by re-weighting toward non-motor is not
   evidence.
3. Control for the pricing cycle — soft and hard markets move loss ratios for unrelated reasons.
4. Require multi-year persistence. One good year is weather, reserve release, or luck.

**Binding classification.** Until the loss-ratio series confirms divergence, any such claim is
**qualitative moat evidence only**. It does **not** enter the valuation and is **not** a
verdict-moving input under the ±20% rule in `data-sources.md`. Acting on it before the series
confirms is paying for a forecast, not reading a fact.

**Three outcomes, not two (amendment #15, 2026-07-27).** The test can **PASS**, **FAIL**, or be
**UNRUNNABLE**. Where the issuer does not disclose the inputs the test requires:

1. Record the test as **UNRUNNABLE** and **name the missing disclosure**.
2. **Do not let the headline substitute for the split.** A combined ratio that improved is not
   evidence about risk selection; it is an undiagnosed number that could be underwriting discipline,
   expense leverage or reserve release — three findings with three different persistence profiles.
3. The improvement **does not enter fair value**, on the same footing as an unconfirmed PASS.
4. **Log the gap in the moat and management assessment.** An issuer that withholds the split is
   telling you something about disclosure quality, which is itself a governance datapoint. Do not
   discard the observation just because the test failed to run.

**Never collapse UNRUNNABLE into PASSED** (the charitable error) **or into FAILED** (the lazy one).
They are different information and they justify different position sizes.

*Live contrast, 2026-07-27.* **PICC P&C (2328.HK)** — the test **ran and failed**: expense ratio moved,
loss ratio did not, so the improvement claim was unproven and classified as cost-cutting.
**Taiping Insurance (P&C arm of 0966.HK)** — the test is **UNRUNNABLE**: only a headline combined ratio
is disclosed (98.8%, −1.3pt) with no expense/loss split at all. The −1.3pt is real and undiagnosable.
Recorded as unrunnable, excluded from fair value, and logged against disclosure quality. Conflating
the two would have credited Taiping with PICC P&C's *finding* while it had produced no finding at all.

*Provenance note:* this rule was developed while stress-testing a specific directional thesis about
cheap machine cognition and insurance margins. That thesis is deliberately **not** in Project
Knowledge — an unproven directional argument sitting in the default load path becomes a prior that
the analysis is then run to confirm, which is the failure mode `sell-discipline-and-traps.md` guards
against. The test above is thesis-neutral and survives on its own merits. If a live thesis is being
evaluated in a session, it belongs in that session's context, not here.

## §F.9 Data Sources for Financials

Extends `data-sources.md`. Same primary-source discipline applies.

**Mainland China insurers and banks**
- **NFRA** (国家金融监督管理总局) — regulatory rulings, permitted pricing granularity, industry
  aggregates. Note that permitted motor-pricing granularity is a policy variable, not a technical
  one, and can change.
- **Quarterly solvency reports** (偿付能力季度报告) — published separately from annual reports,
  usually on the insurer's own site. Contains comprehensive and core solvency ratios, risk
  comprehensive rating, and stress-test disclosures. **This is the primary source for the §F.1 Q6
  substitution and is not in the annual report.**
- **Industry association aggregates** (中国保险行业协会 / 中国银行业协会) for market share and
  premium-pool trajectory.

**HK-listed (H-share) insurers and banks**
- HKEx News annual and interim reports — combined ratio, NBV, EV, solvency all disclosed here.
- ⚠️ **Step 2.5 Anchor 4 is live on every A+H financial.** Verify share-class structure before any
  per-share work. This is the trap that produced the Ping An discrepancy (18.2B true vs. 7.45B
  shown) and the BYD error. Cross-listed insurers and banks are among the most common instances.

**Indian banks (HDFC Bank, ICICI)**
- RBI disclosures and the bank's own quarterly investor presentation — NIM, NPL, provision coverage,
  CET1 are all in the quarterly deck, usually before they appear in any filing.

**US filers**
- SEC EDGAR 10-K Schedule P (P&C loss development triangles) is the primary source for I-1. It is
  the most useful single disclosure in US insurance filing and has no direct equivalent in most
  other jurisdictions — where it is absent, I-1 must be assessed from narrative disclosure and
  flagged as lower-confidence.

## §F.10 Report and Command-Center Integration

- The 10-year table in the report replaces the deleted rows with the §F.2 substitutions. Do not print
  an empty gross-margin row.
- State the transition basis (pre-2023 / post-2023 / restated) in the Data Trail wherever a
  multi-year series crosses the IFRS 17 boundary.
- The command-center `note` field should carry combined ratio (decomposed) and solvency for an
  insurer, or NIM and CET1 for a bank, in place of the margin figures used for industrials.
- Sector distortion flags raised (I-n / B-n) are recorded in the note alongside any core EQ flag.

---

## Insurance

Buffett's most deeply understood industry and the core engine of Berkshire.

### The Industry's Unique Logic

Insurance is a "collect now, pay later" business. Between premium income and claims payouts, insurers hold large amounts of freely investable "float." An excellent insurance company = access to **free or even negative-cost capital** for long-term investment.

The industry's average ROE is only ~8.5%, far below the Fortune 500 average of ~14%, because most insurers write business at a loss to chase market share.

### Core Evaluation Metrics

| Metric | Description | Excellence Standard |
|--------|-------------|---------------------|
| Combined Ratio | (Claims + Expenses) / Premium Revenue | < 100% (underwriting profit) |
| Underwriting Profit/Loss | Premium − Claims − Expenses | Consistently positive |
| Float Size | Total investable funds held | Larger is better |
| Float Growth Rate | Trend in float accumulation | Steady growth |
| Float Cost | Combined Ratio − 100% | Negative = others pay you to invest |

### Underwriting Discipline (Most Important Factor)

Float only has value when its cost is below the return on investment. The ability to say "No" to poorly priced business — and sustain that discipline even when competitors are aggressively cutting prices — is the single most important factor.

**Tests for underwriting discipline:**
- Combined ratio history during competitive soft markets: Did discipline hold?
- Performance after catastrophe years: Did the company opportunistically raise prices (correct) or chase volume?
- Has the company ever sacrificed pricing to gain market share?

### Float Economics

| Combined Ratio | Float Cost | Meaning |
|----------------|-----------|---------|
| < 100% | Negative (free + income) | Others are paying you to invest their money |
| = 100% | Zero (free) | You invest at no cost |
| > 100% | Positive (expensive borrowing) | You're paying to hold float — value-destroying |

**Three structural advantages of insurance float vs. debt:**
1. Cannot be "run on" — no redemption clauses (unlike bank deposits)
2. Near-permanent capital — total float remains stable even as individual policies cycle
3. Understated on balance sheet — recorded as a liability, but for zero-cost float, it's a hidden asset

### Macro Sensitivities

- **Rising rates:** Improves investment returns on float; beneficial for long-duration bond allocators
- **Inflation:** Increases claims costs (medical, repair, replacement); compresses margins if pricing can't keep pace
- **Catastrophe events:** Short-term underwriting losses, but often bring pricing hardening — disciplined companies expand as competitors retreat
- **Economic recession:** P&C premium volumes shrink; but catastrophe demand is inelastic

### Additional Metrics — validated 2026-07-26

**Combined ratio, always decomposed.** Split into expense ratio (费用率) and loss ratio (赔付率).
Never report the headline alone — the split is load-bearing for §F.8.

**Underwriting profit and investment income, tracked separately and never netted.** Two businesses,
two earnings qualities, two multiples.

**Float — MANDATORY, report in the table not the prose (amendment, 2026-07-26).**

| Float metric | Formula | Why |
|---|---|---|
| Float size | ≈ net loss & LAE reserves (+ unearned premium where disclosed) | The scale of the free capital |
| **Float cost** | **− underwriting profit ÷ average float** | **Negative = the insurer is *paid* to hold it. The Buffett condition** |
| Float growth | YoY change in the above | Compounding capacity |

This is the single most important structural number for any insurer and it must appear in the
report's metrics table, not only in commentary. On the first live run it was the fact that separated
"WATCHLIST" from "PASS": PICC P&C's float cost of roughly −6.4% is what makes a commodity business
with a narrow moat still worth tracking.

**Reserve adequacy.** Prior-year development and run-off triangles where disclosed. See I-1 below.

**By sub-sector:**

| Sub-sector | Add |
|---|---|
| P&C | Combined ratio by line, retention rate, mix (motor vs. non-motor) |
| Life | New business value (NBV/新业务价值), NBV margin, embedded value, persistency/lapse rates, **PV of loss-making new contracts (mandatory — see below)**, channel mix (agency vs bancassurance), agent headcount trend |
| Reinsurance | Combined ratio by treaty year, catastrophe exposure (PML), retrocession dependence |
| Health | Medical loss ratio, claims leakage |

> ⚠️ **Life new-business quality — NBV growth alone actively misleads (amendment, 2026-07-26).**
> Under IFRS 17 / CAS 25, insurers disclose the **present value of loss-making (onerous) new
> contracts**. This is the metric that reveals whether growth is being *earned* or *bought*, and it
> can point the opposite way to NBV. PICC Life posted the **fastest** one-year NBV growth in the
> Chinese sector (+64.5%) and the **fastest** premium growth (+18.8%) while writing **over 40% of the
> five listed insurers' combined RMB 310bn of loss-making new contracts** — the worst in the sector
> by a wide margin. On NBV alone it was the best performer; on new-business quality it was the worst.
>
> **Always pair NBV growth with the onerous-contract disclosure, and always check the channel mix
> alongside it.** A shift from agency to bancassurance is a shift from an owned distribution moat to
> a rented channel with worse economics — PICC Life's bancassurance share crossed 54.2% (+6pp,
> overtaking agency for the first time) while agent headcount fell 7%. Rapid growth through a rented
> channel at negative contract economics is the specific pattern to look for.

---

## Banking

Excellent banks can be outstanding investments; leverage makes banking one of the most dangerous industries.

### The Industry's Special Nature

- **Inherently high leverage:** Banks typically operate at 15–20× leverage; modest credit losses can wipe out shareholder equity
- **Credit quality is the lifeline:** Loan portfolio quality determines long-term fate; problems typically surface only years later
- **"Black box" risk:** Complexity makes it nearly impossible for outsiders to truly assess loan quality, derivatives exposure, and trader behavior

### Core Evaluation Metrics

| Metric | Description | Excellence Standard |
|--------|-------------|---------------------|
| ROE | Return on Equity | Consistently > 15% |
| ROA | Return on Assets | > 1.2% |
| NPL Ratio | Non-Performing Loans / Total Loans | < 1% |
| Provision Coverage | Loan Loss Reserves / NPLs | > 200% |
| CET1 Ratio | Core Equity Tier 1 / Risk-Weighted Assets | > 10% (above regulatory minimum) |
| NIM | Net Interest Margin | Compare vs. peers; watch trend |
| Efficiency Ratio | Operating Expenses / Revenue | < 55% |
| Price/Tangible Book | Market Cap / Tangible Equity | Compare to ROE quality |

### Banking-Specific Red Flags
- Opaque loan portfolio with vague disclosures
- Over-reliance on capital markets activities vs. traditional lending
- Management claims "loan quality is excellent" but can't elaborate with specifics
- During banking crises, "looks cheap" is often a trap — real losses haven't yet surfaced
- Rapid loan growth during credit booms — this is the seed of future losses

### Buffett's Lesson: Why He Ultimately Moved Away from Banks
The "black box" nature means loan quality, derivatives exposure, and trader behavior can accumulate fatal vulnerabilities beneath a calm surface. After 2020, Buffett substantially reduced nearly all bank holdings. Lesson: even within the circle of competence, if transparency is insufficient, caution is warranted.

### Macro Sensitivities
- **Rising rates:** NIM expands short-term, but long-duration bond portfolios incur losses; rising deposit costs can erode spreads
- **Economic recession:** Loan defaults rise; under high leverage, modest losses amplified dramatically
- **Deflation/falling asset prices:** Collateral values decline; loan quality deteriorates sharply
- **Liquidity crisis:** Bank runs happen fast; confidence collapse can destroy an apparently healthy bank in days

### Additional Metrics — added 2026-07-26 (unvalidated)

Applies to the existing coverage (HDFC Bank, ICICI) and any future bank.

- **Net interest margin (NIM)** and its direction against the policy-rate cycle
- **Cost-to-income ratio**
- **Asset quality:** gross and net NPL ratio (不良率), provision coverage ratio (拨备覆盖率), credit
  cost (bps of average loans), and the restructured/watchlist book where disclosed
- **Capital:** CET1, total CAR, and headroom over requirement
- **Funding:** CASA ratio, loan-to-deposit ratio, deposit cost trend
- **Growth quality:** loan growth vs. system growth, and mix shift toward higher-yield/higher-risk
  segments

**The credit-cost normalization rule.** A bank's reported profit in a benign credit year is not its
mid-cycle profit. Value banks on normalized credit cost across a full cycle, in the same way the
house treats commodity cyclicals on mid-cycle rather than peak earnings.

---

## Consumer Brands & Retail

One of Buffett's most successful investment areas (Coca-Cola, Gillette, See's Candies).

### Consumer Brand Moat Characteristics
- **Repeat purchase:** Daily/weekly, habitual, minimal decision friction
- **Emotional bond:** Consumers form attachments beyond rational features
- **Pricing power test:** Raise prices 5–10% with near-zero volume loss → brand moat confirmed
- **Global scalability:** Same product distributed worldwide, declining marginal costs
- **Inflation resistance:** Brands with pricing power pass through costs; asset-light models require minimal reinvestment

### See's Candies — The Philosophy-Changing Case
Acquired for $25M in 1972. Taught Buffett three foundational lessons:
1. Brand power can generate returns far exceeding tangible assets
2. Businesses with pricing power withstand inflation
3. Asset-light + high-cash-flow models are far superior to capital-intensive ones

By 2007, See's had contributed >$1.3B in pre-tax profit with almost no additional capital. **Asset-light + pricing power = compounding machine.**

### Retail vs. Brands — The Distinction
Moats in retail are usually **narrower** than in consumer brands. Many retailers once grew astonishingly fast, then reversed sharply. Retail success requires being "smart every day" — competitors constantly copy and surpass you.

**Brand moat** = built on consumer psychology (hard to replicate)
**Retail moat** = built on operational excellence (can be replicated with enough effort)

### Key Metrics for Consumer Analysis
- Organic revenue growth (excluding acquisitions and currency)
- Gross margin trend (pricing power signal)
- Brand reinvestment rate (advertising + R&D as % of revenue)
- Same-store sales growth (for retailers)
- Market share trend vs. competitors

### Macro Sensitivities
- **Recession:** Staples (Coca-Cola, P&G) resilient; discretionary (luxury, furniture) vulnerable
- **Inflation:** Brands with pricing power pass through costs; raw material prices test that power
- **Rising rates:** High-multiple consumer brands see discount-rate pressure on valuations
- **Cultural/health trends:** Carbonated beverages under pressure from health consciousness; brand aging across generations

---

## Media & Publishing

### The Former "Toll Bridge" (Historical)
In the 1970–80s, a city's monopoly daily newspaper was like a toll bridge — advertisers had no alternative. Minimal capital requirements, strong pricing power, stable cash flows. This moat was among the widest in any industry.

### The Moat Destruction Case Study
The internet systematically destroyed the newspaper moat: Craigslist eliminated classified ads (the revenue lifeblood), digital media broke local monopolies, free online content commoditized news. Buffett's 1991 warning: "The economics of newspapers have eroded somewhat — though much of that erosion has been leisurely." By 2020, he had exited media entirely.

**Key lesson:** Technological disruption can destroy a decades-old moat in years. **Durability of moat > current width of moat.**

### Modern Media/Platform Analysis
**New moat sources (digital era):**
- Subscription stickiness (Netflix, Spotify)
- Content ecosystem IP (Disney's franchises)
- Data network effects (algorithm-driven recommendation platforms)

**Key question:** Is revenue derived from genuine user value, or from monetizing user attention (advertising)? The latter has a more fragile moat.

---

## Energy & Utilities

### Why Buffett Likes Regulated Utilities
- Stable, predictable cash flows with inelastic demand
- Can absorb large amounts of capital (Berkshire's capital needs deployment)
- Regulation provides implicit protection from competition
- Renewable energy investment has policy-supported long-term growth

### Evaluation Points
- Regulatory friendliness (historical rate approval track record)
- Sustainability of capital expenditure plans
- Interest rate sensitivity (high leverage + capital-intensive = rate-sensitive)
- Economic growth in the service territory

### Oil & Gas: Opportunism and Lessons
- **PetroChina (success):** Bought $488M stake in 2002; sold for ~$4B in 2007. Purchased when market value was far below oil reserve value.
- **ConocoPhillips (lesson):** Large purchase at peak oil prices in 2008; admitted buying "when oil and gas prices were near their all-time highs."
- **Key principle:** Commodity investments are cyclical — buy at trough earnings, sell at peak. Never extrapolate peak commodity prices.

### Macro Sensitivities
- **Rising rates:** Utilities are "bond substitutes"; rate rises cause valuation pressure
- **Inflation:** Capex costs (steel, equipment, labor) rise; regulatory rate adjustments lag
- **Energy price volatility:** For generators, fuel cost is the key variable
- **Policy shifts:** Renewable energy incentives directly affect investment returns

---

## Railways

### Sources of Competitive Advantage
- **Irreplicability:** Major rail networks took 100 years to build; cannot be rebuilt at any cost. BNSF's book value was $70B; replacement would cost $500B+.
- **Efficient scale:** Major trunk lines already saturated; new entrants would find it unprofitable.
- **Fuel efficiency:** 4× more fuel-efficient than trucking for long-haul freight; this advantage widens as environmental costs rise.

### Key Metrics
- Operating ratio (operating expenses / revenue) — lower is better; <65% is excellent
- Revenue ton-miles trend
- Pricing power (rate increases vs. inflation)
- Capital expenditure as % of revenue (railways are capital-intensive; 15–20% is normal)

---

## Technology

Buffett historically avoided technology, citing inability to predict which companies would have durable competitive advantages. His one major success — Apple — was analyzed as a **consumer brand**, not a technology company.

### Technology Moat Durability Rankings

| Moat Source | Durability | Example |
|-------------|-----------|---------|
| Ecosystem lock-in | Very high (self-reinforcing) | Apple iOS, Microsoft Windows |
| Switching costs (enterprise) | High (data + training + integration) | Salesforce, SAP |
| Data flywheel | High (data accumulation is irreversible) | Google Search |
| Network effects (platform) | High but can tip suddenly | WeChat, Visa |
| Brand (consumer tech) | Moderate to high | Apple hardware |
| Proprietary technology | Low to moderate (can be disrupted) | Most pure-tech plays |

### The Apple Case Study
Buffett redefined Apple as a consumer goods company: moat = brand emotional bond + iOS ecosystem switching costs. Users' psychological and economic cost of switching is extremely high (photos, apps, habits, device interconnectivity). Analyzed through the consumer brand framework, not technology framework.

### Technology-Specific Risks
- **Disruption speed:** Technology moats erode faster than any other type
- **Valuation challenge:** Growth-stage companies often have no current earnings; traditional methods break down
- **Winner-take-all dynamics:** Platforms can flip suddenly when network effects tip
- **If intrinsic value cannot be reliably estimated, don't invest** — no matter how impressive the company looks

### Macro Sensitivities
- **Rising rates:** Devastating to high-growth tech valuations (far-future cash flows discounted more)
- **Recession:** Ad-tech is pro-cyclical; SaaS subscription models more resilient; consumer tech partly counter-cyclical
- **Regulation:** Antitrust and data privacy legislation are structural risks for platforms
- **Geopolitics:** Supply chain risks (semiconductors), market access restrictions (China tech)

---

## Industries to Avoid — Permanent Counter-Examples

### Airlines
"Since Kitty Hawk, the net return from all airlines' efforts has been minus zero." Structural problems: seats are a commodity, high fixed costs, uncontrollable fuel prices, powerful unions, zero pricing power. Buffett was burned three times (USAir 1989, four airlines 2016, COVID exit 2020).

**Exception — NetJets:** Fractional jet ownership, 75% market share, genuine moat. The business model, not the industry, determines value.

### Textiles
"A good managerial record is far more a function of what business boat you get into than it is of how effectively you row." Berkshire's textile operations (1965–1985) were the most expensive lesson: even brilliant management cannot overcome commodity products + global competition + zero pricing power.

**The "Standees at a Parade" trap:** Each company's investment individually looks rational, but when all invest, overcapacity drives down industry returns for everyone — all participants invest more, returns stay flat.

### General Pattern of Industries to Avoid
- Products are commodities with no differentiation
- Competitors can freely enter
- High fixed costs + strong cyclicality
- Powerful suppliers or labor unions capture most value
- Chronic overcapacity driven by the "standees" dynamic

---

## HK/China-Specific Industry Notes

When applying these playbooks to HK/China-listed companies:

- **Insurance (China):** Watch for regulatory-driven pricing windows; investment return assumptions in life insurance are heavily regulated; combined ratio disclosure may be less granular than US peers
- **Banking (China):** SOE banks have implicit government backing but also political lending pressure; NPL disclosure may understate true exposure; watch for "special mention" loan category trends
- **Consumer (China):** Brand dynamics differ — domestic brands gaining share vs. foreign brands in many categories; social commerce (live streaming) adds distribution complexity; pricing power tests must account for intense e-commerce competition
- **Technology (China):** Regulatory intervention risk is uniquely high (Ant Financial, Didi, education sector); VIE structure adds structural uncertainty; ADR vs. H-share listing differences matter for governance

---

## Using This Playbook

1. **Identify the industry** from the company's revenue breakdown
2. **Jump to the relevant section** above
3. **Apply the industry-specific metrics** alongside (not replacing) the standard Graham-Buffett framework
4. **Check macro sensitivities** against the current macro environment
5. **Cross-reference with the "Industries to Avoid" section** — if the business matches the structural patterns described there, increase skepticism regardless of apparent cheapness

---

## Change Log

- **2026-07-27** — **Amendment #15: §F.8 outcome set extended to UNRUNNABLE.** **BINDING on adoption**
  — the amendment adds a third bucket to an outcome set, and a category meaning *"we do not know"*
  cannot produce a worse answer than forcing the case into PASSED or FAILED. Derivation: Taiping
  Insurance (the P&C arm of China Taiping, 0966.HK) discloses only a **headline combined ratio
  (98.8%, −1.3pt)** with no expense/loss split, so the improvement is real but undiagnosable — it could
  be underwriting discipline, expense leverage or reserve release, three findings with three different
  persistence profiles. Recorded as **unrunnable, not failed**; improvement **excluded from fair
  value**; the disclosure gap logged as a governance datapoint. Contrast **PICC P&C (#48)**, where the
  same test **ran and failed** — materially different information that must not be conflated.
  Companion to Amendment #12 (`earnings-quality-and-distortions.md`): both hold that **the issuer's
  disclosure perimeter constrains the analysis**, and that saying so explicitly beats manufacturing a
  number to fill the gap.

- **2026-07-27** — **#11-R: third live case, and the first PASS. No rule change.** China Taiping
  (0966.HK) **cleared** the gate — g = ROE 11.5% × (1 − 0.70 payout) = **8.05%** against r = 11.0%,
  **(r − g) = +2.95pp** — where HDB and IBN both failed it. It passed **precisely because ROE is low
  and payout is high**, which is the perverse property #11-R was written to capture, now **observed
  from the passing side** rather than inferred from two failures. The rule has therefore been tested
  on both sides of the threshold and **stands as written**. Second observation, logged for future
  calibration: where **ROE ≈ r**, the mandatory fade ladder is unusually **fade-*insensitive***. CTIH's
  full ladder spanned 282% (HK$16.79–64.17), but the *defensible* rungs clustered tightly at
  **HK$25–33**, against HDB's ₹542–1,051 (94%) swing across the same rungs. Reading: **the ladder's
  informativeness scales with (ROE − r)** — printing it remains mandatory in all cases, but where
  ROE ≈ r it is *confirming* the answer rather than *choosing* it, and the analyst should say so
  rather than presenting the wide headline spread as though it were live uncertainty.

- **2026-07-26 (d)** — **Amendment #11 validated on ICICI Bank (IBN) and promoted to binding as
  #11-R.** The scheduled validation ran the same day and **confirmed the rule while proving the
  original threshold too weak.** IBN — non-merged, CASA 39%, ROE 16.0%, payout 15.5% — produced a
  **negative** justified P/B (g 13.53% ≥ r 12%), not merely a fragile one. The problem is **general
  to financials**, not specific to post-merger franchises; HDB was the milder case.

  | Change | Detail |
  |---|---|
  | **#11-R** | Binding condition rewritten from "(r − g) < 3pp" to **g ≥ r, i.e. ROE × (1 − payout) ≥ r**. Where g ≥ r the method is **VOID**, not demoted. Primary-weight ban where ROE × (1 − payout) ≥ r − 1pp. No-fade rung must be **stated as undefined** rather than omitted |
  | **#11-R(b)** | **§F.5 method table corrected** — "P/B calibrated to sustainable ROE" demoted from **Primary anchor** to **Conditional** for both insurance and banking; **residual income with explicit moat-calibrated fade** inserted as the primary anchor. This inconsistency was *created* by #11 on the same day and is fixed in the same commit |
  | **#9-R** | B-1 positive case given **two branches**. The original construction assumed a miss and was undefined on IBN, which beat. **Miss branch:** did management decline a release that would have converted it? **Beat branch:** was the beat earned or manufactured — test PAT growth against pre-provision/core operating profit growth, buffer intact. Miss branch is probative; beat branch confirmatory |

  **Why the perverse property matters:** higher ROE and lower payout are the two defining features of
  a great compounder, and **both push g up toward and past r.** Justified P/B is most reliable on
  mediocre, high-payout banks and breaks down entirely on the franchises a value investor most wants
  to own. Visible from the algebra before either deep dive — it was not run.

  **Materiality:** #11 cut base fair value **~33% on HDB and ~17% on IBN**, with negligible FX
  contribution. Not cosmetic.

  **Process note — RF-4 fired twice in one run, both times on my own arithmetic:** (i) 1bn shares =
  100 crore, not 10 → the A1 market-cap anchor first returned a 90% gap; (ii) 1 crore = 0.01bn, not
  0.1 → EPV first returned P/B 13.6×. **Both were caught by the gates and neither reached the
  report.** Absurd-output checking earned its place twice in a single session; the lesson is that
  crore/billion conversion is the highest-frequency unit trap in Indian filings and should be done
  once, explicitly, at the top of the working file.

  **Confirmation-bias control used:** the #11 hypothesis was **pre-registered in the report before
  IBN data was fetched**. The confirming input (payout 15.5%) is a reported fact rather than a
  modelling choice. Recommend adopting pre-registration as standard practice whenever a run's stated
  purpose is to validate a prior amendment.

- **2026-07-26 (c)** — **Validated against a third live deep dive** (HDFC Bank, HDB — Q1 FY27 thesis
  refresh). Amendments **#9–12** applied, continuing the #1–8 series from 2026-07-26 (b). The refresh
  downgraded HDB from BUY 8/10 to HOLD 6/10 and cut base FV from $31.23 to $21.00; three of the four
  amendments are direct outputs of root-causing that error.

  | # | Amendment | File |
  |---|---|---|
  | 9 | **§F.7 B-1 given a positive-case diagnostic** — mirrors amendment #3 (I-1). A bank that leaves a discretionary buffer unreleased through a consensus miss has demonstrated reporting integrity; the diagnostic is the **ratio of the miss to the buffer**. On HDB, 3.0% of an unreleased ~₹9,000cr buffer would have turned a ₹272cr miss into a beat. Set the verdict floor at HOLD rather than AVOID | this file |
  | 10 | **§F.2 post-merger funding-mix rule** — decompose margin compression into asset-side (CD ratio, transitional) and liability-side (CASA mix, **structural**). **Never assume a merged bank recovers to the acquirer's pre-merger NIM.** Track CASA as the deciding series | this file |
  | 11 | **Mandatory fade disclosure** — print the fade-sensitivity ladder; demote justified P/B to corroborative where **(r − g) < 3pp**. ⚠ **UNVALIDATED** — single-case derivation | `intrinsic-value.md`, §F.5 note here |
  | 12 | **Transition-break rule extended to corporate transactions** — merger/demerger/disposal breaks a series like an accounting standard does, and **the issuer's own "not comparable" statement is binding on the analysis** | `earnings-quality-and-distortions.md` |

  **What performed as designed:** the B-1 harvesting check returned a clean negative on first use and
  the positive-case extension then produced the decision-relevant finding — the same two-step that
  I-1 produced on PICC P&C. The Step 2.5 four-anchor gate passed cleanly (single share class, ADR
  1:3), and the A1-reverse test from amendment #5 correctly landed on the ADR as the listing under
  analysis.

  **What did not, and is now flagged:** amendment **#11 is provisional.** It was derived from one
  name and would retroactively demote the primary valuation method for every financial in the book
  (CMB, ICICI, Berkshire, PICC ×2, Waterdrop). **Scheduled validation: ICICI Bank (IBN)** — same
  market and sector but a *non*-merged balance sheet, which isolates whether the fade problem is
  general to financials or specific to post-merger franchises. Do not extend #11 beyond financials
  until that run completes.

  **File-hygiene defect logged:** the 2026-07-26 (b) entries reference **§F.3** and **§F.4**, but no
  such headers exist — the file runs §F.2 → §F.5 and that content sits inside §F.2. Amendment #10 was
  placed in §F.2 accordingly. Either create the headers or correct the dangling references on next
  touch; do not add more of them.

- **2026-07-26 (b)** — **Validated against two live deep dives** (PICC P&C 2328.HK; PICC Group
  1339.HK). Eight amendments applied across four files:

  | # | Amendment | File |
  |---|---|---|
  | 1 | Float cost promoted from prose to a **mandatory metrics table** in §F.3 | this file |
  | 2 | **Book-value quality caveat** added to §F.2 — BVPS is itself mark-to-market for equity-heavy insurers, so P/B struck at a market high re-imports the cyclicality that normalizing the numerator removed | this file |
  | 3 | §F.7 **I-1 given a positive-case diagnostic** — a *rising* reserve ratio is strengthening and acts as a credibility multiplier on every other underwriting number, not merely the absence of harvesting | this file |
  | 4 | §F.5 notes that **P/B and EPV are not independent** (they converge as normalized ROE → r); count them as one method in the probability weighting | this file |
  | 5 | **Step 2.5 Anchor 1 must run in reverse** (market cap ÷ share count → implied price, matched to the listing under analysis) — catches dual-listing *price-basis* errors that the forward test passes | `SKILL.md`, `data-sources.md` |
  | 6 | **Duplicate-exposure test** added to SOTP Method 6 — above ~80% stake concentration, holdco-vs-subsidiary replaces holdco-vs-NAV as the deciding comparison | `intrinsic-value.md` |
  | 7 | §F.3 requires **PV of loss-making (onerous) new contracts** and channel mix for life — NBV growth alone actively misled (sector's fastest NBV belonged to its worst new business) | this file |
  | 8 | **Parent + listed subsidiary = one exposure** for concentration caps; combined cap is the subsidiary's, never the sum | `intrinsic-value.md`, `SKILL.md` |

  Two open questions **resolved**: the pre-2023 insurance series is unusable (comparable window is
  four years, not ten — a ten-year table is impossible for any HK/mainland insurer), and
  comprehensive solvency is always > core.

  What performed as designed and needed no change: the §F.2 metric substitutions, the §F.8 signature
  test (which returned a clean, decision-relevant negative on its first use), the I-3 transition
  break, and the §F.9 data-source routing.

- **2026-07-26 (a)** — File created. Resolves the dangling `references/industry-playbooks.md` reference in
  SKILL.md Step 5. §F Financials written, covering insurance and banking, adapted from an external
  insurance sector draft. Changes from that source: scope widened from insurance-only to all
  financials (the existing book holds two banks that hit the identical misfires); proposed earnings
  quality Classes 9–11 renumbered to I-1/I-2/I-3 to avoid collision with the `process-lessons.md`
  error-class series, and made binary gating flags rather than scored dimensions so the /40 composite
  stays comparable across the book; screener Q5/Q6 substitutions added (the source asserted the
  screener applied unchanged, which contradicted its own deletion of cash-conversion logic); banking
  metrics and class B-1 added; data-source block added; the IFRS 17 rule generalized into
  `earnings-quality-and-distortions.md` with I-3 retained as the sector instance; the underlying
  directional thesis and its candidate shortlist deliberately excluded from Project Knowledge.

- **Pre-2026-07** — Original ten-sector playbook (Insurance, Banking, Consumer Brands & Retail, Media
  & Publishing, Energy & Utilities, Railways, Technology, Industries to Avoid, HK/China notes).
  Retained in full; the §F financials block was added alongside it, not in place of it.
