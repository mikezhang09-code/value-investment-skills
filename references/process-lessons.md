# Process Lessons — Self-Improvement Reference

> A compact reference for analytical errors and how to prevent them. Update this file when new errors are discovered. Read this before starting a new deep dive on any HK / China / India / dual-listed equity.

---

## Most Expensive Error Classes

Errors fall into three families:
- **Mechanical errors** (Classes 1-5): Wrong inputs. Catastrophic but visible — they break things obviously.
- **Interpretive errors** (Classes 6-11): Right inputs, wrong meaning. Subtle but cumulative — they corrupt conclusions silently.
- **Omission errors** (Class 12): Inputs never gathered at all. The most dangerous family, because there is nothing to check — an omitted asset produces a fully self-consistent model built on the wrong number, and no reconciliation complains.

Each family needs a separate defense. Mechanical errors are stopped at Step 2.5 (reconciliation gate). Interpretive errors are stopped at Step 3.5 (earnings quality gate). **Omission errors are stopped only by a positive sweep — Check 15 — because they leave no trace to detect.**

---

### MECHANICAL ERROR CLASSES (data correctness)

### 1. Wrong Share Count (Highest-Impact Single-Point-of-Failure)
**Family:** Mechanical
**Frequency:** Common, especially for dual-listed Chinese companies (H+A), US dual-class (GOOG/GOOGL), and post-equity-raise scenarios.

**Cost:** Catastrophic — every per-share metric is wrong, every IV is wrong, the verdict is wrong.

**Prevention:** Mandatory 4-anchor reconciliation in SKILL.md Step 2.5. Always EPS back-check before any per-share calculation.

**Case study:** BYD May 2026 — used 3.04B shares vs. actual 9.085B (3x off). Caught only when user provided market cap. Required full report rewrite.

---

### 2. Currency / Scale Confusion
**Family:** Mechanical
**Frequency:** Moderate, especially in HK markets (HKD vs CNY vs USD).

**Cost:** Outputs systematically off by 10-50%.

**Prevention:** Always state currency explicitly. Cross-check published market cap in user's preferred currency.

**Common HK conversion:** 1 HKD ≈ 0.92 CNY ≈ 0.128 USD.

---

### 3. Mixed Data Vintage
**Includes the cum/ex-dividend leg (added 2026-07-27).** A stale price is not only stale — if an
ex-dividend date has passed since the quote, the number is also *cum-dividend* and not comparable to
today's screen. Two errors compound in the same direction, and on a high-payout name the dividend
leg alone can be verdict-relevant. See Check 12.

**Family:** Mechanical
**Frequency:** Common — blending annual actuals with quarterly run-rates without labeling.

**Cost:** Inconsistent base, misleading trends, confused multipliers.

**Prevention:** Label vintage per line. Annual and quarterly figures never silently mixed.

---

### 4. Wrong Share Class as Total
**Family:** Mechanical
**Frequency:** Specific to dual-listed Chinese, US dual-class, recently placed stocks.

**Cost:** 2-10x understatement of total shares.

**Prevention:** Sum all classes explicitly. Document each source. See Quick Reference: Share-Class Trap Cheat Sheet below.

---

### 5. Reconciliation Failure Bypass
**Family:** Mechanical
**Frequency:** When analyst skips Step 2.5 gate to "save time."

**Cost:** Variable but propagates everywhere downstream.

**Prevention:** Treat Step 2.5 as non-negotiable, not optional. Five minutes saved upstream can cost a full report rewrite downstream.

---

### INTERPRETIVE ERROR CLASSES (data meaning)

### 6. One-Time Items Treated as Recurring
**Family:** Interpretive
**Frequency:** Very common — especially for Chinese industrials (subsidies), HK conglomerates (asset disposals), cyclicals near peak.

**Cost:** Earnings overstated 10-30%; valuation correspondingly inflated.

**Prevention:** Step 3.5 normalized earnings bridge. Show reported → normalized explicitly.

**Asymmetric trap:** Management highlights one-time costs aggressively but quietly includes one-time gains. The analyst must independently identify both directions.

---

### 7. Aggregate Growth Mistaken for Per-Share Growth
**Family:** Interpretive
**Frequency:** Very common — Chinese tech, EV, biotech, recent IPOs.

**Cost:** Investment looks like a compounder but isn't for existing shareholders.

**Prevention:** Step 3.5 per-share scorecard. Always present both aggregate and per-share CAGR.

**Mental model:** Revenue grew 100% over 5 years but shares grew 100% too → per-share growth is 0% → no value created for owners.

---

### 8. Investment Portfolio Income Treated as Operating
**Family:** Interpretive
**Frequency:** Critical for HK conglomerates, insurance, holding companies, industrial with strategic stakes.

**Cost:** Operating quality misjudged; SOTP not applied when it should be; reported NI volatility mistaken for business volatility.

**Prevention:** Step 3.5 — separate operating and investing returns. Apply SOTP for holding companies.

**Case studies:** Fosun (headline loss dominated by mark-to-market, operations healthier); Tencent (investment portfolio is 20%+ of value but reported income line is noisy).

---

### 9. Goodwill / Acquired Growth Mistaken for Organic
**Family:** Interpretive
**Frequency:** Common — serial acquirers, M&A-led growth stories, post-IPO consolidators.

**Cost:** Moat assessment wrong (you can't "buy" a moat at peer multiples and create value).

**Prevention:** Step 3.5 — separate organic from acquired growth. Compute ROIC ex-goodwill.

**Tell-tale:** Goodwill > 50% of total assets; acquisitions every year; ROIC reported looks fine but ROIC ex-goodwill is mediocre.

---

### 10. Off-Balance-Sheet Obligations Ignored
**Family:** Interpretive
**Frequency:** Common — pension legacy, JV guarantees, VIE structures, factored receivables, operating leases.

**Cost:** True leverage understated; financial flexibility overstated; downside risk mismeasured.

**Prevention:** Step 3.5 — compute true net debt including pensions, leases, guarantees, JV proportionate debt.


### 11. Convertible / Hybrid Conversion Misread
**Family:** Interpretive
**Frequency:** Common — HK/China names financed via convertible bonds or convertible preferreds; warrant-heavy US names; post-restructuring capital stacks.

**Cost:** Two opposite failure modes. (a) **Missed live instrument** — a convertible/preferred not yet in the basic count is ignored → forward dilution understated, IV overstated. (b) **Misread completed conversion** — a convert that has already converted is mistaken for chronic dilution → conviction wrongly cut, or a flat basic EPS misread as an earnings problem.

**Prevention:** At Step 2.5/3.5, inventory every convertible bond, convertible preferred, and warrant. For each: (1) run the **if-converted test** — compute the fully-diluted share count and per-share IV; if overhang > 5%, value on a fully-diluted basis. (2) Check whether a conversion occurred **within the comparison window**. A completed conversion is a *one-time basic-share step-up, not recurring dilution* — anchor on diluted / fully-diluted per-share metrics, and judge the **value transfer separately** (conversion price vs IV at conversion; converting below IV is a one-off transfer to bondholders, usually small).

**Conversion-in-transit tells:** convertible-interest line drops to zero; weighted-average **basic** shares jump while **diluted** barely moves; the diluted-EPS note drops its prior-year convertible add-back (interest + assumed conversion).

**Case study:** Bosideng (3998.HK) H1 FY26 — profit attributable +5.3% but **basic EPS flat** (diluted +1.5%), driven by the US$275M 1% CB due 2024 converting into ~560M shares at HK$3.83 between the comparison periods. One-time; convert interest fell RMB 36.6M → 0; the diluted-EPS note dropped its convert add-back. Overhang now cleared; mild value transfer (converted below ~HK$5 IV). The trap was over-penalizing it as chronic dilution; correct read was a cleared one-off.

---

### OMISSION ERROR CLASSES (data never gathered)

### 12. Balance-Sheet Value Omitted Because It Never Touches Operating Profit
**Family:** Mechanical (omission) — with an Interpretive second stage
**Frequency:** Any issuer where non-operating assets are a material share of market cap: China internet, HK conglomerates, insurance, holdcos, cash-rich compounders. Class 8 covers portfolio *income* misread as operating; **this class covers the portfolio itself never being counted at all.**

**Cost:** The most expensive error class discovered to date *by mechanism*, because it is silent. A wrong share count fails Anchor 1 and announces itself. An omitted asset produces a fully self-consistent DCF, EPV and peer comparison that are simply built on the wrong denominator of value. Nothing in the model complains.

**The three-stage failure, all three of which occurred on TME:**

```
STAGE 1  OMITTED       Asset never enters the valuation at all.
                       (v1: RMB 22.8bn / US$3.3bn portfolio = ~23% of
                        market cap, valued at zero across DCF/EPV/peer)

STAGE 2  GUESSED       Omission caught, but the annual report is not read.
                       A placeholder discount is invented to cover the
                       unknown — and the guess embeds its own thesis.
                       (v2: "opaque Tencent-affiliated private holdings"
                        → punitive 20% haircut)

STAGE 3  READ          The filing dissolves the guess. On TME every one of
                       the four stated grounds for the haircut was false:
                       the holdings are Spotify + Universal + Warner, all
                       exchange-listed, all liquid, and 100% held offshore
                       outside PRC capital controls. Discount 20% → 0-10%.
```

**Prevention — the Step 2.5 upgrade (see Check 15).** Step 2.5 was written as a *share-count* reconciliation. That is the denominator of per-share value; this class attacks the numerator. Both halves must be swept: **every balance-sheet line that carries equity value but never passes through operating profit must be listed and valued explicitly, or explicitly written to zero with a stated reason.**

**Prevention — the second-stage rule.** Where the composition of a material line is unknown, a discount is *not* a substitute for reading the filing. A guessed haircut feels conservative and is not: it is an unexamined thesis carrying the same weight as a researched one, and on TME it happened to be wrong in the favourable direction — which is simply the other way to be wrong.

**Directional warning:** correcting this class is not automatically bullish. The same sweep that added US$3.3bn of portfolio to TME also surfaced an **unrecognised withholding liability of RMB 1,725mn** on undistributed PRC profits that v1 and v2 had both missed. Sweep the liability side with the same discipline; the point is completeness, not a better answer.

**Case study:** Tencent Music (TME) v1 → v3, 2026-05-13 → 2026-08-11. Portfolio omitted entirely in v1; discounted on a guess in v2; decoded in v3 from the 20-F (Spotify + UMG + WMG). Book value per ADS had also never been computed across either prior version — **P/B 1.27×, book alone covering 76% of market cap**, a hard floor that went unrecorded for three months. Related: Tencent (#1) is flagged under Class 8 for the same portfolio being *noisy in the income statement*; TME is the case where it was *missing from the balance sheet*. One asset class, two distinct failure modes.

---

## Most Useful Sanity Checks

### Mechanical Checks (Step 2.5)

### Check 1: Market Cap Reconciliation (30 seconds)
```
My shares × my price ≈ published market cap?
If gap > 5% → STOP, investigate.
```

### Check 2: EPS Back-Check (10 seconds)
```
(Reported NI − perpetual/AT1/preference distribution) ÷ Reported EPS = my share count?
If gap > 2% → STOP, share count is wrong.

⚠️ FIRST run the classification gate (added 2026-07-27, sweep-validated).
   EQUITY-classified  -> trap live, subtract the distribution.
   LIABILITY-classified -> NO TRAP, coupon already in interest expense.
   Indian bank AT1 and mainland capital supplementary bonds are LIABILITIES.
   HK/PRC insurer perpetual capital securities are EQUITY.
   The instrument's NAME tells you nothing; its CLASSIFICATION tells you all.

⚠️ ALWAYS state resolution: ±(0.5 x 10^-dp) / EPS.
   A gap below resolution is rounding, NOT a finding.
   EPS 2dp on a ~1.00 base resolves only ~±0.5% -> "no distortion above 1%",
   never "no distortion". China Taiping was catchable because its 3.83% gap
   was ~550x the resolution of a 3dp EPS on a HK$7.25 base.

Signature: Anchor 2 off by 1–5% while the dividend-derived and BVPS-derived
counts agree with EACH OTHER to <0.1% → look for a senior distribution in
the statement of changes in equity, not for a share-class problem.
```

### Check 3: Currency Self-Consistency (10 seconds)
```
All figures in same currency? Conversion rates documented?
Per-share metrics in same currency as price?
```

### Interpretive Checks (Step 3.5)

### Check 4: Normalized vs. Reported NI Gap (1 minute)
```
What's in this year's NI that isn't normal?
  Big asset sale? Tax benefit? Subsidy spike? FV remeasurement gain?
  Restructuring? Impairment? Litigation? COVID charge?
Compute normalized NI and compare to reported.
If gap > 25% → use normalized for everything downstream.
```

### Check 5: Per-Share Growth vs. Aggregate Growth (2 minutes)
```
10-yr revenue growth: X%
10-yr revenue PER SHARE growth: Y%
Drag: X−Y

Same for NI, equity, FCF.
If drag > 3% annually → dilution is destroying significant value.
```

### Check 6: Operating vs. Investment Income Split (2 minutes)
```
What % of NI comes from:
  Core operations?
  Investment income (interest, dividends)?
  Fair-value gains/losses on investments?
  Asset disposals?

If operating < 70% of NI → not a normal operating business.
Holding company SOTP framework needed.
```

### Output-Stage Checks (Step 6.5)

### Check 7: "Too Good to Be True" Test (1 minute)
```
Is my conclusion that a heavily-covered mega-cap is 40%+ mispriced?
If yes → verify all inputs before publishing.
```

### Check 8: Reverse DCF (5 minutes)
```
What growth rate does the market price imply?
If extreme (<0% or >25%), my model or the market is wrong.
Usually it's my model.
```

### Check 9: Peer Multiple Cross-Check (3 minutes)
```
P/E vs peer median: subject / peer = ratio
If ratio < 0.5 or > 2.0 → why? Is my fair value implausible vs. peers?
```

### Check 10: Single-Input Sensitivity (5 minutes)
```
If I change [share count / growth rate / discount rate / 
 normalized NI / dilution assumption] by 20%, does verdict change?
If yes → conclusion is fragile, verify the key input.
```


### Check 11: Convertible / Hybrid Scan (1 minute)
```
Any convertible bonds, convertible preferreds, or warrants — now OR in the comparison window?
  FORWARD:  compute fully-diluted share count; if overhang > 5% → value fully-diluted.
  IN-TRANSIT: did one convert this period?
     Tells = convert-interest line → 0; basic shares jump while diluted flat;
             diluted-EPS note drops its convertible add-back.
  IF CONVERTED → one-time step-up, NOT chronic dilution. Anchor on diluted.
                 Assess conversion price vs IV (value transfer). Mark overhang cleared.
```

---

### Check 12: Price Vintage and Ex-Dividend (30 seconds)
```
1. What DATE is my price? Is it stated in the report?
2. Has an EX-DIVIDEND date passed between that date and today?
3. If yes → the quote is CUM-dividend and the comparable price is lower.
```
Staleness alone has now bitten twice (sportswear v1/v2; PICC P&C). The dividend leg is the
newer half: on China Taiping a HK$1.23 ex-div step moved margin of safety **15.0% → 20.0%** on
no news whatsoever — a third of the way to the entry threshold. For high-payout financials the
step-down is verdict-relevant by itself. **Confirm both legs before finalizing any verdict.**

### Check 13: Record-Keeping Assertion (10 seconds)

Prose is not validated. Data is. Anything stated in a header, a title or a summary line drifts
silently because no check touches it.

```
assert header_universe_size == len(json_data) == master_table_row_count
```

*Derivation, 2026-07-27.* The command centre header read **46** while the JSON block already held
**49** contiguous entries — stale across roughly three sessions. The definitive cross-file
parsed-dict equality check passed perfectly and caught nothing, because **agreement between the two
checked artifacts said nothing about the unchecked third.** Generalize: when adding a validation,
ask what the check *cannot* see, and whether anything downstream is relying on it anyway.

### Check 14: Is the Book-Value Denominator Real? (60 seconds)

Where a valuation rests on P/B, the denominator deserves the same scrutiny as the numerator.
Three failure modes, all found live in the 2026-07-27 sweep, none of them the one being hunted:

```
1. DERIVED, NOT READ   Was BVPS taken off a balance sheet, or backed out of ROE?
                       (PICC P&C: RMB13.34 reverse-engineered from a ratio)
2. GAAP-BASIS UNNAMED  Does the issuer publish more than one equity figure?
                       (ICICI 20-F: US GAAP Rs409,093cr vs Indian GAAP
                        Rs363,060cr — a 12.7% gap on the same page)
3. SINGLE-SOURCED      One aggregator, never tied to a filing?
                       (ICICI BVPS Rs527 — sits BETWEEN the two bases above)
```

**Name the basis, name the source, and read it to a filing.** A denominator that cannot survive
those three questions makes every multiple built on it decorative.

### Check 15: Full Balance-Sheet Sweep (Step 2.5 extension, 3 minutes)

Step 2.5 reconciles the **share count** — the denominator of per-share value. This check reconciles
the **numerator**. Run it on any issuer where non-operating assets could plausibly exceed ~10% of
market cap; run it always on internet, insurance, conglomerate and holdco structures.

Walk the balance sheet and list every line that **carries equity value but never passes through
operating profit**:

```
[ ] Cash, term deposits, short-term investments   ... and WHERE they sit (Check 16)
[ ] Financial assets at FVOCI / FVTPL             ... COMPOSITION, not just the total
[ ] Investments in associates (equity method)
[ ] Other investments / long-term financial assets
[ ] Investment property, non-core land, surplus assets
[ ] Deferred tax assets of realistic value
[ ] ---- and the LIABILITY side, same discipline ----
[ ] Unrecognised withholding tax on undistributed profits
[ ] Off-balance-sheet obligations (Class 10)
[ ] Minimum guarantees / take-or-pay commitments
[ ] Pension deficits, contingent consideration
```

**Every line is either valued explicitly or written to zero with a stated reason.** Silence is the
failure mode: an omitted asset does not raise an error, it produces a coherent model built on the
wrong number. Where a line's composition is unknown, that is a signal to run **Check 17**, not a
licence to apply a placeholder discount.

**Case:** TME v1 omitted a US$3.3bn portfolio (~23% of market cap) across three valuation methods
simultaneously; the same sweep that found it also found an unrecognised RMB1,725mn withholding
liability. Assets and liabilities both, or the sweep is just a bull case with extra steps.

### Check 16: Where Does the Cash Actually Sit? (60 seconds)

Cash is routinely treated as one number at face value. For China-domiciled, VIE-structured and
emerging-market issuers it is at least two numbers, and the difference is real money.

```
OFFSHORE   parent + non-PRC subsidiaries → distributable now, no withholding
ONSHORE    WOFEs + VIEs                  → 10% withholding to repatriate
                                            (5% via a qualifying HK holdco)
```

Most 20-Fs and HK annual reports disclose this in the **condensed consolidating schedule** filed
for VIE issuers — the same table that gives the VIE revenue and asset percentages. Read the split,
then check it against buyback and dividend capacity: **a company can be cash-rich and still unable
to fund a buyback without a tax event.**

**Case:** TME FY25 — RMB38,043mn total splits offshore RMB13,609mn (36%) vs onshore RMB24,434mn
(64%). The Q2 FY26 US$400mn buyback was executed out of the offshore pocket, so the capacity to
continue is a function of the *offshore* balance, not the headline. The matching liability —
RMB1,725mn of unrecognised withholding on RMB17,247mn of undistributed PRC profits — is disclosed
a few pages earlier in the same filing and was missed twice before it was read.

### Check 17: Read the Same Note Across Successive Annual Reports (5 minutes)

**The single highest-yield technique found this cycle, and it is nearly free.**

When a line item's composition is opaque in the current filing, do not discount it and do not guess
at it. Pull the **same note number from three to seven prior annual reports and read them in
sequence.** Issuers describe a holding in full when it is first acquired and grow terse as it
becomes routine — so the disclosure that is missing today usually exists in the year the position
was opened.

```
TME — Note 18(a), "Financial assets at FVOCI", read across seven 20-Fs:

FY2018-19   "SOLELY represented its equity investment in SPOTIFY"
FY2020      + subscribed ~0.78% of WARNER MUSIC GROUP at IPO for US$100mn
FY2021-22   "mainly Spotify and WMG"
FY2025      + UMG 2% by distribution-in-kind (the RMB2.37bn deemed-disposal gain)

→ Portfolio = Spotify + Universal + Warner. All exchange-listed. All liquid.
  A black box that a single filing left shut, opened by three filings in sequence.
```

**Second use — verify the marks are honest.** A time series of the line tested against the
underlying's share price tells you whether management marks in both directions. TME's FVOCI ran
RMB9,771mn (2020) → **3,168mn (2022, as SPOT fell 66%)** → 14,498mn (2024) → 26,231mn (FY25) →
19,866mn (Q1 FY26). It falls when it should. That is worth more than an assurance in the MD&A.

**Third use — reconstruct history the issuer has stopped disclosing.** Where a metric is
discontinued mid-life (TME dropped quarterly MAU/ARPPU from Q1 FY26), the historical series still
exists in prior filings and can anchor a trend even after the current disclosure goes dark.

**Applies to any issuer with a filing history.** Cost is minutes; it dissolved the largest open
unknown in the book.

## Process Behaviors to Reinforce

### Quarterly filings cannot support a deep dive — they have no notes

A quarterly release carries the three statements and little else. **The notes are where composition
lives**, and composition is where the errors hide. Everything below requires the annual report
(20-F, HK annual report, A-share 年报) and cannot be answered from a quarterly:

```
Investment / FVOCI composition        Related-party terms and pricing
Share-class structure and voting      Undistributed profits and withholding
Entity-level cash location            Segment detail below the headline split
Content / minimum-guarantee commitments   Purchase price allocation on acquisitions
```

**Rule:** a "full deep dive" label requires at least one annual report in the source trail. Working
from quarterlies alone produces at best an *earnings-reaction* note, and the honest move is to say
so and name the gaps rather than to let the deliverable's title overstate its foundation.

**Cost when ignored:** TME v1 and v2 were both built on quarterly releases. v1 omitted a US$3.3bn
portfolio; v2 caught the omission but, still without the 20-F, replaced it with a guess. The single
20-F read in v3 closed **twelve** open items at once — portfolio composition, entity-level cash,
withholding liability, share-class structure, VIE quantification, book value, three-year audited
trajectory, goodwill baseline, and more. One filing, three months late.

**Corollary — state the tier before starting, not after.** When the person asks for a deep dive and
only quarterlies are in hand, say which questions can be answered now, which need the annual report,
and offer to fetch it. That conversation costs one message and prevents a mislabelled deliverable.

### Validate new rules by sweeping backwards, not by waiting forwards

When a rule is derived from a single case, the instinct is to mark it unvalidated and wait for the
next name that triggers it. **Sweep the existing book instead.** The retrospective run is faster,
it is bounded (the population is known), and it tests the rule against more variation than any
single future case will.

*Derivation, 2026-07-27.* Amendment #13 was adopted with "validates on the next issuer carrying
perpetual or AT1 capital." Sweeping the seven financials already in coverage instead produced,
within hours: (1) **two defects in the rule itself** — no classification gate, no resolution
statement — either of which would have generated false findings for months; (2) confirmation that
**no existing entry was corrupted**; and (3) a **larger, unrelated error** on ICICI's P/B
denominator that no #13-triggered future case would ever have surfaced.

The general form: **a rule derived from one case encodes that case's peculiarities as though they
were general.** Only contact with the rest of the population separates the two, and that population
is already sitting in the book.


### Pre-Analysis
- [ ] State share count explicitly at top of analysis
- [ ] Document source for share count (annual report, EPS back-check, etc.)
- [ ] Identify share-class structure (single-class, dual-class, dual-listed, ADR)
- [ ] Inventory hybrid/convertible instruments (convertible bonds, convertible preferreds, warrants); note any conversion within the comparison window

### During Analysis
- [ ] Run all four reconciliation anchors before any per-share calculation
- [ ] Use reported per-share metrics (EPS, BV/share, DPS) as ground truth
- [ ] Document each major valuation input with source

### Post-Analysis
- [ ] Apply 4 plausibility checks before publishing
- [ ] Cross-check against analyst consensus — explain divergence
- [ ] Include reconciliation table in "Sources & Data Trail"

### When Challenged
- [ ] First response: "Let me verify" (NOT defensive elaboration)
- [ ] Treat user-provided data as priority verification trigger
- [ ] When error confirmed: acknowledge → root-cause → rebuild → supersede prior

---

## Interpretive Error Recognition Patterns

Unlike mechanical errors (which fail loudly via reconciliation), interpretive errors fail quietly. Train pattern recognition for these specific tell-tales:

### Pattern: "It's growing fast but per-share economics are flat"
**Trigger:** Revenue grew at 15% CAGR but EPS grew at 6% over 10 years
**Diagnosis:** Heavy dilution — frequent equity issuances or M&A paid in stock
**Response:** Capital allocation history audit. Was equity issued above or below IV?

### Pattern: "The reported earnings look great this year"
**Trigger:** YoY earnings spike of 30%+ with no obvious operational reason
**Diagnosis:** Likely one-time gain — asset disposal, FV remeasurement, tax benefit, subsidy
**Response:** Read income statement bottom-up. Identify the source of the spike. Normalize.

### Pattern: "ROIC looks fine but operating margins are mediocre"
**Trigger:** Reported ROIC 12% but operating margins 5%
**Diagnosis:** Asset turnover doing the heavy lifting, OR investment income inflating numerator
**Response:** Decompose ROIC into operating ROIC and contribution from investments.

### Pattern: "Cash conversion is below earnings consistently"
**Trigger:** OCF / NI < 0.8 for 3+ years
**Diagnosis:** Earnings quality issue — working capital building, aggressive accruals
**Response:** Working capital trend analysis (Class 4 in Step 3.5).

### Pattern: "The market cap is far below what the parts obviously add to"
**Trigger:** Headline P/E looks merely cheap, but cash + investments + a recently acquired subsidiary approach or exceed half of market cap
**Diagnosis:** Either (a) the non-operating assets are being ignored by the market — a real opportunity; or (b) *you* are about to ignore them, which is Class 12. Run the inversion before deciding which.
**Response:** Strip the balance sheet from the market cap layer by layer and read what is left for the operating business alone, then test that residual against a reverse DCF. TME: US$14.95bn less net cash US$5.67bn less portfolio US$2.84bn less Ximalaya at cost US$2.40bn leaves **US$4.04bn against ~US$1.48bn of TTM earnings = 2.7×**, implying ~−8%/yr in perpetuity for a segment growing +11%. The two statements cannot both be true, and the gap is the margin of safety. Note the asymmetry: this pattern is also how a *value trap* presents, so the residual multiple must be paired with evidence the core is not actually shrinking.

### Pattern: "An acquisition closed mid-quarter and the growth still looks weak"
**Trigger:** A material acquisition consolidates, yet reported revenue growth barely moves — prompting "did the prior-year base get restated?"
**Diagnosis:** Under IFRS 3 (and ASC 805) consolidation is **prospective**: the comparison base contains none of the acquired entity, so the contribution is purely additive and the base was *not* inflated. Weak growth despite the deal means (a) partial-period consolidation, (b) the target is smaller than assumed, or (c) an offsetting decline elsewhere — usually more than one.
**Response:** Build the bridge in absolute currency, not percentages, and count the **days consolidated**. TME Q2 FY26: deal closed 18-May so only 44 of 91 days (48%) consolidated, contributing RMB407mn; organic music-related added ~RMB380mn; **social entertainment subtracted RMB260mn** — netting to +RMB490mn, +5.8%. Pro-forma a full quarter the print is ~+11.0%. Then compute what the *first full quarter* must show and pre-commit it as the validation quarter (TME: Q3 FY26 must print >+12%, and below that the composition explanation is falsified).

### Pattern: "Operating earnings are stable but reported NI swings wildly"
**Trigger:** Operating profit 800-1000 range; reported NI 200-1800 range
**Diagnosis:** Investment portfolio mark-to-market dominating reported NI
**Response:** Separate operating from investing. Likely needs SOTP valuation (Class 3).

### Pattern: "Growth came almost entirely from acquisitions"
**Trigger:** 5-year revenue CAGR 12%, but acquisitions contributed 9% of that
**Diagnosis:** Organic growth is only 3% — moat may be weaker than reported growth suggests
**Response:** Compute organic-only growth and operating margins (Class 8).

### Pattern: "Non-GAAP earnings are way higher than GAAP"
**Trigger:** Adjusted EPS $5.00; GAAP EPS $1.50
**Diagnosis:** Either (a) genuinely non-recurring items (acceptable) or (b) SBC and amortization add-backs (suspect)
**Response:** Reconcile each adjustment. SBC is real expense.

### Pattern: "Strong dividends in HK but tiny EPS coverage"
**Trigger:** DPS 0.50, EPS 0.45, payout > 100%
**Diagnosis:** Dividend funded by debt, asset sales, or capital reduction — unsustainable
**Response:** Check dividend coverage from FCF (not earnings) over 5+ years.

### Pattern: "Big asset disposal in cash flow but no gain in NI"
**Trigger:** Sold subsidiary or property for $X, but NI didn't move
**Diagnosis:** Sold at or below book value — could be value-destructive or could be intelligent capital recycling
**Response:** Compare disposal price to book value and to market comparables.

### Pattern: "Promoter holding declining over time" (India)
**Trigger:** Indian company; promoter stake fell from 65% to 45% over 5 years
**Diagnosis:** Either dilution from QIPs, sales by promoter (often distress), or pledged shares sold
**Response:** Check pledging status, equity issuance history, and any forced sales.

---

## Quick Reference: Share-Class Trap Cheat Sheet

### HK + China Dual-Listed (H + A)
**Symptom:** HK source shows ~1B shares; total company is much larger.
**Fix:** Total = H-shares + A-shares. Check annual report "Composition of Share Capital."

### US Dual-Class
**Symptom:** GOOGL share count alone (~5.8B) understates Alphabet (~12.5B total A+B+C).
**Fix:** Sum all classes.

### Indian Dual-Listed (NSE + BSE)
**Symptom:** Looks like 2x the shares.
**Fix:** Same shares on both exchanges. Don't double-count.

### Chinese ADRs
**Symptom:** ADR EPS differs from ordinary EPS by ratio (e.g., 8x for BABA).
**Fix:** Convert to ordinary basis OR work entirely in ADR basis. Don't mix.

### Recently Diluted (Post-Placement)
**Symptom:** Old share count from prior annual report.
**Fix:** Use most recent quarterly or post-placement count.

---

## "Always Verify" Companies

For these companies (and structurally similar ones), always run extra share-count verification:

**HK-listed Chinese with H+A structure:**
- BYD (1211.HK), Tencent (700.HK, no A), Ping An (2318.HK), China Mobile (941.HK)
- All major Chinese banks listed in HK (1398, 939, 1288, 3328, 3968)
- All major Chinese energy SOEs (857, 386, 883, 2883)
- All major Chinese insurance (2318, 2628, 1336, 2378)

**US Dual-Class:**
- Alphabet, Meta, Snap, Berkshire, Visa
- Most recent tech IPOs (Airbnb, DoorDash, etc.)

**Frequently-Placed Stocks (recent dilution risk):**
- Chinese EV/tech names (BYD, NIO, XPeng, Li Auto)
- High-growth biotech
- SPAC merger products

**Non-Operating-Asset Heavy (run Check 15 — the balance sheet is a material part of the thesis):**
- Tencent (700.HK), Tencent Music (TME) — listed-equity portfolios; **note these two are not independent: Tencent is TME's controlling shareholder and holds the balance of the same Spotify position**
- HK conglomerates and holdcos (Fosun, CKH, Jardine-type structures)
- Insurance (investment book routinely exceeds underwriting profit — Class 3/8 as well)
- Cash-rich compounders where net cash exceeds ~25% of market cap (PDD, Trip.com, TME)
- Any issuer whose FVOCI, associates or term-deposit lines move by >10% of market cap year to year

---

## When in Doubt: Three Anchors

If you have only 60 seconds to verify share count:

1. **EPS back-check:** Net income ÷ EPS = shares.
2. **Market cap arithmetic:** Published mcap ÷ price = shares.
3. **Source agreement:** Do 2+ major sources report the same count?

If all three agree, you're safe. If they disagree, dig deeper.

---

## Update Log

| Date | Lesson Added | Trigger |
|------|--------------|---------|
| 2026-05-18 | Share count reconciliation (BYD case) | User caught wrong market cap on BYD deep dive |
| 2026-05-23 | Interpretive error framework (8 distortion classes) | User identified gap: one-time items, dilution, investment portfolios not systematically addressed |
| 2026-07-27 | Check 12 — price vintage + ex-dividend leg | China Taiping: price 6.5 weeks stale AND cum-dividend; the HK$1.23 ex-div step alone moved MoS 15.0% → 20.0% |
| 2026-07-27 | Check 13 — record-keeping assertion (header == data == table) | Command-centre header read 46 against 49 live entries; cross-file equality passed and caught nothing, because both checked artifacts agreed with each other |
| 2026-07-27 | Check 2 extended — senior-instrument subtraction (amendment #13) | China Taiping: perpetual distribution omitted from Anchor 2 numerator overstated share count 3.83%; EVPS overstated 7.6% |
| 2026-07-27 (b) | Check 2 extended again — classification gate + resolution statement | #13 sweep: HDB and IBN both carry AT1 and neither produced the trap (liability-classified); PICC Group's +0.47% gap proved indistinguishable from EPS rounding at ±0.48% resolution |
| 2026-07-27 (b) | Check 14 — is the book-value denominator real? | The #13 sweep found three weak P/B denominators, none weak for the reason #13 predicted: derived-not-read, GAAP-basis unnamed, single-sourced |
| 2026-07-27 (b) | **Run a new rule's validation as a retrospective sweep, not as a wait** | #13 was adopted with "validates on the next issuer carrying perpetual capital". Sweeping the existing book instead surfaced two defects in the rule within hours, and a larger unrelated error (ICICI, 12.7%) on the way |
| 2026-08-11 | **Error Class 12 — balance-sheet value omitted because it never touches operating profit** | TME v1 valued cash + operating business by DCF/EPV/peer and omitted the entire investment portfolio: RMB22.8bn / US$3.3bn, **~23% of market cap**, at zero across all three methods simultaneously. Nothing in the model complained — an omitted asset is silent where a wrong share count fails Anchor 1 loudly |
| 2026-08-11 | **Check 15 — full balance-sheet sweep (Step 2.5 extension to the numerator)** | Step 2.5 reconciled the share count (denominator) and had no counterpart for the numerator. Assets **and liabilities** both: the sweep that added US$3.3bn of portfolio also surfaced an unrecognised RMB1,725mn withholding liability missed in v1 and v2 |
| 2026-08-11 | **Check 16 — where does the cash actually sit?** | TME FY25 cash splits offshore RMB13,609mn (36%, distributable now) vs onshore RMB24,434mn (64%, 10% withholding to repatriate). The Q2 US$400mn buyback ran off the offshore pocket, so continuation capacity is a function of that balance, not the headline. Disclosed in the VIE condensed consolidating schedule |
| 2026-08-11 | **Check 17 — read the same note across successive annual reports** | **Highest-yield technique of the cycle and nearly free.** TME Note 18(a) across seven 20-Fs: FY2018-19 "solely Spotify" → FY2020 adds WMG 0.78% at IPO → FY2025 adds UMG 2%. A black box one filing left shut, opened by three in sequence — and the same series proved the marks are honest (FVOCI fell 68% in 2022 as SPOT fell 66%) |
| 2026-08-11 | **A guessed discount is not a conservative substitute for reading the filing** | TME v2 caught the v1 omission but, still working from quarterlies, invented "opaque Tencent-affiliated private holdings" and applied a 20% haircut. All four grounds were false — the holdings are Spotify/UMG/WMG, exchange-listed, liquid, held 100% offshore. The guess carried the same weight as research and happened to be wrong in the favourable direction, which is simply the other way to be wrong |
| 2026-08-11 | **Quarterly filings cannot support a deep dive — they have no notes** | TME v1 and v2 were both built on quarterly releases. One 20-F read in v3 closed **twelve** open items at once: portfolio composition, entity-level cash, withholding, share-class structure, VIE quantification, book value (P/B 1.27×, never computed before), three-year audited trajectory, goodwill baseline. A deep-dive label now requires ≥1 annual report in the source trail |
| 2026-08-11 | **Pattern — acquisition closed mid-quarter, growth still looks weak** | IFRS 3 consolidates **prospectively**, so the base is never inflated and the contribution is purely additive. Build the bridge in absolute currency and count days consolidated: TME Q2 FY26 had 44 of 91 days (48%), and social entertainment (−RMB260mn) ate more than half of Ximalaya's +RMB407mn. Pre-commit the first full quarter as the validation quarter |

### Pattern: "Net income rose but basic EPS is flat (or basic and diluted EPS diverge)"
**Trigger:** NI up mid-single-digits, basic EPS ~0%, diluted EPS +1-2%; or weighted-avg basic shares jump while diluted barely moves
**Diagnosis:** A convertible (bond or preferred) likely converted — shares crossing from *potential* (diluted-only) to *actual* (basic). Not chronic dilution; not an earnings miss.
**Response:** Confirm via the convert-interest line (→ 0) and the diluted-EPS note (add-back dropped). Anchor on diluted per-share growth; assess conversion price vs IV for value transfer; mark the overhang cleared going forward.
