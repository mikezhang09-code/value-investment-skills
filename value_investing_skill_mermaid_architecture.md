# Value Investing Skill Architecture & Workflow Specification
# 价值投资 Research Skill 架构与工作流程图解指南 (中英双语版)

> **Document Version**: 2026-07-27 (Post-Amendment #13 & 2026-07-26 Sweep Validation)  
> **Target Skill**: `value-investing`  
> **Core Philosophy**: Benjamin Graham, Warren Buffett, Charlie Munger, Philip Fisher

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
        Gate25["Step 2.5: Data Reconciliation Gate (Mechanical)<br>步骤 2.5：数据核对勾稽关口 (机械准确性)"]
        Gate35["Step 3.5: Earnings Quality Gate (Interpretive)<br>步骤 3.5：盈余质量关口 (解释准确性)"]
    end

    subgraph Core_Engine ["Value Investing Processing Engine / 价值投资分析引擎"]
        QuickScreen["Step 0: Quick-Kill Screener<br>步骤 0：8问快速淘汰筛选器"]
        DataCollect["Step 1-2: Scope & Primary Data Collection<br>步骤 1-2：定界与原生数据采集"]
        FinancialDeep["Step 3: 10-Yr Financial Deep Dive<br>步骤 3：十年财务深度挖掘"]
        MoatIndustry["Step 4-5: Moat Trend & Industry Playbook<br>步骤 4-5：护城河趋势与行业专属指南"]
        ValuationTri["Step 6-6.5: Triangulated Valuation & Plausibility<br>步骤 6-6.5：三角交叉估值与合理性校验"]
        RiskDecision["Step 7-9: MoS, Value Trap, Biases & Decision<br>步骤 7-9：安全边际、陷阱诊断、偏差自查与决策"]
        OutputGen["Step 10: Deliverables (Report, Model, Portfolio)<br>步骤 10：交付物输出 (报告/模型/组合)"]
    end

    Core_Philosophy --> QuickScreen
    QuickScreen -->|Pass Gate / 校验通过| DataCollect
    DataCollect --> Gate25
    Gate25 -->|Reconciled / 勾稽无误| FinancialDeep
    FinancialDeep --> Gate35
    Gate35 -->|Normalized / 调整归一化| MoatIndustry
    MoatIndustry --> ValuationTri
    ValuationTri --> RiskDecision
    RiskDecision --> OutputGen

    style Gate25 fill:#f9f,stroke:#333,stroke-width:2px
    style Gate35 fill:#f9f,stroke:#333,stroke-width:2px
    style QuickScreen fill:#ff9,stroke:#333,stroke-width:2px
```

---

## 2. End-to-End 11-Step Research Workflow / 端到端 11 步研究流程

The standard research procedure consists of 11 sequential steps (Steps 0 through 10). Step 2.5 and Step 3.5 act as mandatory circuit breakers.

标准研究流程分为 11 个步骤（步骤 0 至 10）。其中步骤 2.5 与步骤 3.5 作为强强制熔断关口。

```mermaid
flowchart TD
    S0["Step 0: Quick-Kill Screener<br>8-Question Gate / 8问快速淘汰筛选"] -->|Pass / 通过| S1["Step 1: Identify & Scope<br>Name, Ticker, Exchange, Currency / 确定标的与范围"]
    S0 -->|Fail Q7 Integrity Veto / 诚信否决| VETO["AUTOMATIC VETO / 自动一票否决<br>Pass & Move On / 放弃并跳过"]
    S0 -->|4+ 'No' Answers / 4项以上否定| VETO

    S1 --> S2["Step 2: Data Collection<br>Fetch 10-Yr Filings & Aggregators / 收集原生财报与数据源"]
    S2 --> S25{"Step 2.5: Data Reconciliation Gate<br>数据核对勾稽关口 (4 Anchors)"}
    
    S25 -->|Mismatch / 勾稽失败| FAIL25["STOP! Re-source from primary filings<br>停止！重新核对原生财报底稿"]
    FAIL25 --> S2
    
    S25 -->|Pass 4 Anchors / 4项勾稽通过| S3["Step 3: Financial Analysis<br>10-Yr Financial Table & Metrics / 10年财务数据与比率分析"]
    S3 --> S35{"Step 3.5: Earnings Quality Gate<br>盈余质量关口 (8 Distortion Classes)"}
    
    S35 -->|Composite Score < 16 or Leakage / 质量低| HIGH_RISK["Require >50% MoS or Consider Uninvestable<br>要求>50%安全边际或直接判定不可投"]
    S35 -->|Normalized Financials / 完成盈余归一化| S4["Step 4: Moat Assessment<br>5 Moat Types, Durability & Trend / 护城河类型、耐久度与趋势"]
    HIGH_RISK --> S4

    S4 --> S5["Step 5: Industry Analysis & Playbook<br>Sector Playbooks & Avoid Lists / 行业专属指南与规避清单"]
    S5 --> S6["Step 6: Intrinsic Valuation<br>Multi-Method Triangulation / 多模型三角交叉估值"]
    
    S6 --> S65{"Step 6.5: Plausibility Checks<br>估值合理性回溯校验 (4 Sanity Tests)"}
    S65 -->|Fail 2+ Tests / 2项以上异常| FAIL65["Model Error Suspected! Re-verify Anchors<br>怀疑模型错误！退回步骤2.5重新校验"]
    FAIL65 --> S25
    
    S65 -->|Plausible / 校验合理| S7["Step 7: Margin of Safety<br>Compare Price to IV Range / 确认安全边际比例"]
    S7 --> S8["Step 8: Risk & Sell Check<br>Value Traps, Inflation, Biases / 价值陷阱诊断、宏观与偏差自查"]
    S8 --> S9["Step 9: Investment Decision<br>BUY / ACCUMULATE / MONITOR / PASS / SELL / AVOID<br>投资决策定性与逻辑梳理"]
    S9 --> S10["Step 10: Report Generation<br>10-Section Report, Model & Portfolio Summary<br>生成10章节报告、Excel模型与组合建仓方案"]

    style S25 fill:#ffe6e6,stroke:#ff0000,stroke-width:2px
    style S35 fill:#ffe6e6,stroke:#ff0000,stroke-width:2px
    style S65 fill:#fff0c2,stroke:#ff9900,stroke-width:2px
    style VETO fill:#ffcccccc,stroke:#999999,stroke-width:2px
```

---

## 3. Upstream Protection Gates Detailed Flow / 双重前置防护关口详细流程

### 3.1 Step 2.5: Mechanical Data Reconciliation Gate / 机械数据勾稽关口

Step 2.5 protects against data aggregator errors, dual-listing price-basis traps, and hybrid capital distortions.

步骤 2.5 专门用于防范第三方数据源错误、双重上市价格基准陷阱以及混合资本结构（永续债/AT1）导致的股本扭曲。

```mermaid
flowchart TD
    subgraph Step_25_Reconciliation ["Step 2.5: Four Reconciliation Anchors / 四大勾稽锚点"]
        direction TB
        
        A1["Anchor 1: Market Cap Reconciliation<br>锚点 1：市值勾稽 (正向与逆向双向校验)<br>Forward: Shares × Price = MktCap (±5%)<br>Reverse: MktCap ÷ Shares = Implied Listing Price"]
        
        A2_Gate{"Anchor 2: Senior Instrument Classification Gate<br>锚点 2 预检：优先资本（永续债/AT1/优先股）会计分类门禁"}
        
        A2_Equity["EQUITY Classified (权益分类)<br>Coupon NOT deducted from Net Profit!<br>必须扣除永续债分红！"]
        A2_Liability["LIABILITY Classified (负债分类)<br>Coupon already in Interest Expense.<br>利息已在净利润中扣除，直接校验。"]
        
        A2_Calc["Anchor 2 Calculation:<br>Implied Shares = (Net Income - Senior Distributions) ÷ Reported EPS<br>Calculate diagnostic resolution: (0.5 × 10^-dp) ÷ EPS × 100%"]

        A3["Anchor 3: Per-Share Cross-Check<br>锚点 3：每股指标交叉校验<br>BV/share × Shares ≈ Total Equity (±5%)<br>DPS × Shares ≈ Total Dividends (±5%)"]

        A4["Anchor 4: Share-Class Structure Check<br>锚点 4：多股本结构全集核算<br>Total Shares = H-Shares + A-Shares + ADRs + Class B"]

        A1 --> A2_Gate
        A2_Gate -->|Equity / 权益| A2_Equity
        A2_Gate -->|Liability / 负债| A2_Liability
        A2_Equity --> A2_Calc
        A2_Liability --> A2_Calc
        A2_Calc --> A3
        A3 --> A4
    end

    A4 --> Decision{"Do all 4 anchors reconcile within tolerance?<br>四大锚点是否全部在容差范围内勾稽一致？"}
    Decision -->|YES / 是| Proceed["Proceed to Step 3 (Financial Analysis)<br>放行进入步骤 3 (财务深度分析)"]
    Decision -->|NO / 否| Stop["STOP ANALYSIS!<br>Re-verify with primary annual report filings.<br>中断分析！从官方年报重查股本结构"]

    style A2_Gate fill:#e6f2ff,stroke:#0066cc,stroke-width:2px
    style Decision fill:#ffffcc,stroke:#333,stroke-width:2px
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

The skill automatically detects company sector in **Step 1** and loads specialized metrics and valuation method overrides from `references/industry-playbooks.md`.

技能在**步骤 1**识别公司行业后，会自动提前载入 `references/industry-playbooks.md` 中的专属指标与估值模型覆盖逻辑。

```mermaid
flowchart LR
    subgraph Step1_Scope ["Step 1: Scope & Sector Identification"]
        IndCheck{"Check Sector Index in industry-playbooks.md<br>检查行业索引库"}
    end

    subgraph Sector_Overrides ["Sector Specific Overrides / 行业专属覆盖规则"]
        FinOverride["Financials (Insurance & Banking) / 金融板块 (保险与银行)<br>----------------------------------------<br>• Metric Substitution: No Gross Margin, ROE/ROA/NIM/Combined Ratio<br>• Leverage Interpretation: Regulatory leverage is structural<br>• Valuation Override: P/B to ROE, EPV floor, DDM/SOTP<br>• NO DCF / NO Graham Formula / NO NCAV"]
        TechOverride["SaaS & Asset-Light Tech / 科技与SaaS<br>----------------------------------------<br>• Metric Substitution: ARR, NRR, LTV/CAC, SBC Dilution<br>• Valuation Override: EPV, Normalized P/E"]
        HoldcoOverride["Conglomerates & Holdcos / 综合企业与控股公司<br>----------------------------------------<br>• Valuation Override: SOTP mandatory + Holdco Discount"]
    end

    IndCheck -->|Financials / 金融| FinOverride
    IndCheck -->|Tech / 科技| TechOverride
    IndCheck -->|Conglomerates / 控股公司| HoldcoOverride
    IndCheck -->|General Industrial / 通用工业| GenericFlow["Standard Workflow (DCF, EPV, Graham, etc.)<br>通用分析流程"]

    style FinOverride fill:#f0f3ff,stroke:#3366cc,stroke-width:2px
    style Sector_Overrides fill:#fafafa,stroke:#666,stroke-width:1px
```

---

## 5. Triangulated Valuation & Plausibility Feedback Loop / 估值三角交叉与合理性校验闭环

Step 6 executes valuation calculations using at least two independent methods, followed by Step 6.5 sanity checks. If an error is detected, the flow loops back to reconciliation.

步骤 6 使用至少两种独立方法进行三角估值，随后在步骤 6.5 进行 4 项合理性反向校验。若检测出异常，流程将自动回溯至勾稽关口。

```mermaid
flowchart TD
    subgraph Step6_Valuation ["Step 6: Triangulated Intrinsic Valuation / 多模型三角交叉估值"]
        M1["1. Owner Earnings DCF (Buffett)<br>所有者盈余现金流折现"]
        M2["2. Earnings Power Value - EPV (Greenwald)<br>零增长盈利能力价值"]
        M3["3. Graham Formula (Graham)<br>格雷厄姆经典公式"]
        M4["4. Dividend Discount Model - DDM<br>股息折现模型"]
        M5["5. Asset-Based / NCAV (Graham)<br>净清算资产估值"]
        M6["6. Sum-of-the-Parts - SOTP<br>分部加总估值 (Holdcos)"]
    end

    Step6_Valuation --> Range["Establish Intrinsic Value Range<br>建立内在价值区间 (Conservative / Base / Optimistic)"]

    subgraph Step65_Plausibility ["Step 6.5: Output Plausibility Sanity Tests / 估值合理性4项校验"]
        T1["Test 1: 'Too Good to Be True'<br>大盘蓝筹股 MoS > 40% 须极度审慎并找出差异主因"]
        T2["Test 2: Peer Multiple Cross-Check<br>隐含乘数 (P/E, EV/EBITDA, P/B) 与同业中位数对比"]
        T3["Test 3: Reverse DCF<br>反向 DCF 求解当前股价隐含的永续增长率"]
        T4["Test 4: Analyst Consensus Divergence<br>与卖方共识估值偏离 > 50% 必须有明确可防御假设"]
    end

    Range --> Step65_Plausibility

    Step65_Plausibility --> SanityCheck{"Fails 2+ Plausibility Tests?<br>是否触发 2 项以上校验异常？"}
    
    SanityCheck -->|YES (Failure) / 是 (异常)| LoopBack["SUSPECT MODEL ERROR!<br>Loop back to Step 2.5 Reconciliation Gate<br>怀疑数据或模型错误！退回步骤 2.5 重查底稿"]
    LoopBack -->|Re-verify Anchors| Step25_Ref["Step 2.5: Data Reconciliation Gate"]
    
    SanityCheck -->|NO (Passed) / 否 (合理)| Step7_MoS["Step 7: Margin of Safety Gate<br>进入步骤 7：安全边际确认"]

    style Step65_Plausibility fill:#fff7e6,stroke:#ff9900,stroke-width:2px
    style SanityCheck fill:#ffffcc,stroke:#333,stroke-width:2px
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
        MoS_Input --> Ratings
        Ratings["Decision Rating / 决策评级:<br>----------------------------------------<br>• BUY (买入): Strong quality + MoS > 25-40%<br>• ACCUMULATE (加仓/逢低建仓): High quality, MoS 10-25%<br>• MONITOR (观望): Great business, fully valued (MoS < 10%)<br>• PASS (跳过): Fair/Poor quality, insufficient MoS<br>• SELL (卖出): Triggered Sell Criteria<br>• AVOID (规避): Structural trap or Integrity flaw"]
    end

    style Step9_Decision fill:#e6ffe6,stroke:#009933,stroke-width:2px
    style VT fill:#fff0f0,stroke:#cc0000,stroke-width:1px
```

---

## 7. Deliverables Generation & Portfolio Construction Sub-Workflow / 交付物生成与组合构建子流程

Step 10 formats findings into a 10-section markdown report, optional 12-tab Excel model, and portfolio position sizing.

步骤 10 将分析成果规范化输出为 10 章节 Markdown 研究报告、可选的 12 标签页 Excel 估值模型以及投资组合仓位管理方案。

```mermaid
flowchart TD
    subgraph Step10_Deliverables ["Step 10: Deliverables Specification / 交付物规范"]
        Rpt["1. Written Investment Report (10 Sections)<br>书面投资研究报告 (10大标准章节)<br>Must include Step 2.5 Data Trail Anchors!"]
        Mdl["2. Excel Financial Model (Optional)<br>10-Yr Hist, 5-Yr Scenarios, DCF & Sensitivities"]
        Port["3. Portfolio Addition Summary<br>组合建仓与仓位管理方案"]
    end

    subgraph Portfolio_Rules ["Portfolio Construction Rules / 组合构建与仓位管理法则"]
        Rule1["Concentrated Portfolio (10-20 Stocks)<br>集中型组合 (10-20 只优质标的)"]
        Rule2["Position Size Caps (3% - 15%)<br>单一标的仓位上限 (根据护城河与MoS确定 3%-15%)"]
        Rule3_ParentSub["Parent & Subsidiary Combined Cap Rule (母子公司联合仓位上限法则)<br>--------------------------------------------------<br>Where a book holds both a parent holdco and a listed subsidiary<br>that constitutes most of its value, COMBINED position cap<br>is the subsidiary's cap — NEVER the sum of both!<br>母公司与核心上市子公司视为同一风险暴露，联合仓位不得超过子公司单独上限！"]
    end

    Port --> Portfolio_Rules

    style Rule3_ParentSub fill:#ffe6e6,stroke:#cc0000,stroke-width:2px
    style Step10_Deliverables fill:#f9f9f9,stroke:#333,stroke-width:1px
```

---

## Summary of Core Principles / 核心原则总结

1. **Reconcile Before You Analyze (先勾稽，后分析)**: Step 2.5 takes 5 minutes and prevents the vast majority of critical errors.
2. **Normalize Before You Value (先归一化，后估值)**: Step 3.5 bridges accounting earnings to economic owner earnings.
3. **Placing Upstream Gates (双关口护航)**: Upstream gates safeguard downstream valuation from "garbage in, garbage out".
4. **Per-Share Economics Over Aggregates (每股价值高于总量增长)**: Dilution drag matters to existing shareholders.
5. **Parent & Subsidiary Risk Aggregation (母子公司合并风险敞口)**: Treat parent and major listed subsidiary as a single exposure.
