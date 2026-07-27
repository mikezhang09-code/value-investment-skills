# Knowledge File Update Log — 26 July 2026 Session
# 知识库文件更新记录 — 2026年7月26日会话

**Scope / 范围:** Two deep dives (HDFC Bank refresh, ICICI Bank validation run) produced **two commits** across **five files**.
**Commits / 提交批次:** `2026-07-26 (c)` — HDB session · `2026-07-26 (d)` — IBN validation session
**Amendments / 修订编号:** **#9, #10, #11 → #11-R, #11-R(b), #12, #9-R**

---

## 0. Overview / 概览

**EN —** Five files changed. Three are framework files (permanent rules); two are the coverage record. **All edits were pure insertions — no original content was deleted**, verified by line-level diff against the pre-session copies. The one exception is a three-line relabel in `industry-playbooks.md` §F.7, where `*Check:*` became `*Check (harvesting):*` with substantively identical text.

**中文 —** 共修改五个文件。其中三个是框架文件（永久性规则），两个是覆盖记录。**所有编辑均为纯插入 —— 未删除任何原有内容**，已通过与会话前副本的逐行差异比对验证。唯一例外是 `industry-playbooks.md` §F.7 中三行的重新标注，`*Check:*` 改为 `*Check (harvesting):*`，实质内容完全相同。

| File / 文件 | Amendments / 修订 | Size / 大小 |
|---|---|---|
| `industry-playbooks.md` | #9, #9-R, #10, #11 note, **#11-R(b)** | 41KB → **52KB** |
| `intrinsic-value.md` | #11 → **#11-R** | 22KB → **28KB** |
| `earnings-quality-and-distortions.md` | #12 | 31KB → **34KB** |
| `command-center.md` | HDB row, IBN row, stale-line fix, 2 log entries | 108KB → **111KB** |
| `command-center.html` | HDB row, IBN row (DATA array) | 94KB |

---

## Part 1 — `industry-playbooks.md`

### 1.1 Amendment #9 — B-1 positive-case diagnostic (§F.7) / B-1正向诊断

**EN —** B-1 previously had a single `*Check:*` — a harvesting detector only. It now has **two checks**, mirroring the structure amendment #3 gave I-1.

**中文 —** B-1 此前只有单一的 `*Check:*` —— 仅作为「收割拨备」的探测器。现在拥有**两项检验**，结构对应第3号修订赋予I-1的形式。

**Added / 新增:**
- `*Check (harvesting):*` — the original test, relabelled / 原检验，重新标注
- `*Check (integrity — the positive case):*` — **new** / **新增**
- A both-directions signal table / 双向信号表
- **The core diagnostic** — compare the size of the consensus miss to the size of the unreleased buffer / **核心诊断法** —— 将「不及预期的金额」与「未释放缓冲的规模」相比
- Live case: HDB Q1 FY27 (₹272cr miss vs ~₹9,000cr buffer; 3.0% would have made it a beat) / 实战案例
- ⚠ Caveat: where the buffer balance is **inferred rather than confirmed**, mark ▲, log under RF-1, and state the positive reading as **conditional** / ⚠ 提示：当缓冲余额为**推断而非确认**时，标记▲，记入RF-1，并将正向解读表述为**有条件的**

### 1.2 Amendment #9-R — the beat branch (commit d) / 「超预期」分支

**EN —** The original #9 construction **assumed a miss** and was mathematically undefined on IBN, which beat consensus. Split into two branches:

**中文 —** 原#9的构造**假定了「不及预期」**，在超预期的IBN上数学上无定义。因此拆分为两个分支：

| Situation / 情形 | Test / 检验 |
|---|---|
| **On a MISS / 不及预期时** | Did management decline a release that would have converted it? / 管理层是否拒绝了本可扭转结果的拨备释放？ |
| **On a BEAT / 超预期时** | Was the beat **earned or manufactured**? Test PAT growth against pre-provision profit growth, and whether the buffer is intact / 该超预期是**挣来的还是做出来的**？检验净利润增速与拨备前利润增速是否匹配，缓冲是否完好 |

**EN —** The miss branch is **probative** (management accepted a visible cost); the beat branch is **confirmatory** only.
**中文 —** 「不及预期」分支具有**证明力**（管理层承担了可见代价）；「超预期」分支仅具**佐证性**。

### 1.3 Amendment #10 — post-merger funding-mix rule (§F.2) / 并购后融资结构规则

**EN —** New subsection. Requires margin compression after a bank merger to be **decomposed before any of it is assumed to reverse**.

**中文 —** 新增小节。要求银行并购后的息差压缩，**在假设其中任何部分会逆转之前，必须先行分解**。

| Component / 构成 | Side / 端 | Nature / 性质 | Reverses? / 会逆转吗？ |
|---|---|---|---|
| CD-ratio normalisation / 存贷比正常化 | Asset / 资产端 | Transitional / 暂时性 | **Yes / 会** |
| High-cost acquired borrowings rolling off / 高成本收购借款到期 | Liability / 负债端 | Transitional / 暂时性 | **Yes / 会** |
| **CASA / deposit-mix change / 活期存款结构变化** | **Liability / 负债端** | **Structural / 结构性** | **No / 不会** |

**The rule / 规则:** **Never assume a merged bank recovers to the acquirer's pre-merger NIM.** Track the CASA ratio — and specifically whether CASA growth is running ahead of or behind time-deposit growth — as the deciding series.
**绝不假设合并后的银行能恢复到收购方并购前的净息差。** 以CASA比率（尤其是CASA增速相对定期存款增速的快慢）作为决定性跟踪序列。

### 1.4 Amendment #11-R(b) — §F.5 method table corrected (commit d) / §F.5方法表更正

> **EN — This fixes a contradiction the previous commit created.** After #11 was added, §F.5 still listed *"P/B calibrated to sustainable ROE"* as the **Primary anchor** for both insurance and banking — directly contradicting the new rule. Corrected in the same commit as #11-R.
>
> **中文 — 这修正了上一次提交自身制造的矛盾。** #11加入后，§F.5仍将「按可持续ROE校准的市净率」列为保险与银行业的**首要锚定方法** —— 与新规则直接冲突。已在#11-R的同一次提交中更正。

| Method / 方法 | Before / 此前 | After / 此后 |
|---|---|---|
| P/B calibrated to sustainable ROE | **Primary anchor** | **Conditional** — void where g ≥ r / **有条件** —— 当 g ≥ r 时无效 |
| Residual income with explicit moat-calibrated fade | *(not listed)* / *（未列出）* | **Primary anchor** / **首要锚定方法** |

### 1.5 File-hygiene defect logged, not silently fixed / 已记录（而非默默修复）的文件卫生缺陷

**EN —** The `2026-07-26 (b)` entries reference **§F.3** and **§F.4**, but **no such headers exist** — the file runs §F.2 → §F.5, and that content sits inside §F.2. Amendment #10 was therefore placed in §F.2, and the dangling reference was **documented rather than propagated**. Open item: either create the headers or correct the references — **do not add more of them**.

**中文 —** `2026-07-26 (b)` 的条目引用了 **§F.3** 与 **§F.4**，但**这两个标题并不存在** —— 文件从§F.2直接跳到§F.5，相关内容实际位于§F.2内。因此第10号修订被放置于§F.2，且该悬空引用被**记录下来而非继续沿用**。待办：要么创建这两个标题，要么修正引用 —— **不要再增加此类引用**。

---

## Part 2 — `intrinsic-value.md`

### 2.1 Amendment #11 → #11-R: from provisional to binding / 由暂行升级为强制

**EN —** This is the **largest single change of the session.** The rule was added on the HDB run flagged `⚠ UNVALIDATED`, validated on IBN the same day, and **promoted to binding — with its threshold rewritten because the original was too weak.**

**中文 —** 这是本次会话**最大的单项变更。** 该规则在HDB分析中加入时标记为 `⚠ 未验证`，同日在IBN上完成验证，并**升级为强制性 —— 且因原阈值过于宽松而被重写。**

| | Original #11 / 原#11 | **Revised #11-R / 修订后#11-R** |
|---|---|---|
| Status / 状态 | ⚠ UNVALIDATED / 未验证 | **VALIDATED · BINDING / 已验证·强制** |
| Threshold / 阈值 | (r − g) < 3pp → *demote* / 降级 | **g ≥ r → *VOID* / 无效** |
| Expressed as / 等价表述 | — | **ROE × (1 − payout) ≥ r** |
| Scope / 适用范围 | "do not extend beyond financials" / 「勿超出金融业」 | General to financials — HDB was the *milder* case / 普遍适用于金融业 —— HDB反而是较轻的一例 |

**The payout requirement table added / 新增的派息率要求表** — the method requires **payout > 1 − r/ROE** / 该方法要求**派息率 > 1 − r/ROE**:

| Bank ROE / 银行ROE | Min payout for the method to function (r=12%) / 方法有效所需最低派息率 |
|---|---|
| 14% | 14.3% |
| **16%** | **25.0%** |
| 18% | 33.3% |
| 20% | 40.0% |

### 2.2 The perverse property — the finding that matters / 悖论性质 —— 最重要的发现

> **EN —** Higher ROE and lower payout are **the two defining features of a great compounder**, and **both push g up toward and past r.** Justified P/B is most reliable on mediocre, high-payout banks and **breaks down entirely on exactly the franchises a value investor most wants to own.**
>
> **中文 —** 更高的ROE与更低的派息率是**优秀复利机器的两大定义性特征**，而**两者都把g推高、逼近并越过r。** 合理市净率法在平庸的高派息银行上最可靠，却**恰恰在价值投资者最想拥有的特许经营权上彻底失效。**

**EN —** This was visible from the algebra before either deep dive was run. It was not run.
**中文 —** 这一点从代数上在两次深度分析之前就可见。但当时并未演算。

### 2.3 The four-point rule now in force / 现行四条规则

1. **EN —** No primary weight where ROE × (1 − payout) ≥ r − 1pp. **中文 —** 当 ROE × (1−派息率) ≥ r − 1个百分点时，不得作为主要权重。
2. **EN —** Where **g ≥ r the method is VOID, not demoted** — do not report the output. **中文 —** 当 **g ≥ r 时该方法无效（而非降级）** —— 不得报告其输出。
3. **EN —** Fade-sensitivity ladder mandatory; **where the no-fade rung is undefined, state it as undefined rather than omitting the row** — its absence is itself the diagnostic. **中文 —** 衰减敏感度阶梯为强制项；**当「不衰减」一档无定义时，须明确标注为「无定义」而非省略该行** —— 它的缺失本身就是诊断信号。
4. **EN —** Primary anchor is **residual income with an explicit, moat-calibrated fade**. **中文 —** 首要锚定方法为**带明确、按护城河校准衰减的剩余收益法**。

### 2.4 Comparative evidence table added / 新增对照证据表

| | HDB | IBN |
|---|---|---|
| g = ROE × retention / g = ROE × 留存率 | 15.0% × 68.1% = **10.21%** | 16.0% × 84.5% = **13.53%** |
| (r − g) at r = 12% | **+1.78pp** — fragile / 脆弱 | **−1.53pp** — broken / 失效 |
| Justified P/B / 合理市净率 | 2.68× | **−1.62× (negative / 负值)** |
| Fade-ladder spread / 衰减阶梯区间 | +39% | **+75%** |
| No-fade bound / 不衰减上界 | ₹1,051 | **does not exist / 不存在** |

**Materiality / 重要性:** applying the rule cut base fair value **~33% on HDB and ~17% on IBN**, with negligible FX contribution. **It changes verdicts.** / 应用该规则使基准内在价值**在HDB上下调约33%，在IBN上下调约17%**，汇率贡献可忽略。**它会改变结论。**

### 2.5 Change-log ordering defect — flagged, not fixed / 变更日志顺序缺陷 —— 已标记，未修复

**EN —** Entries in this file now run **(c) → [unsuffixed] → (b)**. The unsuffixed entry should logically be **(a)**. `industry-playbooks.md` is clean by contrast: (d) → (c) → (b) → (a). Flagged here rather than silently corrected, consistent with how the §F.3 defect was handled. **Cosmetic; fix on next touch.**

**中文 —** 该文件的条目顺序现为 **(c) → [无后缀] → (b)**。无后缀条目按逻辑应为 **(a)**。相比之下 `industry-playbooks.md` 是干净的：(d) → (c) → (b) → (a)。此处选择标记而非默默更正，与处理§F.3缺陷的方式保持一致。**属外观问题；下次接触时修复。**

---

## Part 3 — `earnings-quality-and-distortions.md`

### Amendment #12 — Corporate-Transaction Breaks / 公司交易断点

**EN —** The transition-break rule previously covered **accounting standards only** (IFRS 17, IFRS 9, IFRS 16, IFRS 15). It now extends to **corporate transactions** — merger, demerger, spin-off, disposal — on the same reasoning: *the reporting entity on one side of the line is not the reporting entity on the other.*

**中文 —** 「转换断点」规则此前**仅涵盖会计准则**（IFRS 17、IFRS 9、IFRS 16、IFRS 15）。现扩展至**公司交易** —— 合并、分立、分拆、重大处置 —— 依据同一逻辑：*断点一侧的报告主体，与另一侧的报告主体并非同一个。*

> **The binding test is the issuer's own statement. / 约束性检验是发行人自己的声明。**
>
> **EN —** Where a company states in its own filings or investor materials that prior periods are not comparable, **that statement is binding on the analysis.** It is **not** a boilerplate disclaimer to be noted and stepped past. Treat it with the same force as an IFRS 17 adoption date.
>
> **中文 —** 当公司在自己的申报文件或投资者材料中声明前期数据不可比时，**该声明对分析具有约束力。** 它**不是**可以「记录一下然后跳过」的样板免责声明。应赋予其与IFRS 17实施日期同等的效力。

| Transaction type / 交易类型 | What breaks / 什么被打断 |
|---|---|
| Merger / large acquisition / 合并·重大收购 | Every ratio with a balance-sheet denominator; margin structure; funding mix for financials / 所有以资产负债表为分母的比率；利润率结构；金融机构的融资结构 |
| Demerger / spin-off / 分立·分拆 | Revenue base, margin mix, entire per-share series / 收入基础、利润率结构、全部每股数据序列 |
| Major disposal / 重大处置 | Revenue and segment continuity; often the ROE denominator / 收入与分部连续性；通常还有ROE的分母 |

**Live case / 实战案例:** HDFC Ltd merged into HDFC Bank on **1 July 2023**; the bank's own deck states *"Prior period numbers are not comparable."* A 2026 analysis therefore has a comparable window of **FY24–FY27 — three years, not ten.** / HDFC Ltd于**2023年7月1日**并入HDFC银行；该行自己的演示材料写明「前期数据不可比」。因此2026年的分析可比窗口为 **FY24–FY27 —— 三年，而非十年。**

---

## Part 4 — `command-center.md` / `command-center.html`

### 4.1 Row updates / 行更新

| id | Name | Before / 此前 | After / 此后 |
|---|---|---|---|
| **2** | HDFC Bank (HDB) | BUY 8/10 · FV $31.23 · px $24.45 · MoS +24% · cap 6% | **HOLD 6/10** · FV **$21.00** · px $23.13 · MoS **−9.2%** · floor $12.24 · cap **3–4%** |
| **13** | ICICI Bank (IBN) | WATCHLIST 7/10 · FV $27.93 · px $25.86 · MoS +8% | **WATCHLIST 7/10** · FV **$23.04** · px $29.76 · MoS **−22.6%** · floor $14.86 · cap **3–4%** |

**EN —** Both are **replacements, not insertions** — the universe remains at **49** names, ids 1–49 contiguous, and the MD JSON block and HTML DATA array were verified byte-identical after parsing.

**中文 —** 两者均为**替换而非新增** —— 覆盖范围仍为 **49** 只，id 1–49 连续无缺口，且MD的JSON块与HTML的DATA数组在解析后经验证完全一致。

⚠ **EN —** Both entries carry an explicit cross-cap: **HDB + IBN are one country/sector exposure — combined cap ≤7%, not the sum.**
⚠ **中文 —** 两条记录都带有明确的交叉上限：**HDB与IBN属同一国别／行业敞口 —— 合计上限 ≤7%，而非各自相加。**

### 4.2 Stale-line correction / 过期表述更正

**EN —** The HDB change-log entry originally ended *"Playbook amendments **A–D proposed**."* By the time the IBN run began this was false on two counts — they had been **applied**, and they had been **renumbered #9–12** to continue the PICC series. Corrected to read *"Playbook amendments **#9–12 APPLIED**"* with the renumbering explained and a pointer to the `industry-playbooks.md` change log.

**中文 —** HDB的变更日志条目原本以「**拟议**框架修订 A–D」结尾。到IBN分析开始时，这在两方面已不成立 —— 它们已被**应用**，且已**重新编号为 #9–12** 以延续PICC系列。现更正为「框架修订 **#9–12 已应用**」，并说明了重新编号的缘由及指向 `industry-playbooks.md` 变更日志的引用。

> **EN —** This is the **same defect class** as the dangling §F.3 reference: a log entry written at proposal time and never reconciled once the work landed. Worth watching for.
>
> **中文 —** 这与悬空的§F.3引用属于**同一类缺陷**：在「提议阶段」写下的日志条目，在工作落地后从未回头对齐。值得警惕。

### 4.3 New change-log entries / 新增变更日志条目

| Date / 日期 | Content / 内容 |
|---|---|
| `2026-07-26` | HDB downgrade, 3-gate root cause, B-1 positive clearance, reverse-DCF inversion, amendments #9–12 |
| `2026-07-26 (b)` | IBN deep dive + **#11 validation result**, #11-R, #11-R(b), #9-R, RF-4 double hit, RF-1 BVPS caveat |

---

## Part 5 — What Will Actually Be Different Next Run / 下次分析将有何实质不同

**EN —** The most useful summary is not what was written but **what behaviour changes.**
**中文 —** 最有用的总结不是「写了什么」，而是**哪些行为会改变。**

| # | Next time I analyse… / 下次分析…时 | The framework now forces / 框架现在强制要求 |
|---|---|---|
| 1 | **Any bank or insurer / 任何银行或保险公司** | Compute **g = ROE × (1 − payout)** *first*. If g ≥ r, justified P/B is **void** and must not be reported — residual income with explicit fade becomes the primary anchor / 先计算 **g = ROE × (1−派息率)**。若 g ≥ r，合理市净率**无效**且不得报告 —— 改以带明确衰减的剩余收益法为首要锚定 |
| 2 | **Any financial valued on P/B or RI / 任何以市净率或剩余收益法估值的金融机构** | Print the **fade-sensitivity ladder**, including a row for the no-fade bound even when it is undefined / 必须列出**衰减敏感度阶梯**，包括「不衰减」一行——即使其无定义也要标注 |
| 3 | **A bank that missed consensus / 不及预期的银行** | Compare the miss to the size of any unreleased discretionary buffer / 将差额与任何未释放的可裁量缓冲规模相比 |
| 4 | **A bank that beat consensus / 超预期的银行** | Test whether the beat was **earned** (PAT growth ≈ pre-provision profit growth, buffer intact) or **manufactured** / 检验该超预期是**挣来的**（净利润增速≈拨备前利润增速，缓冲完好）还是**做出来的** |
| 5 | **A post-merger bank / 并购后的银行** | Decompose margin compression asset-side vs liability-side; **never** assume recovery to the acquirer's pre-merger NIM; track CASA / 将息差压缩分解为资产端与负债端；**绝不**假设能恢复到收购方并购前的净息差；跟踪CASA |
| 6 | **Any company post-merger/demerger/disposal / 任何经历合并·分立·处置的公司** | Treat the issuer's own "not comparable" statement as **binding**; state the truncated window explicitly / 将发行人自己的「不可比」声明视为**有约束力**；明确说明被截断的窗口 |
| 7 | **Any Indian filing / 任何印度财报** | Do the **crore ↔ billion conversion once, explicitly, at the top of the working file** (RF-4 fired twice in one session on this) / 在工作文件顶部**一次性、明确地**完成 **crore ↔ billion** 换算（本次会话此项RF-4触发两次） |
| 8 | **Any run whose purpose is validating a prior amendment / 任何以验证既有修订为目的的分析** | **Pre-register the hypothesis before fetching data** (adopted as standard practice this session) / **在获取数据前预先登记假设**（本次会话确立为标准做法） |

---

## Part 6 — Verification Status / 验证状态

| Check / 检查项 | Result / 结果 |
|---|---|
| Original content preserved (line-diff vs pre-session) / 原有内容保留（与会话前逐行比对） | ✅ **Pure insertions; 0 lines deleted** / **纯插入；0行被删除** |
| Code fences balanced in all files / 所有文件代码围栏配对 | ✅ Pass |
| `command-center` id contiguity 1–49 / id连续性 | ✅ No gaps, no duplicates / 无缺口、无重复 |
| MD ↔ HTML parsed-dict equality / MD与HTML解析后一致性 | ✅ **IDENTICAL** / **完全一致** |
| Stale "A–D proposed" line removed / 过期「拟议A–D」表述已移除 | ✅ Confirmed / 已确认 |
| Amendments live in Project Knowledge (commit c) / 提交(c)已在项目知识库生效 | ✅ Verified by search / 经检索验证 |
| Amendments live in Project Knowledge (commit d) / 提交(d)已在项目知识库生效 | ⏳ **Pending re-upload** / **待重新上传** |

### ⚠ Re-upload queue — four files / 待重新上传 —— 四个文件

```
command-center.md
command-center.html
intrinsic-value.md
industry-playbooks.md
```

**EN —** `earnings-quality-and-distortions.md` was uploaded in the previous round and is **unchanged** by the IBN commit — no action needed.
**中文 —** `earnings-quality-and-distortions.md` 已在上一轮上传，且IBN提交**未对其做修改** —— 无需操作。

---

## Part 7 — Open Items / 待办事项

| # | Item / 事项 | Priority / 优先级 |
|---|---|---|
| 1 | **▲ IBN BVPS ₹527 is single-sourced (Screener)** and is the denominator of every P/B in the IBN report — verify to the Q1 FY27 filing before committing capital / **IBN的每股账面价值₹527为单一来源**，且是该报告中所有市净率的分母 —— 投入资金前须核对至FY27一季度财报 | **High / 高** |
| 2 | **▲ HDB ~₹9,000cr floating buffer is inferred**, not confirmed on the Q1 FY27 balance sheet. The entire B-1 positive reading is conditional on it — **if the buffer was drawn down, the finding inverts and the verdict goes to AVOID** / **HDB约₹9,000cr浮动缓冲为推断值**，未在FY27一季度资产负债表上确认。整个B-1正向解读以此为条件 —— **若缓冲已被动用，结论反转，判定应为「回避」** | **High / 高** |
| 3 | `industry-playbooks.md` — create §F.3/§F.4 headers **or** correct the dangling references / 创建§F.3、§F.4标题**或**修正悬空引用 | Medium / 中 |
| 4 | `intrinsic-value.md` — relabel the unsuffixed `2026-07-26` change-log entry as `(a)` / 将无后缀的 `2026-07-26` 变更日志条目重标为 `(a)` | Low / 低 |
| 5 | **361 Degrees (1361.HK) verdict flag ▲** still unreconciled — v1 BUY/7 vs v2 HOLD/ACCUMULATE 6/10. Oldest unresolved item in the book / **361度（1361.HK）结论标记▲** 仍未统一 —— v1「买入/7」对v2「持有/逐步增持 6/10」。本书中最久未决事项 | Medium / 中 |

---

*Compiled 26 July 2026. Two commits, five files, six amendments (#9, #9-R, #10, #11→#11-R, #11-R(b), #12). Research documentation, not investment advice.*

*编制于2026年7月26日。两次提交，五个文件，六项修订（#9、#9-R、#10、#11→#11-R、#11-R(b)、#12）。本文为研究记录，不构成投资建议。*
