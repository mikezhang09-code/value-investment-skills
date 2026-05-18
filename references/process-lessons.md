# Process Lessons — Self-Improvement Reference

> A compact reference for analytical errors and how to prevent them. Update this file when new errors are discovered. Read this before starting a new deep dive on any HK / China / India / dual-listed equity.

---

## Top 5 Most Expensive Error Classes

### 1. Wrong Share Count (Highest-Impact Single-Point-of-Failure)
**Frequency:** Common, especially for dual-listed Chinese companies (H+A), US dual-class (GOOG/GOOGL), and post-equity-raise scenarios.

**Cost:** Catastrophic — every per-share metric is wrong, every IV is wrong, the verdict is wrong.

**Prevention:** Mandatory 4-anchor reconciliation in SKILL.md Step 2.5. Always EPS back-check before any per-share calculation.

**Case study:** BYD May 2026 — used 3.04B shares vs. actual 9.085B (3x off). Caught only when user provided market cap. Required full report rewrite.

---

### 2. Currency / Scale Confusion
**Frequency:** Moderate, especially in HK markets (HKD vs CNY vs USD).

**Cost:** Outputs systematically off by 10-50%.

**Prevention:** Always state currency explicitly. Cross-check published market cap in user's preferred currency.

**Common HK conversion:** 1 HKD ≈ 0.92 CNY ≈ 0.128 USD.

---

### 3. Extrapolation of Recent Growth
**Frequency:** Very common, especially for high-flying tech and EV names.

**Cost:** Growth-stock valuations that look like value-stock undervaluation.

**Prevention:** Cap mid-term growth at 50-70% of recent CAGR. Apply reverse DCF to see what market expects.

---

### 4. Adjusted/Non-GAAP Earnings Trap
**Frequency:** Common — companies aggressively add back stock comp, restructuring, "one-time" items.

**Cost:** Owner earnings overstated by 20-40%.

**Prevention:** Start from GAAP. Make explicit adjustments only with justification. Stock comp is real expense.

---

### 5. Ignoring Balance Sheet
**Frequency:** Common — analysts focus on income statement, forget debt and dilution.

**Cost:** Equity value overstated.

**Prevention:** Always compute Enterprise Value first. Subtract net debt from EV to get equity value.

---

## Top 5 Most Useful Sanity Checks

### Check 1: Market Cap Reconciliation (30 seconds)
```
My shares × my price ≈ published market cap?
If gap > 5% → STOP, investigate.
```

### Check 2: EPS Back-Check (10 seconds)
```
Reported NI ÷ Reported EPS = my share count?
If gap > 2% → STOP, share count is wrong.
```

### Check 3: "Too Good to Be True" Test (1 minute)
```
Is my conclusion that a heavily-covered mega-cap is 40%+ mispriced?
If yes → verify all inputs before publishing.
```

### Check 4: Reverse DCF (5 minutes)
```
What growth rate does the market price imply?
If extreme (<0% or >25%), my model or the market is wrong.
Usually it's my model.
```

### Check 5: Single-Input Sensitivity (5 minutes)
```
If I change [share count / growth rate / discount rate] by 20%,
does my verdict change?
If yes → conclusion is fragile, verify the key input.
```

---

## Process Behaviors to Reinforce

### Pre-Analysis
- [ ] State share count explicitly at top of analysis
- [ ] Document source for share count (annual report, EPS back-check, etc.)
- [ ] Identify share-class structure (single-class, dual-class, dual-listed, ADR)

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
