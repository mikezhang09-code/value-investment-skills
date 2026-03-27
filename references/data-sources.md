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
