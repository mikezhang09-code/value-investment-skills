# Knowledge File Update Log — 27 July 2026 Session
# 知识库文件更新记录 — 2026年7月27日会话

**Scope / 范围:** One deep dive (China Taiping 0966.HK) plus a retrospective sweep of all financials in coverage, producing **two commits** across **five files**.
**Commits / 提交批次:** `2026-07-27` — CTIH deep dive · `2026-07-27 (b)` — Amendment #13 sweep and corrections
**Amendments / 修订编号:** **#13, #14, #15** (new) · **#11-R** (third case, no rule change) · **Checks 12, 13, 14** (new)

---

## 0. Overview / 概览

**EN —** Five files changed, all in the same direction: three framework files gained new binding rules, and the coverage record gained one new name plus seven sweep stamps. **All edits were pure insertions — no original content was deleted**, verified by heading-level diff against the pre-session copies. The session's unusual feature is that a rule adopted in the morning was **corrected by its own validation sweep in the afternoon** — see Part 6.

**中文 —** 共修改五个文件，方向一致：三个框架文件新增强制性规则，覆盖记录新增一只标的并为七只标的加注排查标记。**所有编辑均为纯插入 —— 未删除任何原有内容**，已通过与会话前副本的标题级差异比对验证。本次会话的特殊之处在于：上午采纳的一条规则，**在下午被其自身的验证排查所修正** —— 详见第六部分。

| File / 文件 | Amendments / 修订 | Size / 大小 |
|---|---|---|
| `SKILL.md` | **#13** (three-step: gate → arithmetic → resolution) | 31KB → **37KB** |
| `references/data-sources.md` | Warning Class G, classification gate, 4 checklist lines | 23KB → **28KB** |
| `references/intrinsic-value.md` | **#14** (Method 6 discount mechanism) | 30KB → **35KB** |
| `references/industry-playbooks.md` | **#15** (§F.8 UNRUNNABLE), #11-R third case | 54KB → **58KB** |
| `references/process-lessons.md` | Checks 12, 13, 14; sweep-backwards principle | 17KB → **24KB** |
| `command-center.md` / `.html` | CTIH as #50; 7 sweep stamps; 2 log entries | *gitignored — not in repo* |

> **Note / 说明:** `command-center.md` and `command-center.html` are excluded by `.gitignore` as live portfolio data. They are listed here for completeness of the session record only.
> `command-center.md` 与 `command-center.html` 已由 `.gitignore` 排除（属实盘持仓数据）。此处列出仅为保持会话记录完整。

---

## Part 1 — `SKILL.md`

### 1.1 Amendment #13 — senior-instrument adjustment to Step 2.5 Anchor 2 / 优先级资本工具对锚点二的调整

**EN —** Anchor 2 back-calculates shares as `profit attributable to owners ÷ basic EPS`. The numerator is **not** that figure as printed. Perpetual capital securities, AT1 notes and preference shares sit *inside* equity but rank **ahead of** ordinary shares; the issuer removes their distribution before striking basic EPS, even where the income statement does not show the deduction on its face.

**中文 —** 锚点二以「归母净利润 ÷ 基本每股收益」反算股数。但分子**并非**报表上直接印出的那个数字。永续资本证券、其他一级资本工具（AT1）与优先股在**形式上计入权益，实质上优先于普通股**；发行人在计算基本每股收益之前即已扣除其分派，即使利润表表面并未列示该扣除。

**Live derivation / 实战推导:** China Taiping FY2025. Naive back-check HK$27,059.28mn ÷ HK$7.251 = 3,731.8mn shares against a true count of **3,594.2mn — a 3.83% overstatement** — because HK$997.63mn of perpetual distribution had not been removed. Dividend-derived (3,594.0mn) and BVPS-derived counts agreed to 0.01%, which is what isolated the error to Anchor 2 alone.

**Second-order effect / 二阶影响:** reported embedded value per share HK$58.297 → **HK$53.85 ex-perpetual (−7.6%)**, and P/EV was one of five valuation methods.

**EN — Structurally different from the A+H trap.** CTIH has a single share class, a single listing and no A-share twin: **Anchor 4 was clean.** The trap lives in the **capital stack**, not the share register — a name can pass every share-class test and still fail here.

**中文 —— 与A+H陷阱在结构上不同。** 中国太平只有单一股份类别、单一上市地、无A股孪生股：**锚点四完全干净**。此陷阱藏在**资本结构**中，而非股东名册中 —— 一只标的可以通过全部股份类别检验，却仍在此处失守。

### 1.2 The classification gate — added the same day by the sweep / 分类闸口 —— 当日由排查新增

**EN —** #13 as first written had no gate, and would have false-alarmed on most of a financials sleeve. **The trap only exists where the instrument is classified as equity.** Step 1 is now:

**中文 —** #13 最初的写法没有闸口，会在整个金融板块的多数标的上产生误报。**只有当该工具被分类为权益时，陷阱才存在。** 现在的第一步是：

```
EQUITY-classified    → trap LIVE. Distribution NOT in net profit. Subtract it.
                       权益类 → 陷阱成立，分派未计入净利润，须扣除。

LIABILITY-classified → NO TRAP. Coupon already in interest expense.
                       负债类 → 无陷阱，票息已列入利息支出。
```

**EN —** Indian bank AT1 sits under *borrowings* (RBI Basel III framework, Banking Regulation Act schedule format); mainland capital supplementary bonds are subordinated debt. Both are liability-classified. HK/PRC insurer **perpetual capital securities** are equity-classified and do create the trap. **The instrument's name tells you nothing; its classification tells you everything.**

**中文 —** 印度银行的AT1列于*借款*科目（依印度央行巴塞尔III框架及《银行业监管法》报表格式）；境内资本补充债券属次级债。两者均为负债类。而港/中保险公司的**永续资本证券**属权益类，确实会产生陷阱。**工具的名称什么也说明不了，其分类说明一切。**

### 1.3 The resolution statement / 分辨率声明

**EN —** Anchor 2's precision is bounded by the **decimal places in reported EPS**, and across the book it varies by roughly two orders of magnitude:

**中文 —** 锚点二的精度受**公告每股收益小数位数**约束；在整个覆盖范围内，该精度差异接近两个数量级：

```
resolution (±%) = (0.5 × 10^−dp) ÷ EPS × 100

  China Taiping 中国太平  HK$7.251 (3dp) → ±0.007%   detects anything 任何幅度
  PICC P&C     中国财险   RMB 1.815 (3dp) → ±0.028%   detects ~0.1%
  PICC Group   中国人保   RMB 1.04  (2dp) → ±0.481%   detects only >1% 仅能检出1%以上
```

**EN —** Never report an unqualified pass. Report *"passes at ±X% resolution"* — which means "no distortion above X%", not "no distortion". This is why CTIH was catchable: its 3.83% gap was **~550×** the diagnostic's resolution. The same proportional error on a low-EPS name would have hidden completely.

**中文 —** 绝不可报告无条件通过。应报告**「在±X%分辨率下通过」**—— 其含义是「不存在超过X%的扭曲」，而非「不存在扭曲」。这正是中国太平能被检出的原因：其3.83%的偏差约为该检验分辨率的**550倍**。同样比例的错误若发生在每股收益基数较低的标的上，将被完全掩盖。

---

## Part 2 — `references/data-sources.md`

### 2.1 Warning Class G — perpetual / AT1 / preference capital / 警示类别G

**EN —** A new warning class, **explicitly orthogonal to Classes A–F**. Those cover the share register; this covers the capital stack. Includes a "who carries them / assume present until checked" list — mainland Chinese insurers and banks, Indian banks, European banks, utilities and REITs with hybrid capital — and a pointer to **subsidiary-level perpetuals sitting inside non-controlling interests**, which never touch the parent equity note and are therefore easy to miss.

**中文 —** 新增警示类别，**与类别A–F明确正交**。后者针对股东名册，本类别针对资本结构。包含「谁会持有／未经核实即假定存在」清单 —— 中国境内保险与银行、印度银行、欧洲银行、持有混合资本的公用事业与REITs —— 并特别提示**藏于少数股东权益之中的子公司层面永续工具**，此类工具从不出现在母公司权益附注中，极易遗漏。

### 2.2 Four new pre-verdict checklist lines / 四条新增的结论前核对项

**EN —** One of them is not about #13 at all, and is the sweep's most transferable output:

**中文 —** 其中一条与#13毫无关系，却是本次排查最具可迁移性的产物：

> **Book-value denominator READ FROM A FILING, not derived from a ratio, and its GAAP basis named where the issuer publishes more than one (e.g. 20-F filers: US GAAP vs local).**
>
> **账面价值分母须直接读取自原始文件，而非由比率倒算；当发行人公布一套以上口径时（如20-F申报人：美国准则 vs 当地准则），必须指明所采用的口径。**

---

## Part 3 — `references/intrinsic-value.md`

### 3.1 Amendment #14 — a Method 6 discount requires a named enforcing mechanism / 方法六折价须有明确的执行机制

**EN —** Do not apply a holding-company discount because the entity is structurally a holding company. **Structural resemblance is not a mechanism.** Name which is present, and size the discount to that:

**中文 —** 不得仅因主体在结构上属控股公司便施加控股公司折价。**结构相似不等于存在机制。** 必须指明以下哪一项成立，并据此确定折价幅度：

| # | Mechanism / 机制 | What makes it real / 何以成立 |
|---|---|---|
| 1 | Separately listed subsidiary / 子公司单独上市 | The stub is directly observable — you are *measuring* the discount, not assuming it / 剩余部分可直接观察 —— 是在*测量*折价，而非假定 |
| 2 | Cross-listing arbitrage (A/H, ADR) / 跨市场套利 | An observable price on the same claim in another venue / 同一权益在另一市场的可观察价格 |
| 3 | Documented cash-flow leakage / 有据可查的现金流漏损 | Minority leakage or trapped capital **not already removed** by attributable figures / 归属口径**尚未扣除**的少数股东漏损或受困资本 |

**EN —** If none is present, apply no discount. Where the analysis already works from figures *attributable to owners*, leakage has been deducted once — applying a discount on top **double-counts it**. The list is **explicitly non-exhaustive**; a fourth candidate (controlling shareholder with a demonstrated history of value transfer) is a **governance** discount with different sizing logic and must be argued separately rather than folded in.

**中文 —** 若无任何一项成立，则不施加折价。当分析本身已采用*归属于母公司股东*的口径时，漏损已扣除过一次 —— 再叠加折价即为**重复计算**。该清单**明确为非穷尽式**；第四个候选机制（有价值转移历史记录的控股股东）属**治理**折价，其幅度逻辑不同，必须单独论证，不得并入。

**Live derivation / 实战推导:** CTIH vs PICC Group. Both are holding companies over regulated insurers, and the reflex was to carry the discount across. PICC Group's 22% is *enforced* by a separately listed subsidiary (PICC P&C, 2328.HK) plus an A/H pair. CTIH has no listed subsidiary, no A-share twin, and leakage already removed. **No discount applied.** A reflexive 15% would have cut base FV HK$24.51 → ~HK$20.83, **to roughly spot**, turning a 15%-MoS WATCHLIST into a false PASS on a manufactured number.

**Companion rule / 配套规则:** **decompose bundled discounts.** A single range covering "SOE / holdco / leverage" is three claims wearing one number. / **拆解捆绑折价。** 用单一区间涵盖「国企／控股／杠杆」，是三项主张共用一个数字。

---

## Part 4 — `references/industry-playbooks.md`

### 4.1 Amendment #15 — §F.8 outcome set extended to UNRUNNABLE / §F.8结论集新增「无法执行」

**EN —** The test can **PASS**, **FAIL**, or be **UNRUNNABLE**. Where the issuer does not disclose the required inputs: record it as unrunnable, **name the missing disclosure**, keep the headline out of fair value, and **log the gap in the moat and management assessment** — an issuer that withholds the split is telling you something about disclosure quality, which is itself a governance datapoint.

**中文 —** 该检验可以**通过**、**未通过**，或**无法执行**。当发行人未披露所需输入项时：记录为无法执行，**指明缺失的披露内容**，将表面数据排除于合理价值之外，并**将该缺口计入护城河与管理层评估** —— 拒绝披露拆分数据的发行人，正在告诉你关于其披露质量的信息，而这本身就是一项治理数据点。

> **Never collapse UNRUNNABLE into PASSED** (the charitable error) **or into FAILED** (the lazy one). They are different information and justify different position sizes.
>
> **绝不可将「无法执行」并入「通过」**（宽容型错误）**或并入「未通过」**（懒惰型错误）。三者是不同的信息，对应不同的仓位规模。

**Live contrast / 实战对照:** **PICC P&C** — the test **ran and failed**: expense ratio moved, loss ratio did not, so the improvement was cost-cutting. **Taiping Insurance (P&C arm of CTIH)** — **UNRUNNABLE**: only a headline combined ratio (98.8%, −1.3pt), no expense/loss split at all. Conflating the two would have credited CTIH with PICC P&C's *finding* while it had produced no finding at all.

### 4.2 Amendment #11-R — third live case, and the first PASS / 第三个实战案例，且为首次通过

**EN —** CTIH **cleared** the gate — g = ROE 11.5% × (1 − 0.70 payout) = **8.05%** against r = 11.0%, **(r − g) = +2.95pp** — where HDB and IBN both failed it. It passed **precisely because ROE is low and payout is high**, which is the perverse property #11-R was written to capture, now **observed from the passing side** rather than inferred from two failures. The rule has been tested on both sides of the threshold and **stands as written — no change.**

**中文 —** 中国太平**通过**了该闸口 —— g = 净资产收益率11.5% × (1 − 派息率0.70) = **8.05%**，对应r = 11.0%，**(r − g) = +2.95个百分点** —— 而印度住房开发金融银行与印度工业信贷投资银行均未通过。它之所以通过，**恰恰因为净资产收益率低而派息率高**，这正是#11-R所要捕捉的悖论性质，如今**从通过一侧被观察到**，而非从两次失败中推断得出。该规则已在阈值两侧完成检验，**维持原文不变 —— 无需修订。**

**Second observation / 第二项观察:** where **ROE ≈ r**, the mandatory fade ladder is unusually **fade-*insensitive***. CTIH's full ladder spanned 282% (HK$16.79–64.17), but the *defensible* rungs clustered tightly at **HK$25–33**, against HDB's ₹542–1,051 (94%) swing. **The ladder's informativeness scales with (ROE − r)** — printing it remains mandatory, but where ROE ≈ r it is *confirming* the answer rather than *choosing* it, and the analyst should say so rather than presenting the wide headline spread as live uncertainty.

---

## Part 5 — `references/process-lessons.md`

### 5.1 Check 12 — price vintage and ex-dividend / 价格时点与除息

**EN —** Staleness has now bitten twice (sportswear v1/v2; PICC P&C). The dividend leg is the newer half: on CTIH a HK$1.23 ex-div step moved margin of safety **15.0% → 20.0%** on no news whatsoever — a third of the way to the entry threshold. For high-payout financials the step-down is verdict-relevant by itself.

**中文 —** 价格陈旧已两次造成损失（运动服饰v1/v2；中国财险）。股息一环是较新的另一半：中国太平1.23港元的除息使安全边际由**15.0%升至20.0%**，而期间毫无消息面变化 —— 已走完通往入场阈值三分之一的距离。对高派息金融股而言，除息落差本身即可影响结论。

### 5.2 Check 13 — record-keeping assertion / 记录一致性断言

**EN —** The command-centre header read **46** while the JSON block already held **49** entries — stale across roughly three sessions, because it is prose, not data, and nothing in the validation chain touched it.

**中文 —** 指挥中心表头显示**46**，而JSON数据块中已有**49**条记录 —— 陈旧状态延续约三个会话，原因在于表头是文字而非数据，验证链条中没有任何环节触及它。

```
assert header_universe_size == len(json_data) == master_table_row_count
```

**EN —** The instructive part: cross-file parsed-dict equality passed perfectly and caught nothing, because **agreement between the two checked artifacts said nothing about the unchecked third.** Generalize: when adding a validation, ask what the check *cannot* see, and whether anything downstream relies on it anyway.

**中文 —** 最具启发性的地方在于：跨文件解析字典相等性检验完美通过却毫无所获，因为**两个被检对象彼此一致，并不能说明第三个未被检查的对象是否正确。** 推而广之：新增验证时，应追问该检验*看不见*什么，以及下游是否仍在依赖它。

### 5.3 Check 14 — is the book-value denominator real? / 账面价值分母是否真实？

**EN —** Three failure modes, all found live in the sweep, **none of them the one being hunted**: (1) **derived, not read** — was BVPS taken off a balance sheet, or backed out of ROE? (2) **GAAP basis unnamed** — does the issuer publish more than one equity figure? (3) **single-sourced** — one aggregator, never tied to a filing? *Name the basis, name the source, read it to a filing.* A denominator that cannot survive those three questions makes every multiple built on it decorative.

**中文 —** 三种失效模式，均在排查中实盘发现，**且没有一种是原本要找的那一种**：(1) **倒算而非读取** —— 每股净资产是取自资产负债表，还是由净资产收益率反推？(2) **未指明会计准则口径** —— 发行人是否公布了一套以上的权益数字？(3) **单一来源** —— 仅凭一家数据商，从未与原始文件对应？*指明口径、指明来源、回溯至原始文件。* 一个经不起这三问的分母，会使建立其上的所有倍数沦为装饰。

### 5.4 Validate new rules by sweeping backwards, not by waiting forwards / 以回溯排查验证新规则，而非向前等待

**EN —** When a rule is derived from a single case, the instinct is to mark it unvalidated and wait for the next name that triggers it. **Sweep the existing book instead.** The retrospective run is faster, bounded (the population is known), and tests the rule against more variation than any single future case.

**中文 —** 当一条规则源自单一案例时，本能反应是标注为「未验证」，等待下一只触发它的标的。**应改为排查现有覆盖范围。** 回溯执行更快、范围有界（样本总体已知），且能让规则接触到比任何单一未来案例更丰富的变异。

**EN —** *Derivation:* #13 was adopted with "validates on the next issuer carrying perpetual or AT1 capital." Sweeping the seven financials already in coverage instead produced, within hours: (1) **two defects in the rule itself**; (2) confirmation that **no existing entry was corrupted**; and (3) a **larger, unrelated error** that no #13-triggered future case would ever have surfaced. **A rule derived from one case encodes that case's peculiarities as though they were general.** Only contact with the rest of the population separates the two — and that population is already sitting in the book.

**中文 —** *推导过程：* #13采纳时标注为「待下一只持有永续或AT1资本的标的验证」。改为排查覆盖范围内已有的七只金融股后，数小时内即产生：(1) **规则自身的两处缺陷**；(2) 确认**既有记录未被污染**；(3) 一个**更大的、无关的错误**，而任何由#13触发的未来案例都永远不会使其浮现。**源自单一案例的规则，会把该案例的特殊性当作普遍性编码进去。** 唯有与总体其余部分接触才能将两者区分 —— 而这个总体，早已躺在覆盖记录之中。

---

## Part 6 — The Amendment #13 Sweep / 修订条款#13专项排查

**EN —** Full bilingual findings are in `sweep_amendment13_2026-07-27_bilingual.md`. Summary: **7 financials swept, no #13 error anywhere, CTIH remains the only case.** The sweep's value was not the null result but the three things it produced on the way — two defects in #13 (Parts 1.2 and 1.3 above), a new general check (Part 5.3), and one material unrelated finding:

**中文 —** 完整双语结论见 `sweep_amendment13_2026-07-27_bilingual.md`。摘要：**排查七只金融股，未发现任何#13类错误，中国太平仍是唯一个案。** 本次排查的价值不在于这一「无发现」结论，而在于过程中产生的三项成果 —— #13的两处缺陷（上文1.2与1.3）、一项新的通用检验（5.3），以及一项重大的无关发现：

> **ICICI Bank (#13):** the FY2026 Form 20-F discloses **US GAAP equity ₹409,093cr against Indian GAAP net worth ₹363,060cr — a 12.7% gap**, roughly 3× the CTIH #13 effect. The single-sourced **BVPS ₹527 ▲ sits between the two bases.** Basis unidentified, plausible range ~±12% on the single input driving the entire valuation. **IBN's fair value and every P/B are provisional pending resolution.**
>
> **印度工业信贷投资银行（#13）：** FY2026年度20-F文件披露**美国准则股东权益₹409,093千万卢比，对应印度准则合并净资产₹363,060千万卢比 —— 差距12.7%**，约为中国太平#13影响的3倍。来源单一的**每股净资产₹527 ▲恰好落在两套口径之间。** 口径未定，合理区间约±12%，而这一输入项独自驱动整个估值。**该标的的合理价值及全部市净率在此问题解决前均属暂定。**

---

## Part 7 — What Will Actually Be Different Next Run / 下次分析将有何实质不同

| Trigger / 触发条件 | Old behaviour / 原有做法 | New behaviour / 新做法 |
|---|---|---|
| Any financial with hybrid capital / 任何持有混合资本的金融股 | Anchor 2 run naively / 直接执行锚点二 | Classification gate first; arithmetic only if equity-classified / 先过分类闸口，仅权益类才执行算术 |
| Any Anchor 2 result / 任何锚点二结果 | "Passes" / 「通过」 | "Passes at ±X% resolution" / 「在±X%分辨率下通过」 |
| Any holdco SOTP / 任何控股公司分部加总 | Discount applied by analogy / 类比施加折价 | Name the mechanism or apply none / 指明机制，否则不施加 |
| A §F-series test lacking inputs / 缺少输入项的§F系列检验 | Forced into pass or fail / 强行归入通过或未通过 | Recorded UNRUNNABLE, logged against disclosure quality / 记为无法执行，并计入披露质量 |
| Any P/B-anchored valuation / 任何以市净率为锚的估值 | BVPS taken as given / 直接采用每股净资产 | Check 14: basis named, source named, read to filing / 检验14：指明口径与来源，回溯原始文件 |
| A new single-case rule / 新的单案例规则 | Marked unvalidated, wait / 标注未验证，等待 | Sweep the existing book immediately / 立即回溯排查现有覆盖范围 |

---

## Part 8 — Verification Status / 验证状态

**EN —** All five knowledge files re-uploaded to Project Knowledge and confirmed **byte-identical (SHA-256)** to the versions committed here. Command-centre validation: 50 entries in Markdown, HTML and master table; IDs contiguous 1–50; **cross-file parsed-dict equality `True`**; **Check 13 passes on its first live run** (header == data == table == 50). All seven swept names confirmed **unchanged** in verdict, conviction and fair value — the sweep added evidence, it did not move a number.

**中文 —** 五个知识库文件均已重新上传至项目知识库，并确认与此处提交版本**逐字节一致（SHA-256）**。指挥中心验证：Markdown、HTML与主表均为50条记录；ID连续1–50；**跨文件解析字典相等性为`True`**；**检验13在首次实盘运行中通过**（表头 == 数据 == 表格 == 50）。经排查的七只标的，其结论、信心度与合理价值均确认**未发生变化** —— 本次排查增加的是证据，而非改动了任何数字。

### ⚠ Open items / 待办事项

**EN —**
1. **ICICI BVPS basis — highest priority in the book.** ±12% range on the denominator driving the entire valuation. The one open item that could move a fair value.
2. **PICC P&C:** read BVPS from the FY2025 balance sheet (currently ▲ derived from ROE); obtain reported basic EPS to close Test B.
3. **AT1 classification for HDB/IBN** rests on tier-3 evidence — structurally sound and doubly protected by magnitude (~0.5% of capital), but not read line-by-line to either balance sheet.

**中文 —**
1. **印度工业信贷投资银行每股净资产口径 —— 覆盖范围内最高优先级。** 驱动整个估值的分母存在±12%区间。这是唯一可能改变合理价值的待办项。
2. **中国财险：** 从FY2025资产负债表读取每股净资产（现为▲由净资产收益率倒算）；取得公告口径基本每股收益以完成检验B。
3. **两家印度银行的AT1分类**建立在三级证据之上 —— 结构逻辑成立，且因规模微小（约占资本0.5%）而具双重保护，但尚未逐行核对至任一家银行的资产负债表。
