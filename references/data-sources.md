# Data Sources Reference

This file covers where and how to find primary financial data for each covered market. Always prefer official exchange filings over secondary aggregators — they are authoritative and legally required to be accurate.

---

## US Markets — SEC EDGAR

**Primary source for all US-listed companies.**

### Key URLs
- **Full-text search**: `https://efts.sec.gov/LATEST/search-index?q="COMPANY NAME"&dateRange=custom&startdt=2014-01-01&enddt=2024-12-31&forms=10-K`
- **EDGAR company search**: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=NAME&CIK=&type=10-K&dateb=&owner=include&count=40`
- **Direct CIK lookup**: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=TICKER&type=10-K`
- **EDGAR full-text search**: `https://efts.sec.gov/LATEST/search-index?q="ticker"&forms=10-K,10-Q`

### Documents to Fetch
| Document | Frequency | Key Contents |
|----------|-----------|-------------|
| **10-K** | Annual | Full financials, MD&A, risk factors, business description |
| **10-Q** | Quarterly | Interim financials, quarterly updates |
| **DEF 14A** (Proxy) | Annual | Executive compensation, board composition, shareholder votes |
| **8-K** | As filed | Material events: earnings, acquisitions, management changes |
| **13F** | Quarterly | Institutional holdings (if analyzing who owns the stock) |

### What to Extract from 10-K
1. **Item 1**: Business description — what they do, competitive position
2. **Item 1A**: Risk factors — key threats management acknowledges
3. **Item 7**: MD&A — management's narrative on results
4. **Item 8**: Financial Statements — 3 years of income, balance sheet, cash flow
5. **Notes to financial statements**: Segment data, goodwill, debt terms, lease obligations

### Free Financial Data (US)
- **Macrotrends**: `macrotrends.net/stocks/charts/TICKER/company-name/revenue` — 10-year tables ready to use
- **Yahoo Finance**: `finance.yahoo.com/quote/TICKER/financials` — quick access
- **Wisesheets / StockAnalysis**: `stockanalysis.com/stocks/TICKER/financials/` — clean 10-year data

---

## Hong Kong — HKEx

**Primary source for all HK-listed companies (Main Board and GEM).**

### Key URLs
- **HKEx News (filing search)**: `https://www.hkexnews.hk/listedco/listconews/advancedsearch/search_active_main.aspx`
- **Company filings by stock code**: `https://www.hkexnews.hk/listedco/listconews/SEHK/[YEAR]/[MMDD]/[FILING].pdf`
- **Direct company search**: Search by stock code (e.g., 0001, 0700, 2318) at hkexnews.hk
- **Stock code lookup**: `https://www.hkex.com.hk/Market-Data/Securities-Prices/Equities`

### Documents to Fetch
| Document | Frequency | Key Contents |
|----------|-----------|-------------|
| **Annual Report** | Annual | Full financials, business review, corporate governance |
| **Interim Report** | Semi-annual (every 6 months) | Mid-year financials |
| **Announcements** | As filed | Material events, results announcements |
| **Circular** | As needed | Major transactions, rights issues |

### HKEx Filing Categories
- Type `"Annual Report"` in the document type filter
- Type `"Results Announcement"` for earnings releases
- HK companies report in HKD (or sometimes USD for dual-listed)

### HK-Specific Accounting Notes
- HK companies use HKFRS (Hong Kong Financial Reporting Standards) — very close to IFRS
- Many HK companies have significant Mainland China operations — look for geographic segment data
- Watch for: related party transactions, VIE structures (for China-exposed companies), RMB/HKD translation effects

### Free Financial Data (HK)
- **AASTOCKS**: `aastocks.com/tc/stocks/quote/detail/main.aspx?symbol=00001` — basic financials
- **AAStocks Financials**: Good for HK blue chips
- **Yahoo Finance HK**: `finance.yahoo.com/quote/0001.HK/`

---

## China A-Shares

**Note**: Disclosure standards have improved but remain less rigorous than US/HK. Exercise additional skepticism on earnings quality.

### Key URLs
- **Shanghai Stock Exchange (SSE)**: `http://www.sse.com.cn/disclosure/listedinfo/announcement/` — search by company name (Chinese) or stock code (6-digit, starts with 6)
- **Shenzhen Stock Exchange (SZSE)**: `http://www.szse.cn/disclosure/listed/bulletinType/index.html` — stock codes starting with 0 or 3
- **CSRC (regulator)**: `http://www.csrc.gov.cn/` — regulatory filings
- **cninfo.com.cn**: `http://www.cninfo.com.cn/new/index` — most comprehensive A-share disclosure aggregator (Chinese interface)

### Documents to Fetch
| Document | Chinese Name | Notes |
|----------|-------------|-------|
| Annual Report | 年度报告 (年报) | Full audited financials |
| Semi-Annual Report | 半年度报告 (半年报) | Mid-year |
| Quarterly Report | 季度报告 | Brief quarterly update |

### A-Share Specific Warnings
- Auditor quality varies — Big Four audits preferred
- State-owned enterprises (SOEs) have different incentive structures — scrutinize capital allocation
- VIE structures: for tech/education/media companies with foreign restrictions
- Regulatory risk: sector crackdowns (fintech 2021, education 2021, gaming scrutiny)
- Watch for: frequent "non-recurring income", asset write-downs, related party transactions

### Free Financial Data (China)
- **Yahoo Finance** covers some ADRs and H-shares
- **Macrotrends** for large companies with ADR listings
- For pure A-shares, use cninfo.com.cn or the exchange websites directly

---

## Singapore — SGX

### Key URLs
- **SGX Filing search**: `https://www.sgx.com/securities/company-announcements`
- **SGXNet announcements**: `https://www.sgxnet.sgx.com/SGXNET/FWPropSearch.nsf/`
- **Company search**: Search by company name or stock code at sgx.com

### Documents to Fetch
- **Annual Report**: Full financials + business review
- **SGX Announcements**: Earnings results, material announcements
- Singapore companies use SFRS (based on IFRS)

### SGX Notes
- Singapore market has many REITs, industrials, and financial companies
- Singapore dollar (SGD) reporting standard
- MAS (Monetary Authority of Singapore) regulations are generally strong — good disclosure

### Free Financial Data (Singapore)
- **Yahoo Finance**: `finance.yahoo.com/quote/D05.SI/` (DBS example)
- **SGX website**: Basic financial data
- **Macrotrends** for large-cap SGX names

---

## India — NSE / BSE

### Key URLs
- **BSE (Bombay Stock Exchange)**: `https://www.bseindia.com/corporates/ann.html` — search by company name or ISIN
- **NSE (National Stock Exchange)**: `https://www.nseindia.com/companies-listing/corporate-filings-announcements`
- **SEBI filings**: `https://www.sebi.gov.in/`
- **MCA (Ministry of Corporate Affairs)**: `https://www.mca.gov.in/` — company registry

### Documents to Fetch
| Document | Notes |
|----------|-------|
| Annual Report | Filed with BSE/NSE — full financials |
| Quarterly Results | Mandatory for listed companies (SEBI requirement) |
| Investor Presentations | Often on company IR website |

### India-Specific Notes
- Indian companies use Ind AS (India Accounting Standards, converged with IFRS)
- Indian Rupee (INR) reporting
- Strong sectors: IT services, pharma, FMCG, banking, insurance
- Family-owned conglomerates are common — check promoter holding % and pledged shares
- Watch for: promoter share pledging (financial stress signal), regulatory issues (especially pharma FDA)

### Free Financial Data (India)
- **Screener.in**: `https://www.screener.in/company/TCS/` — excellent free tool, 10-year financials, ratios
- **Tijori Finance**: Detailed Indian company analysis
- **Moneycontrol**: `moneycontrol.com` — financials and news
- **Yahoo Finance**: `finance.yahoo.com/quote/TCS.NS/`

---

## Universal Sources (All Markets)

### Company Investor Relations Websites
Every major listed company has an IR page. Typical URL patterns:
- `[company].com/investors`
- `[company].com/investor-relations`
- `ir.[company].com`

IR pages typically contain:
- Annual reports (PDFs)
- Earnings presentation slides
- Earnings call transcripts or audio
- Press releases
- Corporate governance documents

### Web Search Strategy for Qualitative Data
Use web search to find:
1. **Competitor analysis**: Search `"[company name] vs [competitor] analysis"`
2. **Industry reports**: Search `"[industry] market share report [year]"`
3. **Management reputation**: Search `"[CEO name] interview"` or `"[company] management quality"`
4. **Customer/product reviews**: Search `"[product] review"` or check relevant review platforms
5. **Regulatory issues**: Search `"[company] SEC investigation"` or `"[company] regulatory fine"`
6. **Recent news**: Search with date filters for last 12-24 months

### Financial News & Analysis
- **Bloomberg** (articles accessible via web)
- **Reuters** company pages
- **Financial Times**
- **Seeking Alpha** (investor analysis — treat as opinion, verify numbers)
- **Value Investors Club** — high-quality write-ups from institutional investors
- **GuruFocus** — Buffett/Munger portfolio tracker, some free data

---

## Data Quality Hierarchy

When multiple sources conflict, trust in this order:

1. **Official exchange filing** (10-K, HKEx annual report) — authoritative
2. **Company IR press release** — official but less audited
3. **Audit-verified aggregator** (Macrotrends, Screener.in) — generally reliable
4. **Yahoo Finance / Google Finance** — convenient but can have errors
5. **Analyst estimates** — forward-looking, use with caution
6. **News articles** — useful for context, not for financial data

**Always note**: fiscal year end dates vary — Apple (Sep), Berkshire (Dec), many HK companies (Dec or Mar). When comparing across companies, normalize to calendar year or clearly label fiscal years.

---

## Share-Class Structure Warnings ⚠️ NEW (May 2026)

This is where the most expensive share-count errors happen. **Always document share-class structure explicitly before any per-share calculation.** Multi-class structures are the single most common single-point-of-failure in equity valuation.

This section was added after the BYD May 2026 incident where H-share float was incorrectly used as total shares outstanding, producing per-share intrinsic values that were 3x too high and flipping a correct PASS verdict into a wrong BUY verdict.

### Warning Class A: HK-Listed Chinese Companies (H + A Shares)

HK-listed Chinese companies typically have multiple share classes:

| Class | Listing | Investors | Currency |
|-------|---------|-----------|----------|
| H-shares | HKEx | Foreign + HK | HKD |
| A-shares | Shanghai/Shenzhen | Domestic Chinese | CNY |
| B-shares (rare) | Shanghai/Shenzhen | Foreign in domestic exchanges | USD/HKD |
| ADRs (if applicable) | NYSE/Nasdaq | US | USD |

**The trap:** HK-focused data sources (Google Finance, AAStocks) sometimes report H-share count (the float listed in HK) as "shares outstanding." This is wrong for total company valuation.

**Example (BYD as of FY25):**
- H-shares (HK-listed): ~1.10 billion
- A-shares (Shenzhen-listed): ~7.99 billion
- **Total diluted: ~9.09 billion**

Using 1.10B alone understates true company by 8x. Using 3.04B (initial error) understates by 3x.

**Example (Ping An as of FY25):**
- H-shares (2318.HK): ~7.44 billion
- A-shares (601318.SS): ~10.76 billion
- **Total diluted: ~18.20 billion**

Google Finance shows "shares outstanding · 7.45B" for Ping An — this is H-shares only, not total.

**How to verify:**
1. **Company annual report** — search for "Composition of Share Capital" or "Share Information"
2. **EPS back-check** — Reported group net income ÷ reported EPS = total shares (always works mechanically)
3. **HKEx CCASS reports** — show H-share split by holder type but ALSO total issued shares
4. **Cross-check market cap** — published mcap ÷ price = total shares (sanity check)

**Examples of HK-listed Chinese companies with dual H+A structure:**
- BYD (1211.HK / 002594.SZ)
- China Mobile (941.HK / 600941.SS)
- Ping An Insurance (2318.HK / 601318.SS)
- ICBC (1398.HK / 601398.SS)
- China Construction Bank (939.HK / 601939.SS)
- Bank of China (3988.HK / 601988.SS)
- CNOOC (883.HK)
- Petrochina (857.HK / 601857.SS)
- China Life (2628.HK / 601628.SS)
- Sinopec (386.HK / 600028.SS)

**Special case — Tencent (0700.HK):** No A-share class. All shares are H-shares. ~9.2B shares total. Easier to handle correctly, but always confirm.

### Warning Class B: US Dual-Class Structures

| Company | Classes | Notes |
|---------|---------|-------|
| Alphabet | GOOGL (Class A, voting) + GOOG (Class C, non-voting) + Class B (private, super-voting) | Sum all three for total; GOOG and GOOGL trade publicly |
| Meta | Class A + Class B (super-voting, private) | Class B held by founder/insiders |
| Berkshire Hathaway | BRK.A + BRK.B | Different prices, but BRK.B is 1/1500 of BRK.A economic interest |
| Visa | Class A (public) + Class B + Class C (held by banks) | Conversion ratios apply |
| Snap | Class A (non-voting public) + Class B + Class C | Founder control via Class C |
| Liberty Media | Multiple tracking stocks | Complex; verify carefully |

**Action:** Always sum ALL classes for total shares. Most reported earnings/EPS are on a combined basis, so total shares = combined.

### Warning Class C: Indian Equities (NSE + BSE)

The same shares trade on both NSE and BSE. Total share count is NOT NSE + BSE.

| Source | What it shows |
|--------|---------------|
| NSE listing | Same shares as BSE; price may differ slightly due to liquidity |
| BSE listing | Same shares as NSE |
| Company annual report | True total share count |

**Don't double-count.** Look at the company's reported share capital.

### Warning Class D: Chinese ADRs

| Company | Underlying | ADR Ratio |
|---------|-----------|-----------|
| Alibaba (BABA) | 1 ADR = 8 ordinary shares | Confusing for per-share metrics |
| JD.com (JD) | 1 ADR = 2 ordinary Class A shares | |
| Baidu (BIDU) | 1 ADR = 8 Class A ordinary shares | |
| Pinduoduo / PDD | 1 ADR = 4 ordinary shares | |
| NetEase (NTES) | 1 ADR = 5 ordinary shares | |
| NIO (NIO) | 1 ADR = 1 Class A ordinary share | Simpler |

**Critical:** ADR price ≠ ordinary share price × ratio always — premium/discount exists. EPS reported per ADR ≠ EPS per ordinary share. Always confirm which basis you're using.

### Warning Class E: SPAC / Recent IPO / Post-Placement Companies

Companies that have recently:
- Completed an IPO
- Issued PIPE or follow-on offerings
- Completed share placements (HK Chinese companies frequently)
- Granted significant ESOPs / restricted stock units
- Issued convertible notes

...will have share counts that differ between pre/post-event reporting. Always use the most recent post-event count.

**Example:** BYD completed a HK$43.5B placement in early 2025, adding ~130M H-shares. Pre-placement and post-placement share counts differ. Reports written in 2024 may still cite the lower count.

### Warning Class F: Treasury Shares

"Shares issued" can include treasury shares (shares the company has bought back but not retired). For valuation, use:

```
Diluted Shares Outstanding = Issued Shares - Treasury Shares + Dilutive Instruments
```

Where dilutive instruments include:
- In-the-money options
- Convertible notes (if dilutive under if-converted method)
- Warrants
- Restricted stock units

The reported "diluted EPS" already accounts for these — back-solving from diluted EPS gives you the right count.

### Warning Class G: Perpetual / AT1 / Preference Capital ⚠️ NEW (July 2026)

**FIRST — run the classification gate.** The trap only exists where the instrument is classified as
**equity**. Check before anything else:

```
EQUITY-classified    → trap LIVE. Distribution is NOT in net profit. Subtract it.
                       HK/PRC insurer perpetual capital securities live here.

LIABILITY-classified → NO TRAP. Coupon is in interest expense; net profit is
                       already net of it. Anchor 2 clean by construction.
                       Indian bank AT1 (RBI Basel III / Banking Regulation Act
                       schedule format) and mainland capital supplementary
                       bonds (subordinated debt) live here.
```

**The name of the instrument tells you nothing — its classification tells you everything.** Sweep
of 2026-07-27: HDFC Bank and ICICI Bank both carry AT1 and **neither** produced the trap, because
both report it under borrowings. Skipping this gate false-alarms on most of a financials sleeve.

**Where the gate returns EQUITY — equity in form, senior in substance.** Perpetual capital
securities, AT1 notes and preference shares are presented *within* equity but rank **ahead of**
ordinary shares for both distributions and liquidation. Two consequences, both live:

```
1. SHARE COUNT
   Basic EPS is struck AFTER the senior distribution.
   Implied Shares = (Profit attributable to owners − senior distribution) ÷ basic EPS
   Skip the subtraction → share count overstated (3.83% on China Taiping FY25)
   ALWAYS state resolution: ±(0.5 × 10^−dp)/EPS. A gap below resolution is
   rounding, not a finding. EPS at 2dp on a ~1.00 base resolves only ~±0.5%.

2. PER-SHARE VALUE METRICS
   Issuer-published EV/share, NAV/share, BV/share may divide TOTAL equity
   by ordinary shares — attributing senior capital to ordinary holders.
   Strike an EX-PERPETUAL version before valuing on it.
   (China Taiping FY25: EVPS HK$58.297 → HK$53.85 ex-perp, −7.6%)
```

**Where to look:** statement of changes in equity (the distribution line); equity note (instrument
carrying value); and check for **subsidiary-level** perpetuals sitting inside non-controlling
interests — these are easy to miss because they never touch the parent equity note.

**Who carries them:** mainland Chinese insurers and banks (perpetual bonds and capital supplementary
bonds are routine regulatory capital), Indian banks (AT1), European banks, and utilities/REITs with
hybrid capital. **Assume present until checked** for any financial.

**Not a share-class problem.** This is orthogonal to Warning Classes A–F. An issuer with one share
class, one listing and a perfectly clean Anchor 4 can still fail here. The trap is in the **capital
stack**, not the share register.

### The Four Reconciliation Anchors

Before any per-share calculation, verify all four (per SKILL.md Step 2.5):

**Anchor 1: Market Cap Reconciliation** — run in BOTH directions
```
Forward:  Computed: Shares × Price = $X B
          Published (Yahoo): $Y B
          Published (Bloomberg/Reuters): $Z B
          Gap: ±X% — must be ≤ 5%

Reverse:  Implied Price = Published Market Cap ÷ Your Share Count
          ⚠️ MANDATORY for dual-listed (A+H, ADR+local) names.
          The implied price must match the listing you are analysing.
```
The reverse test catches **price-basis** errors that the forward test passes: an aggregator striking
market cap on the *other* listing's price and displaying it beside your quote. Caught live on PICC
Group (1339.HK) — see SKILL.md Step 2.5. Anchor 2 is the tiebreaker when the two directions disagree.

**Anchor 2: EPS Back-Check** (most reliable) — ⚠️ deduct senior distributions first (amendment #13)
```
Reported Net Income (attributable to owners): $X B
LESS perpetual / AT1 / preference distribution: $S B   ← Warning Class G; often overlooked
Reported EPS: $Y per share
Implied Shares = (X − S) / Y = Z B
Gap vs. assumed share count: ±W% — must be ≤ 2%
```

**Anchor 3: Per-Share Metrics Cross-Check**
```
Reported BV per share × Shares = $X B ≈ Total Equity (within 5%)
Reported DPS × Shares = $X M ≈ Total Dividends Paid (within 5%)
```

**Anchor 4: Share-Class Structure**
```
□ Class 1: ___ B shares (source: ___)
□ Class 2: ___ B shares (source: ___)
□ Class 3: ___ B shares (source: ___) [if applicable]
□ Total: ___ B shares
□ Reconciled with EPS back-check: Yes/No
```

If any anchor fails → STOP, re-source data from primary filings, re-run all four.

### Quick-Lookup Patterns

**"What's the right share count for an HK-listed Chinese company?"**
1. Annual report → "Composition of Share Capital" section
2. EPS back-check (NI ÷ EPS) using group-level numbers
3. Cross-check via market cap arithmetic

**"What's the right share count for a US company?"**
1. Most recent 10-Q cover page (shares outstanding as of recent date)
2. 10-K share count
3. EPS back-check using group-level numbers

**"What's the right share count for an Indian company?"**
1. Annual report
2. NSE listing page (NOT BSE — they're the same shares)
3. EPS back-check

**"What's the right share count for a SPAC / recent IPO?"**
1. Most recent 10-Q
2. Subtract any subsequently announced buybacks
3. Add any subsequent issuances (read 8-K filings)
4. EPS back-check using most recent quarter's reported EPS

---

## Verdict-Moving Numbers — When to Escalate

The hierarchy above tells you which sources to trust. This section tells you when to escalate from Tier 3 (aggregators) up to Tier 1 (filings).

**The ±20% rule:** if shifting a number by ±20% would flip the recommendation (Buy / Hold / Avoid) or push intrinsic value outside the margin-of-safety band, that number is **verdict-moving** and must be verified against the primary filing before the report reaches verdict stage. Aggregator data is not sufficient for verdict-movers.

Typical verdict-movers:
- Net cash / net debt position
- Owner earnings or FCF base used in DCF
- Non-operating assets in SOTP valuations
- Classification of items as recurring vs. one-time
- **Share count — basic vs. diluted vs. post-buyback vs. all-class total** (see Share-Class Structure Warnings above)
- Segment revenue/profit for moat assessment

Non-verdict-movers (Tier 3 aggregator acceptable):
- Revenue figures 3+ years back
- General margin trend direction
- Historical ROE for context (not used in intrinsic-value calc)

---

## Red-Flag Patterns from Past Analyses — 历史教训

Specific mistake classes that have surfaced in real work. Check for each explicitly on any SOTP, DCF, or verdict-stage analysis.

### RF-1. Pending M&A in current SOTP
Announced-but-not-closed acquisitions must not appear in the current sum-of-parts. Either exclude, or model pro-forma separately with the pending status clearly disclosed.
*Case: TME — pending Ximalaya acquisition was initially double-counted in SOTP.*

### RF-2. Unverified stakes or cross-holdings
Minority investments and strategic stakes must come from the most recent annual report's notes, not from press summaries or legacy filings.
*Case: TME — unverified Spotify stake estimate drove a ~$11B vs. ~$6.4B non-operating asset discrepancy until corrected against the balance sheet.*

### RF-3. Headline loss vs. cash performance
For companies reporting large GAAP losses, separate cash impact from non-cash impairments, fair-value remeasurements, and one-time writedowns before concluding anything about operating health.
*Case: Fosun — headline loss was dominated by non-cash impairments; core operations were healthier than the bottom line suggested.*

### RF-4. Mixed data vintage
DCFs combining annual actuals with quarterly run-rates must label vintage per line. Do not silently blend annual and quarterly figures.
*Case: BYD — FY2025 actuals (¥804B revenue, 17.7% GM) alongside Q1 2026 sales (700K units, -30% YoY) required explicit vintage labeling.*

### RF-5. Currency and listing-venue mismatches
Price in HKD, financials in RMB, ADR ratio ≠ 1:1 — verify the full conversion chain. For H-share vs. A-share dual listings, confirm which share class the EPS and book value correspond to.

### RF-6. Share count confusion
Match the share count to the period of the earnings figure. For companies with aggressive buybacks, current shares outstanding can diverge meaningfully from weighted-average diluted.

### RF-7. Wrong share class as total ⚠️ NEW (May 2026)
For HK-listed Chinese companies (and other dual-class structures), HK-focused data sources sometimes report H-share float as "total shares outstanding." This understates true total by 2x–10x.
*Case: BYD May 2026 — initially used 3.04B shares vs. actual 9.085B (H + A combined). 3x error. Caught only when user provided market cap. Required full report rewrite. See Share-Class Structure Warnings section above for the full reconciliation protocol.*
*Reproduction test on Ping An: Google Finance shows "shares outstanding 7.45B" — this is H-share only. True total: ~18.2B (H + A). EPS back-check (NI ÷ EPS) confirmed.*

---

## Data Trail — 数据台账

Any report reaching verdict stage should include a minimal audit trail for the top 5–10 inputs driving the valuation. Inline table or appendix — analyst's choice.

| Metric | Value | Source | Date retrieved | Vintage |
|--------|-------|--------|----------------|---------|
| Revenue FY2025 | ¥804B | BYD FY2025 annual report, p.XX | 2026-04-10 | FY2025 reported |
| Net cash | HK$62B | Xiaomi FY2025 annual report, balance sheet | 2026-04-08 | As of 2025-12-31 |
| Q1 2026 units | 700K | BYD monthly sales press release | 2026-04-15 | Q1 2026 |
| **Share count (total)** | **9.085B** | **BYD FY2025 AR composition + EPS back-check (32.62B ÷ 3.58 = 9.11B ✓)** | **2026-05-18** | **Post-2025 placement** |

Purpose: any report can be re-audited six months later to know exactly what went in and where it came from.

**Mandatory rows for share-class structure (added May 2026):** Any company with dual-class, dual-listing, or recent dilution must include explicit share-count row in the Data Trail with the reconciliation source noted (EPS back-check is the most reliable).

---

## Estimation Discipline

When an exact number is unavailable and an estimate is used:

1. **Label it** — prefix with `~` or annotate `(est.)` in tables
2. **Cite the basis** — "estimated from peer-average EV/EBITDA of 8x" is acceptable; "estimated" alone is not
3. **Sensitivity-test it** — if the estimate is verdict-moving (per §"Verdict-Moving Numbers" above), run the DCF/SOTP at the estimate ±20% and report the resulting range

---

## Pre-Verdict Checklist

Run before finalizing any Buy / Hold / Avoid recommendation:

- [ ] Every verdict-moving number has a Tier 1 or Tier 2 source
- [ ] **Share count reconciled via all four anchors (per Share-Class Structure Warnings section)** ⚠️ NEW
- [ ] **Classification gate run: senior instrument is EQUITY or LIABILITY? (Warning Class G) — only
      equity-classified instruments require the Anchor 2 subtraction** ⚠️ NEW
- [ ] **Where equity-classified: distribution deducted before Anchor 2, and any issuer-published
      per-share value metric restated ex-perpetual** ⚠️ NEW
- [ ] **Anchor 2 reported as "passes at ±X% resolution", never as an unqualified pass** ⚠️ NEW
- [ ] **Book-value denominator READ FROM A FILING, not derived from a ratio, and its GAAP basis named
      where the issuer publishes more than one (e.g. 20-F filers: US GAAP vs local)** ⚠️ NEW
- [ ] **Price vintage stated, and checked for an ex-dividend date passing since the quote (RF-4)** ⚠️ NEW
- [ ] No pending M&A is embedded in current SOTP (RF-1)
- [ ] Headline losses/gains decomposed into cash vs. non-cash (RF-3)
- [ ] Data vintage labeled per line for time-sensitive figures (RF-4)
- [ ] Currency and share-class conversions verified (RF-5, RF-6, RF-7)
- [ ] Data trail table present for top inputs (including share-count row for multi-class stocks)
- [ ] Estimates flagged with basis and sensitivity tested if verdict-moving
