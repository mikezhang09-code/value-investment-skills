# Data Inputs — the inputs file, the validator and the second pass

> **Rule.** Every number that reaches a valuation sits in `inputs_<ticker>_<YYYY-MM-DD>.json` and
> goes through `scripts/validate_inputs.py`. **The analysis is always produced.** What the validator
> decides is how frankly the report must be labelled — it never leaves the reader with nothing.
>
> **Why.** Prose checklists are filled in by the same reader that made the error; three recorded
> errors passed every written gate and were caught by the user. But a process that produces nothing
> when one filing is missing invites skipping the gate. So: analyse on what is in hand, and say
> plainly what is verified, what is missing and what disagrees.

A passing synthetic example is `assets/inputs-template.json`. Copy it and replace every value.

---

## 1. The three steps and the three outcomes

```
A  BUILD     Fill the inputs file while reading the sources. Every verdict-moving number gets a
             provenance entry: source, page, and the line as printed.
B  VALIDATE  python3 scripts/validate_inputs.py inputs_X.json --stage first
             Close what can be closed by re-sourcing — never by editing a number to fit.
C  SECOND    Independent re-read of every verdict-moving number (§4), then
   READ      python3 scripts/validate_inputs.py inputs_X.json      → writes validation_X.json
```

Each check returns **PASS** · **NOTE** (passed with a written reconciling note) · **FLAG** (allowed,
must be shown, e.g. ▲ single-source price) · **SKIP** (not applicable) · or one of two failures:

- **GAP** — something was not read, not recorded or not explained: a filing not fetched, a year
  taken from a summary table, dates that do not align, a second read not done.
- **CONFLICT** — two figures disagree, or a figure breaks a rule: a share count that does not
  reconcile to EPS, a quote page whose 52-week range excludes a price on file, cash that does not
  roll forward, a quoted line that does not contain the number.

| Outcome | When | What the report does |
|---|---|---|
| **VERIFIED** | no gap, no conflict, second read done | normal report |
| **QUALIFIED** | gaps only | full analysis and fair value; **data-status box** at the top of every deliverable; verdict carries **PROVISIONAL**; **conviction capped at 6/10**; **required margin of safety +10 points**; each gap listed with what it affects; the gaps become the next refresh's fetch list |
| **UNRESOLVED** | any conflict | data-status box; value shown **under each reading** of the conflicting number (`scenario_dcf.py --reading "<label>"`, one run per reading); **no single fair value and no verdict** until the conflict is resolved |

A gap is closed by fetching and reading; a conflict is closed by finding which figure is wrong.
Neither is closed by a note that restates it. The caps for QUALIFIED match the existing
earnings-quality gate (conviction ≤ 6, margin of safety +10–15) and do not stack beyond the larger
of the two.

**What to say for each gap.** State what it affects, and the size where it can be sized: the
unreconciled percentage on a share count, the fair-value range across the two dates of an unaligned
balance sheet, the years of history that rest on a summary table. "Not verified" without a
consequence is not enough.

Tools: `--status-box` prints the data-status box; `--trail` prints the Data Trail table. Both are
generated, never typed.

**Tolerance ladder, all ratio checks:** gap ≤ 2% passes; 2–5% passes only with a reconciling item
written in `notes["<check id>"]`; otherwise CONFLICT. The five-year cash identity (D6 cumulative)
uses 10% / 20% because it has more legitimate leaks (leases, investment purchases, FX).

---

## 2. File layout

All money and share counts use **one** scale (`meta.unit`) and **one** reporting currency
(`meta.currency`). With `unit: "millions"`, shares are in millions too, so NI ÷ EPS gives shares
directly.

| Block | Holds |
|---|---|
| `meta` | `ticker`, `listing`, `analysis_date`, `fiscal_year_end`, `currency`, `unit` (`units`/`thousands`/`millions`/`billions`), `scope` (`deep_dive`/`quick`/`refresh`/`earnings`), `ads_ratio` (ordinary shares per depositary share, else null), `is_depositary`, `cyclical` (true/false — autos, semiconductors, batteries, materials, shipping, airlines; required for `latest_margin`, and `scenario_dcf.py` stops if its `risk.cyclical` disagrees) |
| `sources[]` | `id`, `tier`, `doc`, `url`, `period`, `retrieved`, `annual` (true for an annual report) |
| `provenance{}` | keyed by path (e.g. `treasury.cash`, `shares.classes[H].count`, `statements.years[FY2025].ni`, `stakes[Spotify].shares_held`): `basis`, `source`, `page`, `quote`, optional `quote_scale` and `quoted_values`, `verified.value_read` |
| `shares` | `classes[]`, `period_end_count`, `period_end_date`, `dilutive`, `valuation_count`, `weighted_avg_basic`, `senior_instrument{classification, distribution}`, `ni_attributable`, `eps_basic`, `eps_dp`, `bvps`, `equity_attributable`, `dps`, `dividends_declared`, `published_market_caps[]`, `other_listing_prices[]`; with a depositary ratio also `count_basis` and `eps_basis` |
| `price` | `value`, `currency`, `date`, `p1_timestamp`, `sources[]` (`name`, `value`, `date`, `week52_low`, `week52_high`), `on_file[]` (`label`, `value`, `date`), `vintage_label`, `move_event`; with a depositary ratio also `basis` |
| `treasury` | exactly the block `scenario_dcf.py` reads, plus `as_of` |
| `statements.years[]` | one row per fiscal year: `fy`, `period_end`, `basis`, `source`, `revenue`, `op_profit`, `ni`, `da`, `capex`, `ocf`, `icf`, `cff`, `fx_effect`, `cash_begin`, `cash_end`, `pretax`, `tax`, `invested_capital`, `equity_begin`, `equity_end`, `dividends`, `buybacks`, `issuance`, `acquisitions`, `other_cash_uses`, `oci_and_other`, `equity_note`, `net_cash_end`, `shares_end`, `break_note`, `context_only` |
| `statements.ytd`, `ytd_prior` | `label`, `months`, and the same flow lines; optional `ttm` if a TTM figure is stated anywhere |
| `owner_earnings` | `components{FY: op_profit, non_operating, tax_rate, da, maintenance_capex, wc_adjustment}`, `maintenance_capex_basis`, `tax_rate_basis`, `non_operating_note`, `adjustments[]`, `method` (`average`, `margin`, or `latest_margin` with `structural_cause{line, kind, reason, amount, window_start{period, value, source}, periods[]{period, value, prior_value, source}}`), `value` — operating, pre-interest (`intrinsic-value.md` Method 1 Step 1) |
| `fx[]` | `from`, `to`, `rate`, `basis` (`fixing`), `date`, `source` |
| `stakes[]` | `name`, `shares_held` (absolute count), `quote`, `quote_currency`, `quote_date`, `carrying_value`, `accounting` (`fair_value`/`equity_method`), `holder_filing` |
| `notes{}` | reconciling notes keyed by check id |

Sign conventions: `capex`, `dividends`, `buybacks`, `issuance`, `acquisitions` are positive amounts;
`icf` and `cff` are signed as printed; `oci_and_other` is signed.

### The single source-tier ladder

One ladder for the whole skill (it replaces the six-level hierarchy and the three-tier ladder that
used the same labels for different things):

| `tier` | What it is | May back |
|---|---|---|
| `filing` | Annual / interim report, 10-K, 10-Q, 20-F, 年报, ownership filing | anything |
| `issuer_release` | The issuer's own results release with statements | anything except composition and notes |
| `structured` | Regulator-hosted structured data taken from filings (SEC company facts) | history; verdict-movers if the tag and period are quoted |
| `aggregator` | Data sites, quote pages | context only; quotes for the price gate |
| `wire` | Earnings flashes, news | a logged headline; never a number in this file |

### `basis` of a number or a history row

`filed` (read from a `filing` or `issuer_release`) · `structured` · `filing_summary` (the filing's
own multi-year summary table) · `aggregator` · `computed` · `estimated`.

---

## 3. What the validator checks

| ID | Check | GAP (missing / unexplained) or CONFLICT (disagrees) when |
|---|---|---|
| **D1** | Provenance of every verdict-moving number | no source, page or quote; basis is not `filed`/`structured`; **the quote does not contain the value**; second-pass read missing or different; a deep dive has no annual report |
| **D2** | Units and currency | unknown scale; per-share currency differs from reporting currency; price currency has no FX entry; depositary listing without a ratio or without stated bases |
| **D3** | Share count | class sum ≠ period-end count; valuation count ≠ period-end + dilution; EPS back-check fails (senior-instrument gate first, resolution stated); weighted-average gap unexplained; BVPS, DPS or market-cap cross-check off the ladder |
| **D4** | Price (P1–P5) | no timestamp note; a source dated differently; quote older than 4 days without a vintage label; a 52-week range that excludes a price on file; a >10% move with one source and no event; no source within ±2% |
| **D5** | Net cash | a treasury line missing; >5% from the issuer's own liquidity figure without reconciling items; cash and share count on different dates without a note |
| **D6** | Statement articulation | cash does not roll forward; equity does not roll forward; an unexplained equity plug above 10% of profit; cumulative free cash flow ≠ distributions + acquisitions + change in net cash |
| **D7** | Owner-earnings tie | operating profit or D&A ≠ its statement line; a net-income base or a stock-compensation add-back; maintenance capex above total capex or without a stated basis; tax rate without a basis or more than 5 points from the reported rate unexplained; financial items removed from operating profit without a note; the figure handed to the valuation ≠ the computed one; owner earnings >25% above average free cash flow without a note. **D7.structural** (method `latest_margin`): `meta.cyclical` true or not stated; no structural cause; the cause not a filed, quoted figure; `amount` ≠ the filed change over the window; fewer than the last two reported periods, or one moving the other way; the cause after tax explains less than half the gap between the two bases — each a CONFLICT |
| **D8** | History | too few years for the scope; one of the latest three years not `filed`; an `aggregator`/`estimated` year not marked `context_only`; an unexplained jump in revenue (>+50% / <−30%) or share count (>±20%) |
| **D9** | Matched windows | a year-to-date period with no prior-year window of the same length; a stated TTM that is not FY − prior YTD + YTD |
| **D10** | FX | a rate that is not a dated official fixing; a missing pair; a fixing more than 7 days old without a note |
| **D11** | Stake containment | shares × quote × FX above the carrying value of a fair-value line; no investee ownership filing named |

**A figure built from several printed lines** (depreciation + amortisation, cash less restricted
cash) lists them in `quoted_values`: each must appear in the quote and their sum, after
`quote_scale`, must equal the value. A sum is never written into the quote by hand.

**Verdict-moving numbers (D1 list):** each share class's count, attributable profit, basic EPS,
attributable equity, every treasury line and each debt line, any equity-classified senior
distribution, the latest fiscal year's revenue, operating profit, net income, depreciation, capex
and operating cash flow, and each stake's share count and carrying value.

**The share count used for valuation** is the latest period-end count (10-Q/10-K cover, exchange
monthly return, annual-report share-capital table) plus dilution. The EPS back-check is a
cross-check against the **weighted-average** count, not a way to derive the valuation count.

**Measured ROIC.** Where statement rows carry `invested_capital` (equity + debt − cash and
non-operating assets), the validation prints the average and the incremental ROIC over the usable
years. The valuation's RONIC is read from them and the script warns when it is set higher.

**History that is `context_only`** may appear in charts but is excluded from growth rates,
normalised averages and the profit-decline count behind the discount rate.

**What stays manual** (record the result in `notes` or the report): P1 — reading the quote's own
timestamp; Check 22 S1–S4, S6, S7 — finding and reading the investee's filing; Check 23 W5 — never
annualising a part-year segment figure; Checks 24–25; Checks 15–17.

---

## 4. The second pass

A transcription error survives every arithmetic check that uses the mistyped number on both sides.
The second pass re-reads the source without seeing the first reader's reasoning.

**Claude Code.** Start a fresh agent with only: the list of verdict-moving paths, each entry's
source URL and page, and the instruction to report the value printed there. It must not be given
the values. Write each answer to `provenance[path].verified.value_read`.

**Claude Project (no subagents).** After the inputs file is complete and `--stage first` passes,
do the re-read as a separate step: for each verdict-moving path, open the cited page again, read
the line, and record `verified.value_read` from the page — not from the file.

**In both.** A mismatch is resolved by a third read of the source, never by copying one value over
the other. A missing `value_read` is a GAP; a different one is a CONFLICT.

---

## 5. Running the valuation

`scenario_dcf.py` input must name the validation file:

```json
{ "validation": "validation_INTU_2026-10-10.json", "owner_earnings": 0, "...": "..." }
```

- **VERIFIED / QUALIFIED:** it runs. `owner_earnings`, `diluted_shares`, `price` and net debt must
  equal the validated figures (a figure the validation could not derive is listed under
  `not_validated`). On QUALIFIED data the output carries the gaps, the PROVISIONAL tag, the
  conviction cap and the extra margin of safety in `data_gate` and in `warnings`.
- **UNRESOLVED:** it runs only with `--reading "<label>"`, once per reading of the conflicting
  number; each output is one reading, not a fair value.
- **Always stops** when no validation file is named, when the inputs file changed after it was
  validated, or when a figure was retyped instead of taken from the inputs file. These are process
  failures, not data gaps, and cost one command to fix.

`--illustrative` runs without a validation file for sweeps and teaching examples; its output is
labelled UNVALIDATED and may not enter a report or the command center.

Tests: `python3 -m unittest discover -s scripts/tests`.

---

## Change log

- **2026-11-11** — **D7.structural and the `latest_margin` method.** The structural cause's figures
  are verdict-moving numbers (provenance, quote and second read required); the validation file
  carries `derived.owner_earnings_alternative` (the three-year-margin basis), which `scenario_dcf.py`
  values through to a second fair value. A cyclical (`meta.cyclical` true) cannot use it, and the flag
  must be stated; `scenario_dcf.py` stops when its rate build's `risk.cyclical` disagrees with the
  validated flag. Rule in `intrinsic-value.md` Method 1 Step 1.

- **2026-11-10 (b)** — **Three outcomes replace pass / stop.** Every failed check is a GAP or a
  CONFLICT; the result is VERIFIED, QUALIFIED or UNRESOLVED. The analysis is always produced: gaps
  qualify it (status box, PROVISIONAL, conviction ≤ 6, margin of safety +10), conflicts remove the
  verdict and show each reading. Decision by the user after the Great Wall pilot stopped on seven
  checks that were all "not yet read".

- **2026-11-10** — Created. Mechanises Anchors 1–4, P2–P5, Check 21 R1/R2/R6, Check 22 S5,
  Check 23 W1–W3 and the dated-fixing rule; adds provenance with quote matching (D1), unit checks
  (D2), statement articulation (D6), the owner-earnings tie (D7), history basis rules (D8) and the
  second pass. Resolves the Key Principle 3 / Check 21 R6 conflict in favour of the period-end count.
