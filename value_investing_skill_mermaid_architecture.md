# Value Investing Skill Architecture & Workflow Specification
# 价值投资 Research Skill 架构与工作流程图解指南 (中英双语版)

> **Document Version**: 2026-11-10 (Data gate with three outcomes; valuation method rebuilt)  
> **Target Skill**: `value-investing`  
> **Core Philosophy**: Benjamin Graham, Warren Buffett, Charlie Munger, Philip Fisher  
> **Supersedes**: 2026-07-27 version (Post-Amendment #13)

**What changed since the 2026-07-27 version / 本版主要变化**

| Area / 领域 | Before / 之前 | Now / 现在 |
|---|---|---|
| Step 2.5 | Four anchors checked by hand; any failure stopped the analysis / 四锚点人工核对，任一失败即中断 | `validate_inputs.py` runs 11 checks (D1–D11) on an inputs file, plus an independent second read; outcome **VERIFIED / QUALIFIED / UNRESOLVED** — the analysis is always produced / 脚本化11项校验+独立复核；三种结果，分析始终输出 |
| Owner earnings / 所有者盈余 | Net income + D&A − maintenance capex (three conflicting definitions) / 以净利润为起点，三种口径并存 | Operating profit × (1 − tax) + D&A − maintenance capex, pre-interest, SBC not added back / 以经营利润为起点、税后、息前，不加回股权激励 |
| Growth / 增长 | Free / 增长无成本 | Charged at g ÷ RONIC; terminal RONIC by moat (r / r+2 / r+4) / 按 g ÷ 新增资本回报率扣除再投资 |
| Fair value / 公允价值 | Multi-method triangulation with free weights / 多方法自由加权 | One figure from the primary method per business type; others are cross-checks / 按业务类型取单一主方法，其余仅作交叉校验 |
| Financials / 金融 | P/B to ROE | Residual income with explicit fade (`residual_income.py`) / 带衰减的剩余收益模型 |
| Verdicts / 评级 | BUY / ACCUMULATE / MONITOR / PASS / SELL / AVOID | BUY / ACCUMULATE / WATCHLIST / HOLD / PASS / AVOID; SELL is an action / SELL为操作而非评级 |

---

## 1. System Architecture & Core Philosophy / 系统架构与核心哲学

The `value-investing` skill is built upon a fundamental principle: **protect downstream valuation and decision-making by enforcing strict upstream data integrity and quality gates**.

本技能的核心设计理念为：**通过设立严密的上游数据勾稽与盈余质量关口，确保下游的估值模型与投资决策建立在真实、未受扭曲的基础之上**。

```mermaid
flowchart TD
    subgraph Core_Philosophy ["Core Investment Philosophy / 核心投资哲学"]
        P1["Benjamin Graham: Margin of Safety & EPV/NCAV<br>本杰明·格雷厄姆：安全边际与资产/盈利能力估值"]
        P2["Warren Buffett: Moats & Owner Earnings<br>沃伦·巴菲特：护城河与所有者盈余"]
        P3["Charlie Munger: Inversion & Quality<br>查理·芒格：逆向思维与好生意/好管理"]
        P4["Philip Fisher: Scuttlebutt & Growth<br>菲利普·费雪：草根调研与长期成长性"]
    end

    subgraph Two_Upstream_Gates ["Two Upstream Protection Gates / 双重前置防护关口"]
        Gate25["Step 2.5: Data Gate (Mechanical)<br>validate_inputs.py D1–D11 + second read<br>步骤 2.5：数据关口 (脚本校验+独立复核)"]
        Gate35["Step 3.5: Earnings Quality Gate (Interpretive)<br>步骤 3.5：盈余质量关口 (解释准确性)"]
    end

    subgraph Core_Engine ["Value Investing Processing Engine / 价值投资分析引擎"]
        QuickScreen["Step 0: Quick-Kill Screener<br>步骤 0：8问快速淘汰筛选器"]
        DataCollect["Step 1-2: Scope, Structured Sources First, Inputs File<br>步骤 1-2：定界、结构化数据优先、录入数据文件"]
        FinancialDeep["Step 3: 10-Yr Financial Deep Dive<br>步骤 3：十年财务深度挖掘"]
        MoatIndustry["Step 4-5: Anchored Moat Scorecard & Industry Playbook<br>步骤 4-5：锚定护城河评分与行业专属指南"]
        ValuationOne["Step 6-6.5: One Fair Value per Business Type & Plausibility<br>步骤 6-6.5：按业务类型的单一公允价值与合理性校验"]
        RiskDecision["Step 7-9: MoS, Value Trap, Biases & Decision<br>步骤 7-9：安全边际、陷阱诊断、偏差自查与决策"]
        OutputGen["Step 10: Three Deliverables, each opening with the Data-Status Box<br>步骤 10：三份交付物，均以数据状态框开篇"]
    end

    Core_Philosophy --> QuickScreen
    QuickScreen -->|Pass Gate / 校验通过| DataCollect
    DataCollect --> Gate25
    Gate25 -->|VERIFIED / QUALIFIED / UNRESOLVED<br>always proceeds, labelled / 始终继续，并标注| FinancialDeep
    FinancialDeep --> Gate35
    Gate35 -->|Normalized / 调整归一化| MoatIndustry
    MoatIndustry --> ValuationOne
    ValuationOne --> RiskDecision
    RiskDecision --> OutputGen
    Gate25 -.->|Data status travels with the verdict<br>数据状态随评级一并输出| OutputGen

    style Gate25 fill:#f9f,stroke:#333,stroke-width:2px
    style Gate35 fill:#f9f,stroke:#333,stroke-width:2px
    style QuickScreen fill:#ff9,stroke:#333,stroke-width:2px
```

---

## 2. End-to-End Research Workflow / 端到端研究流程

The standard research procedure runs Steps 0 through 10.5. The data gate (2.5) no longer stops the analysis: it decides how frankly the result must be labelled. Step 3.5 still raises the bar on distorted earnings, and Step 6.5 still loops back when the output looks implausible.

标准研究流程为步骤 0 至 10.5。数据关口（2.5）不再中断分析，而是决定结果须如何如实标注；步骤 3.5 仍对扭曲盈余提高门槛；步骤 6.5 在结果异常时仍回溯核查。

```mermaid
flowchart TD
    S0["Step 0: Quick-Kill Screener<br>8-Question Gate / 8问快速淘汰筛选"] -->|Pass / 通过| S1["Step 1: Identify & Scope<br>Name, Ticker, Exchange, Currency, Sector / 确定标的、范围与行业"]
    S0 -->|Fail Q7 Integrity Veto / 诚信否决| VETO["AUTOMATIC VETO / 自动一票否决<br>Pass & Move On / 放弃并跳过"]
    S0 -->|4+ 'No' Answers / 4项以上否定| VETO

    S1 --> S2["Step 2: Data Collection<br>Structured sources first; latest 3 yrs tied to filings;<br>every number + page + quoted line → inputs file<br>结构化数据优先；近3年对照原始财报；逐项录入数据文件"]
    S2 --> S25{"Step 2.5: Data Gate<br>validate_inputs.py D1–D11 + independent second read<br>数据关口：脚本校验 + 独立复核"}

    S25 -->|No gap, no conflict| V["VERIFIED<br>Normal report / 正常报告"]
    S25 -->|Gaps only / 仅有缺口| Q["QUALIFIED<br>Verdict PROVISIONAL · conviction ≤ 6/10 · MoS +10 pts<br>评级标注暂定 · 确定性≤6 · 安全边际+10个百分点"]
    S25 -->|A conflict / 存在矛盾| U["UNRESOLVED<br>Try to resolve first; else value under each reading, NO verdict<br>先尝试化解；否则按各读数分别估值，不给评级"]
    U -.->|Resolved by re-reading the filing / 重读财报化解| S2

    V --> S3["Step 3: Financial Analysis<br>10-Yr Financial Table & Metrics / 10年财务数据与比率分析"]
    Q --> S3
    U --> S3
    S3 --> S35{"Step 3.5: Earnings Quality Gate<br>盈余质量关口 (8 Distortion Classes)"}

    S35 -->|Composite Score < 16 or Leakage / 质量低| HIGH_RISK["Require >50% MoS or Consider Uninvestable<br>要求>50%安全边际或直接判定不可投"]
    S35 -->|Normalized Financials / 完成盈余归一化| S4["Step 4: Moat Assessment<br>Anchored /30 Scorecard, Durability & Trend / 锚定评分、耐久度与趋势"]
    HIGH_RISK --> S4

    S4 --> S5["Step 5: Industry Analysis & Playbook<br>Sector Playbooks & Avoid Lists / 行业专属指南与规避清单"]
    S5 --> S6["Step 6: Intrinsic Valuation<br>One fair value from the primary method / 主方法得出单一公允价值"]

    S6 --> S65{"Step 6.5: Plausibility Checks<br>估值合理性回溯校验 (4 Sanity Tests)"}
    S65 -->|Fail 2+ Tests / 2项以上异常| FAIL65["Model Error Suspected! Re-check inputs<br>怀疑模型错误！退回数据关口重查"]
    FAIL65 --> S25

    S65 -->|Plausible / 校验合理| S7["Step 7: Margin of Safety<br>Price vs the one fair value / 价格对照单一公允价值"]
    S7 --> S8["Step 8: Risk & Sell Check<br>Value Traps, Inflation, Biases / 价值陷阱诊断、宏观与偏差自查"]
    S8 --> S9["Step 9: Investment Decision<br>BUY / ACCUMULATE / WATCHLIST / HOLD / PASS / AVOID<br>(PROVISIONAL if QUALIFIED; none if UNRESOLVED)"]
    S9 --> S10["Step 10: Report Generation<br>Report · Dashboard · Bilingual Summary, each with the Data-Status Box<br>报告、仪表盘、双语摘要，均附数据状态框"]
    S10 --> S105{"Step 10.5: Deliverable Gate<br>交付物关口: manifest + canonical figures match"}

    style S25 fill:#ffe6e6,stroke:#ff0000,stroke-width:2px
    style S35 fill:#ffe6e6,stroke:#ff0000,stroke-width:2px
    style S65 fill:#fff0c2,stroke:#ff9900,stroke-width:2px
    style V fill:#e6ffe6,stroke:#009933,stroke-width:2px
    style Q fill:#fff7e6,stroke:#ff9900,stroke-width:2px
    style U fill:#ffe6e6,stroke:#cc0000,stroke-width:2px
    style VETO fill:#ffcccc,stroke:#999999,stroke-width:2px
```

---

## 3. Upstream Protection Gates Detailed Flow / 双重前置防护关口详细流程

### 3.1 Step 2.5: The Data Gate / 数据关口

Step 2.5 protects against transcription and scale slips, aggregator errors, dual-listing price-basis traps, hybrid capital distortions, stale quotes, missing treasury lines and mismatched windows. Every verdict-moving number carries its source, page and the line as printed; the script checks the arithmetic and a second, independent read checks the transcription. Each failed check is either a **GAP** (not read / not explained) or a **CONFLICT** (two figures disagree).

步骤 2.5 防范誊录与单位错误、第三方数据源错误、双重上市价格基准陷阱、永续债/AT1 导致的股本扭曲、过期报价、遗漏的现金类科目以及期间口径错配。每个关键数字均记录出处、页码与原文；脚本核对勾稽，独立复核核对誊录。每项未通过的校验归为 **缺口（GAP）** 或 **矛盾（CONFLICT）**。

```mermaid
flowchart TD
    Inputs["inputs_&lt;ticker&gt;_&lt;date&gt;.json<br>every verdict-moving number: source, page, quoted line<br>关键数字：来源、页码、原文"] --> Script

    subgraph Script ["validate_inputs.py — checks D1–D11 / 11项校验"]
        direction TB
        D1["D1 Provenance: quote contains the value; filed/structured basis<br>出处：原文含该数值"]
        D2["D2 Units & currency / 单位与币种"]
        D3["D3 Share count: 4 anchors incl. senior-instrument gate,<br>EPS resolution, reverse market-cap test; valuation count =<br>period-end + dilution / 股本：四锚点"]
        D4["D4 Live price P1–P5 / 实时股价校验"]
        D5["D5 Net cash from every treasury line (Check 21) / 净现金"]
        D6["D6 Statements articulate: cash & equity roll-forward,<br>5-yr cash identity / 报表勾稽"]
        D7["D7 Owner-earnings tie: operating profit, tax, D&A,<br>maintenance capex = statement lines / 所有者盈余对账"]
        D8["D8 History basis: latest 3 yrs filed / 历史数据来源"]
        D9["D9 Matched windows: FY, YTD vs YTD, TTM / 期间匹配"]
        D10["D10 FX: dated official fixing / 官方定盘汇率"]
        D11["D11 Stake ≤ carrying value (Check 22) / 持股市值不超账面"]
        D1 --> D2 --> D3 --> D4 --> D5 --> D6 --> D7 --> D8 --> D9 --> D10 --> D11
    end

    Second["Independent second read of each verdict-moving number<br>(fresh agent in Claude Code; separate step in a Claude Project)<br>独立复核每个关键数字"] --> Script

    Script --> Outcome{"Any CONFLICT? Any GAP?<br>是否存在矛盾或缺口？"}
    Outcome -->|Neither / 均无| Ver["VERIFIED<br>Normal report"]
    Outcome -->|Gaps only / 仅缺口| Qual["QUALIFIED<br>Status box · PROVISIONAL · conviction ≤ 6 · MoS +10<br>gaps become the next fetch list / 缺口即下次补抓清单"]
    Outcome -->|Any conflict / 有矛盾| Unres["UNRESOLVED<br>Re-read the filing; if still in conflict, run the DCF once per<br>reading (--reading) and give NO verdict<br>重读财报；仍矛盾则按各读数分别估值，不给评级"]

    Ver --> Out["--status-box opens every deliverable · --trail prints the Data Trail<br>数据状态框置于所有交付物开头 · 自动生成数据溯源表"]
    Qual --> Out
    Unres --> Out

    style Script fill:#e6f2ff,stroke:#0066cc,stroke-width:2px
    style Outcome fill:#ffffcc,stroke:#333,stroke-width:2px
    style Ver fill:#e6ffe6,stroke:#009933,stroke-width:2px
    style Qual fill:#fff7e6,stroke:#ff9900,stroke-width:2px
    style Unres fill:#ffe6e6,stroke:#cc0000,stroke-width:2px
```

The four anchors are still the heart of D3 / 四锚点仍是 D3 的核心:

```mermaid
flowchart LR
    A1["Anchor 1: Market cap, forward & reverse<br>锚点 1：市值正反双向校验"] --> A2G{"Anchor 2 pre-check:<br>senior instrument EQUITY or LIABILITY?<br>优先资本会计分类"}
    A2G -->|Equity / 权益| A2E["Deduct the distribution<br>扣除永续债分红"]
    A2G -->|Liability / 负债| A2L["Coupon already in interest<br>利息已扣除"]
    A2E --> A2["Anchor 2: (NI − senior) ÷ EPS vs weighted average,<br>stated at its resolution / 按精度披露"]
    A2L --> A2
    A2 --> A3["Anchor 3: BVPS, DPS × shares<br>≤2% pass · 2–5% with a note / 每股指标交叉校验"]
    A3 --> A4["Anchor 4: all share classes summed<br>H + A + ADR + treasury excluded / 全部股本类别"]
```

---

### 3.2 Step 3.5: Earnings Quality Gate & 8 Distortions / 盈余质量关口与 8 大扭曲类

Step 3.5 transforms accounting numbers into true **Economic Owner Earnings**.

步骤 3.5 将会计层面披露的净利润转换为反映商业本质的**经济所有者盈余**。

```mermaid
flowchart TD
    subgraph Eight_Distortions ["8 Distortion Classes Check / 8 大会计扭曲类排查"]
        D1["1. One-Time Items (非经常性损益/一次性收益或损失)"]
        D2["2. Dilution Drift (股本稀释漂移: 10年总量CAGR vs 每股CAGR)"]
        D3["3. Investment Portfolios (投资组合公允价值变动主导净利润)"]
        D4["4. Working Capital Quality (营运资金质量: 应收账款/现金转换率)"]
        D5["5. Stock-Based Compensation (股权激励SBC未在Non-GAAP中扣除)"]
        D6["6. Related-Party Transactions (关联交易与控股股东利益输送)"]
        D7["7. Off-Balance-Sheet Items (表外债务/养老金缺口/VIE担保)"]
        D8["8. Goodwill & M&A (商誉减值风险/无形资产/外延式并购依赖)"]
    end

    subgraph Sector_Flags ["Sector Binary Gating Flags / 板块特有二元关口标记"]
        S_Ins["Insurance: I-1 Reserve Dev, I-2 Discount Rates, I-3 IFRS 17 Break<br>保险：准备金发展、折现率假设、IFRS 17重述"]
        S_Bank["Banking: B-1 ECL Provisioning Discretion<br>银行：预期信用损失拨备自由裁量权"]
    end

    Eight_Distortions --> Bridge["Normalized Earnings Bridge Construction<br>构建归一化盈余桥接表 (Reported NI → Normalized NI)"]
    Sector_Flags --> Bridge
    Bridge --> ScoreComposite["Calculate Composite Quality Score (/40)<br>计算盈余质量综合得分 (满分 40 分)"]

    ScoreComposite --> GateCheck{"Composite Score & Risk Gate Check<br>综合得分与风险门禁评估"}
    
    GateCheck -->|Score 32-40| HighQual["Exceptional Quality / 极高质量<br>Standard Margin of Safety / 标准安全边际"]
    GateCheck -->|Score 24-31| GoodQual["Good Quality / 良好质量<br>Minor Normalization Applied / 需进行微调归一化"]
    GateCheck -->|Score 16-23 or 3+ Distortions| MediumRisk["Questionable Quality / 质量存疑<br>Demand +10-15pp MoS, Cap Conviction at 6/10<br>提高10-15%安全边际，确定性上限封顶6/10"]
    GateCheck -->|Score < 16 or Class 6 Leakage| Uninvestable["Severe Accounting Distortion / 严重会计扭曲<br>Require >50% MoS or Deem Uninvestable / 需>50%MoS或直接判定不可投"]

    style ScoreComposite fill:#e6ffe6,stroke:#009933,stroke-width:2px
    style GateCheck fill:#ffffcc,stroke:#333,stroke-width:2px
```

---

## 4. Sector Playbook Override & Early Loading Logic / 行业专属指南覆盖逻辑

The skill identifies the sector in **Step 1** and loads the overrides from `references/industry-playbooks.md` before the financial table and the valuation method are chosen.

技能在**步骤 1**识别行业，并在构建财务表与选择估值方法之前载入 `references/industry-playbooks.md` 中的覆盖规则。

```mermaid
flowchart LR
    subgraph Step1_Scope ["Step 1: Scope & Sector Identification"]
        IndCheck{"Check Sector Index in industry-playbooks.md<br>检查行业索引库"}
    end

    subgraph Sector_Overrides ["Primary method per business type / 各业务类型的主估值方法"]
        FinOverride["Banks & Insurers / 银行与保险<br>----------------------------------------<br>• Metrics: ROE/ROA/NIM/Combined Ratio, no gross margin<br>• Primary: residual income with explicit fade (residual_income.py)<br>• Justified P/B VOID where ROE × (1 − payout) ≥ r<br>• Cross-checks: EPV floor, DDM, fade ladder<br>• NO Graham Formula / NO NCAV"]
        CycOverride["Cyclicals & Capital-Heavy / 周期与重资产<br>----------------------------------------<br>• Mid-cycle owner earnings (≥7 yrs, ≥1 down year)<br>• +1 pt business-risk rate add-on<br>• Primary: owner-earnings DCF"]
        HoldcoOverride["Holdcos & Conglomerates / 控股公司<br>----------------------------------------<br>• SOTP mandatory beside the DCF<br>• Discount only with a named enforcing mechanism<br>• Duplicate-exposure test"]
        DistOverride["Distressed / Asset Plays / 困境与资产型<br>----------------------------------------<br>• Primary: NCAV or liquidation value<br>• Required MoS 40%+"]
    end

    IndCheck -->|Financials / 金融| FinOverride
    IndCheck -->|Cyclical / 周期| CycOverride
    IndCheck -->|Conglomerates / 控股公司| HoldcoOverride
    IndCheck -->|Distressed / 困境| DistOverride
    IndCheck -->|Other going concerns / 其他持续经营企业| GenericFlow["Owner-earnings DCF<br>fair value = lower of Base and probability-weighted<br>Cross-checks: EPV, reverse DCF, peers<br>所有者盈余DCF：取基准与概率加权中较低者"]

    style FinOverride fill:#f0f3ff,stroke:#3366cc,stroke-width:2px
    style Sector_Overrides fill:#fafafa,stroke:#666,stroke-width:1px
```

---

## 5. Valuation Engine & Plausibility Feedback Loop / 估值引擎与合理性校验闭环

Step 6 values the business on **one owner-earnings definition**, charges growth for the capital it needs, bridges to equity counting every balance-sheet item once, and states **one fair value**. Other methods are cross-checks, never averaged in. Step 6.5 then runs four sanity tests and loops back to the data gate if two or more fail.

步骤 6 采用**统一的所有者盈余口径**，对增长扣除所需再投资，在权益桥接中每个资产负债表项目只计一次，并给出**单一公允价值**。其他方法仅作交叉校验，不参与加权。步骤 6.5 执行4项合理性测试，2项以上异常则退回数据关口。

```mermaid
flowchart TD
    subgraph OE ["Operating owner earnings (validated, D7) / 经营性所有者盈余"]
        OE1["(Operating profit − financial items inside it) × (1 − normal tax)<br>+ D&A − maintenance capex ± normal working capital<br>Pre-interest · SBC stays an expense · base = latest revenue × avg margin<br>Cyclicals: mid-cycle margin<br>息前 · 股权激励视为费用 · 周期股用周期中值利润率"]
    end

    subgraph Rate ["Discount rate / 折现率"]
        R1["Currency base (USD 10% · HKD 9% · RMB/JPY/SGD/TWD 8% · INR 12%)<br>+ Step 3b business risk 0 to +2 pts (variability, moat, leverage, cyclical)<br>货币基准利率 + 业务风险加点"]
    end

    subgraph Growth ["Growth is not free / 增长有成本"]
        G1["Cash to owners = OE × (1 − g ÷ RONIC)<br>RONIC from measured ROIC (organic: ex goodwill; acquired: incl.), cap 60%<br>Terminal RONIC = r / r+2 / r+4 by moat class<br>按新增资本回报率扣除再投资；终值回报按护城河等级"]
    end

    subgraph Scen ["scenario_dcf.py — four scenarios / 四情景"]
        SC["Disruption · Bear · Base · Bull<br>growth, terminal growth and (with a reason) the earnings level differ<br>prints terminal-value share and a per-share bridge"]
    end

    OE --> Scen
    Rate --> Scen
    Growth --> Scen

    Scen --> Bridge["Bridge to equity: EV + net cash (Check 21) + stakes (Check 22)<br>− minorities − pension deficit; ÷ period-end shares + dilution<br>权益桥接：每项只计一次"]
    Bridge --> FV["ONE FAIR VALUE = lower of Base and probability-weighted<br>单一公允价值 = 基准情景与概率加权值中较低者"]

    FV --> XC["Cross-checks: EPV floor · reverse DCF · peers · DDM / SOTP<br>> 30% apart → name the assumption that explains it<br>交叉校验：差距>30%须说明原因"]

    subgraph Step65 ["Step 6.5: Output Plausibility / 合理性4项校验"]
        T1["Test 1: 'Too Good to Be True' (heavily covered names)"]
        T2["Test 2: Peer Multiple Cross-Check"]
        T3["Test 3: Reverse DCF — implied growth"]
        T4["Test 4: Consensus divergence > 50% needs a specific assumption"]
    end

    XC --> Step65
    Step65 --> SanityCheck{"Fails 2+ tests?<br>是否2项以上异常？"}
    SanityCheck -->|YES / 是| LoopBack["Suspect an input or model error<br>Back to the Step 2.5 data gate<br>退回数据关口重查"]
    SanityCheck -->|NO / 否| Step7["Step 7: Margin of Safety on the one fair value<br>25% · 40%+ turnarounds · +10 if QUALIFIED<br>安全边际仅以单一公允价值计算"]

    style FV fill:#e6ffe6,stroke:#009933,stroke-width:2px
    style Growth fill:#f0f3ff,stroke:#3366cc,stroke-width:1px
    style Step65 fill:#fff7e6,stroke:#ff9900,stroke-width:2px
    style LoopBack fill:#ffe6e6,stroke:#cc0000,stroke-width:2px
```

---

## 6. Risk Assessment, Behavioral Bias Check & Decision Matrix / 风险评估、偏差自查与决策矩阵

Step 8 screens for value traps and cognitive biases before finalizing the rating in Step 9.

步骤 8 在步骤 9 输出最终评级前，对 5 类价值陷阱、宏观风险及 8 项认知偏差进行自我审查。

```mermaid
flowchart TD
    subgraph Step8_Risk ["Step 8: Risk Assessment & Self-Checks / 风险评估与自查"]
        VT["Value Trap Diagnostic (5 Types)<br>价值陷阱5类诊断:<br>1. Structural Decline (行业结构性衰退)<br>2. Commodity Business (无定价权大宗商品)<br>3. Capital Allocation (毁灭价值的M&A)<br>4. High Asset Low ROIC (重资产低资本回报)<br>5. Accounting Quality (现金转换率<70%)"]
        
        SellCheck["Sell Criteria Check (4 Triggers)<br>卖出纪律4项检查:<br>1. Price Severely Overvalued (股价严重过高)<br>2. Moat Permanently Destroyed (护城河永久破坏)<br>3. Management Integrity Issue (管理层诚信问题 - 立刻卖出!)<br>4. Better Opportunity (存在显著更优替代标的)"]
        
        Biases["Behavioral Bias & Self-Analysis Check (8-Question Filter)<br>行为认知偏差与自我校验8问:<br>Confirmation, Sunk Cost, Anchoring, Recency, Action Bias,<br>Verification first, Mega-cap market sanity, Data trail verification"]
    end

    Step8_Risk --> MoS_Input["Combine with Margin of Safety (Step 7)<br>结合步骤 7 安全边际比例"]

    subgraph Step9_Decision ["Step 9: Investment Recommendation Matrix / 投资决策矩阵"]
        MoS_Input --> DS{"Data status from Step 2.5<br>数据关口结果"}
        DS -->|VERIFIED| Ratings
        DS -->|QUALIFIED| Ratings
        DS -->|UNRESOLVED| NoVerdict["NO VERDICT — data conflict<br>value shown under each reading<br>不给评级，列示各读数下的估值"]
        Ratings["Decision Rating / 决策评级 (QUALIFIED → marked PROVISIONAL, conviction ≤ 6):<br>----------------------------------------<br>• BUY (买入): strong business, MoS above the requirement<br>• ACCUMULATE (逐步买入): strong business approaching fair value<br>• WATCHLIST (观察名单): good business, no adequate MoS yet; entry zone set<br>• HOLD (持有): already owned, do not add at this price<br>• PASS (放弃): quality insufficient or no MoS<br>• AVOID (规避): structural decline, excessive debt or integrity<br>SELL is an action on a held position, not a verdict / 卖出为操作，非评级"]
    end

    style Step9_Decision fill:#e6ffe6,stroke:#009933,stroke-width:2px
    style NoVerdict fill:#ffe6e6,stroke:#cc0000,stroke-width:2px
    style VT fill:#fff0f0,stroke:#cc0000,stroke-width:1px
```

---

## 7. Deliverables Generation & Portfolio Construction Sub-Workflow / 交付物生成与组合构建子流程

Step 10 produces three deliverables, each opening with the data-status box, derived from one canonical figure block; Step 10.5 checks they exist and agree. Portfolio sizing applies where a position is added.

步骤 10 输出三份交付物，均以数据状态框开篇，且全部源自同一组规范数据；步骤 10.5 核查交付物齐全且数字一致。新增持仓时执行组合仓位规则。

```mermaid
flowchart TD
    subgraph Step10_Deliverables ["Step 10: Deliverables / 交付物"]
        Box["Data-Status Box (validate_inputs.py --status-box)<br>VERIFIED / QUALIFIED + gaps / UNRESOLVED + conflicts<br>数据状态框"]
        Rpt["1. Markdown Report (10 Sections)<br>valuation leads with drivers, break-evens, terminal-value share,<br>dated falsifiable forecasts; generated Data Trail (--trail)<br>Markdown报告：以驱动因素、盈亏平衡点与可证伪预测为先"]
        Dash["2. HTML Dashboard (12 tabs)<br>交互式仪表盘"]
        Sum["3. Bilingual EN/中文 Summary (derived from the report)<br>中英双语摘要"]
        Box --> Rpt
        Box --> Dash
        Box --> Sum
    end

    Canon["One canonical figure block (command-center JSON row)<br>verdict, conviction, fair value, MoS, entry zone, rate, implied return<br>唯一规范数据块"] --> Step10_Deliverables
    Step10_Deliverables --> Gate105{"Step 10.5: Deliverable Gate<br>files exist · figures identical<br>交付物齐全且数字一致"}

    subgraph Portfolio_Rules ["Portfolio Construction Rules / 组合构建与仓位管理法则"]
        Rule1["Concentrated Portfolio (10-20 Stocks)<br>集中型组合 (10-20 只优质标的)"]
        Rule2["Position Size Caps (3% - 15%)<br>单一标的仓位上限 (3%-15%)"]
        Rule3_ParentSub["Parent & Subsidiary Combined Cap Rule (母子公司联合仓位上限法则)<br>--------------------------------------------------<br>Where a book holds both a parent holdco and a listed subsidiary<br>that constitutes most of its value, COMBINED position cap<br>is the subsidiary's cap — NEVER the sum of both!<br>母公司与核心上市子公司视为同一风险暴露，联合仓位不得超过子公司单独上限！"]
    end

    Gate105 --> Portfolio_Rules

    style Box fill:#fff7e6,stroke:#ff9900,stroke-width:2px
    style Rule3_ParentSub fill:#ffe6e6,stroke:#cc0000,stroke-width:2px
    style Step10_Deliverables fill:#f9f9f9,stroke:#333,stroke-width:1px
```

---

## Summary of Core Principles / 核心原则总结

1. **Record Before You Analyze (先录入，后分析)**: every verdict-moving number goes into the inputs file with its page and the line as printed, and is read twice.
2. **Analyse on What You Have, and Say So (据实分析，如实标注)**: gaps qualify the verdict; conflicts remove it. The analysis is never withheld and never presented as more verified than it is.
3. **Normalize Before You Value (先归一化，后估值)**: Step 3.5 bridges accounting earnings to economic owner earnings.
4. **One Owner-Earnings Definition, Counted Once (统一口径，只计一次)**: operating, pre-interest, SBC as an expense; net cash and debt enter the bridge exactly once.
5. **Growth Is Not Free (增长有成本)**: every point of growth is charged for the capital it needs.
6. **One Fair Value (单一公允价值)**: from the primary method for the business type; other methods cross-check, they do not average in.
7. **Per-Share Economics Over Aggregates (每股价值高于总量增长)**: Dilution drag matters to existing shareholders.
8. **Parent & Subsidiary Risk Aggregation (母子公司合并风险敞口)**: Treat parent and major listed subsidiary as a single exposure.
