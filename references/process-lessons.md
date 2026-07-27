# Process Lessons — Self-Improvement Reference

> A compact reference for analytical errors and how to prevent them. Update this file when new errors are discovered. Read this before starting a new deep dive on any HK / China / India / dual-listed equity.

---

## Most Expensive Error Classes

Errors fall into two families:
- **Mechanical errors** (Classes 1-5): Wrong inputs. Catastrophic but visible — they break things obviously.
- **Interpretive errors** (Classes 6-10): Right inputs, wrong meaning. Subtle but cumulative — they corrupt conclusions silently.

Both families need separate defenses. Mechanical errors are stopped at Step 2.5 (reconciliation gate). Interpretive errors are stopped at Step 3.5 (earnings quality gate).

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

### INTERPRETIVE ERROR CLASSES (data meaning) — NEW

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

### Interpretive Checks (Step 3.5) — NEW

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

## Process Behaviors to Reinforce

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

### Pattern: "Net income rose but basic EPS is flat (or basic and diluted EPS diverge)"
**Trigger:** NI up mid-single-digits, basic EPS ~0%, diluted EPS +1-2%; or weighted-avg basic shares jump while diluted barely moves
**Diagnosis:** A convertible (bond or preferred) likely converted — shares crossing from *potential* (diluted-only) to *actual* (basic). Not chronic dilution; not an earnings miss.
**Response:** Confirm via the convert-interest line (→ 0) and the diluted-EPS note (add-back dropped). Anchor on diluted per-share growth; assess conversion price vs IV for value transfer; mark the overhang cleared going forward.
