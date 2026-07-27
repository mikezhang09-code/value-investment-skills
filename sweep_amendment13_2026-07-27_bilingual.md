# Amendment #13 Sweep — Senior-Instrument Distortion Across the Coverage Universe
# 修订条款 #13 专项排查 —— 优先级资本工具对覆盖范围内每股指标的扭曲

**Date 日期:** 2026-07-27
**Scope 范围:** All financials in the 50-name coverage universe · 覆盖范围内全部金融股（共 50 只标的）
**Trigger 触发来源:** Amendment #13, derived from China Taiping (0966.HK) · 由中国太平（0966.HK）个案推导出的修订条款 #13

---

## 1. Question Asked
## 第一节 · 排查所要回答的问题

Amendment #13 requires that Anchor 2 subtract distributions to perpetual, AT1 and preference
holders **before** back-calculating the share count, because those instruments sit inside equity
but rank **ahead of** ordinary shares. On China Taiping the omission overstated the share count by
**3.83%** and the issuer-published embedded value per share by **7.6%**.

The sweep asks the retrospective version of that question: **has this error already corrupted an
entry in the book?**

修订条款 #13 规定：在用"归母净利润 ÷ 基本每股收益"反算股数（锚点二）之前，**必须先扣除**支付给永续资本
证券、其他一级资本工具（AT1）及优先股持有人的分派。原因在于，这类工具在**形式上计入权益，但在实质上
优先于普通股**。在中国太平个案中，遗漏该步骤使股数被高估 **3.83%**，并使公司公布的每股内含价值被高估
**7.6%**。

本次排查所问的，是这一问题的**回溯版本：该错误是否已经污染了覆盖范围内的既有记录？**

---

## 2. Population
## 第二节 · 排查样本

| # | Name 名称 | Ticker 代码 | Sector 行业 | Per-share metric at risk 存在风险的每股指标 |
|---|---|---|---|---|
| 2 | HDFC Bank · 印度住房开发金融银行 | HDB | Banking 银行 | BVPS / justified P/B · 每股净资产与合理市净率 |
| 8 | Berkshire Hathaway · 伯克希尔·哈撒韦 | BRK.B | Insurance/Holding 保险控股 | — (no per-share book anchor 无每股账面锚点) |
| 13 | ICICI Bank · 印度工业信贷投资银行 | IBN | Banking 银行 | **BVPS ₹527 ▲ — denominator of every P/B 全部市净率计算的分母** |
| 33 | Futu Holdings · 富途控股 | FUTU | Online Brokerage 互联网券商 | BVPS; ADS ratio 1:8 · 每股净资产；存托股比例 1:8 |
| 41 | Waterdrop · 水滴公司 | WDH | Insurtech 保险科技 | BVPS, EPS, DPS — all per ADS 均为每存托股口径 |
| 48 | PICC P&C · 中国财险 | 2328.HK | Insurance / P&C 财产保险 | BVPS RMB13.34 ▲, EPS · 每股净资产与每股收益 |
| 49 | PICC Group · 中国人保 | 1339.HK | Insurance / Holding 保险控股 | NAV/SOTP, EPS · 分部加总净资产与每股收益 |
| ~~50~~ | ~~China Taiping · 中国太平~~ | ~~0966.HK~~ | — | Source case, excluded 源头个案，不纳入排查 |

**7 names swept · 实际排查 7 只标的。**

---

## 3. Method
## 第三节 · 排查方法

Two tests, run in order. The second is only required where the first is not decisive.

采用两道检验，依次执行；仅当第一道检验无法定案时，才需要执行第二道。

**Test A — Classification gate (new).** Does the instrument sit in **equity** or in
**liabilities**? Only equity-classified instruments create the trap. A liability-classified
perpetual has its coupon recognised in interest expense, already deducted before net profit, and
Anchor 2 is therefore clean by construction.

**检验 A —— 分类闸口（新增）。** 该工具究竟计入**权益**还是**负债**？只有计入权益的工具才会产生此项
陷阱。若永续工具被分类为负债，其票息计入利息支出，在净利润之前即已扣除，锚点二在构造上就是干净的。

**Test B — Anchor 2 arithmetic.** Compute `(profit attributable to owners − senior distribution)
÷ basic EPS` and compare with the share count on file, **stating the EPS-rounding band
explicitly**.

**检验 B —— 锚点二算术验证。** 计算 `(归母净利润 − 优先级工具分派) ÷ 基本每股收益`，与档案中记录的
股数比对，并**明确列出每股收益四舍五入所对应的区间**。

---

## 4. Results
## 第四节 · 排查结果

| # | Name 名称 | Test A — Classification 分类检验 | Test B — Anchor 2 锚点二 | Verdict 结论 |
|---|---|---|---|---|
| 49 | PICC Group 中国人保 | — | Naive 44,433mn vs 44,224mn on file, **+0.47%**, inside rounding band 44,220–44,647 · 朴素算法 444.33 亿股 对 档案 442.24 亿股，偏差 **+0.47%**，落在四舍五入区间内 | **PASS** (at ≤0.48% resolution) · **通过**（分辨率 ≤0.48%） |
| 2 | HDFC Bank 住房开发金融银行 | AT1 = **borrowings**; coupon in interest expense; pool ~0.5% of capital · AT1 计入**借款**，票息列于利息支出，规模约占资本 0.5% | Not required 无需执行 | **PASS — structurally immune** · **通过 —— 结构上免疫** |
| 13 | ICICI Bank 工业信贷投资银行 | AT1 = **borrowings** (20-F prepared under Indian GAAP with US GAAP reconciliation) · AT1 计入**借款**（20-F 以印度会计准则编制并附美国会计准则调节表） | Not required 无需执行 | **PASS on #13** — but see §6 · **就 #13 而言通过** —— 但见第六节 |
| 48 | PICC P&C 中国财险 | Capital supplementary bonds = **subordinated debt**, not equity · 资本补充债券属**次级债**，非权益 | Implied EPS RMB1.8153 from file; reported EPS not obtained · 由档案倒算每股收益 1.8153 元；未取得公告口径每股收益 | **INCOMPLETE** · **未完成** |
| 8 | Berkshire 伯克希尔 | No preferred outstanding at parent level · 母公司层面无存续优先股 | n/a 不适用 | **PASS** · **通过** |
| 33 | Futu 富途 | Post-IPO; convertible preferred converted at listing · 上市后可转换优先股已于上市时全部转股 | n/a 不适用 | **PASS (low residual)** · **通过（剩余风险低）** |
| 41 | Waterdrop 水滴 | Post-IPO; same as above · 上市后情况同上 | n/a 不适用 | **PASS (low residual)** · **通过（剩余风险低）** |

> **No #13 error was found anywhere in the book. China Taiping remains the only case.**
>
> **覆盖范围内未发现任何 #13 类错误。中国太平仍是唯一个案。**

---

## 5. Two Validated Refinements to Amendment #13
## 第五节 · 对修订条款 #13 的两项经验证细化

The sweep served as amendment #13's scheduled validation. The rule survived — but two live cases
sharpened it.

本次排查即为修订条款 #13 的预定验证程序。该规则通过了验证，但两个实盘个案使其得以细化。

### 5a. Add the classification gate *before* the arithmetic
### 5a. 应在算术验证**之前**加入分类闸口

HDFC Bank and ICICI Bank **both** carry AT1 perpetual capital — #13's predicate was satisfied on
two names — **and the trap fired on neither.** Indian banks report AT1 under **borrowings** (RBI
Basel III framework, Banking Regulation Act schedule format), so the coupon is interest expense
and net profit is already net of it. PICC P&C's capital supplementary bonds are subordinated debt
on the same logic.

**The discriminator is not whether the instrument is called "perpetual." It is where it sits.**
Without this gate, #13 generates a false alarm on every Indian bank and on every mainland issuer
of capital supplementary bonds — which is most of the financials sleeve. One line of checking
prevents it.

印度住房开发金融银行与印度工业信贷投资银行**均**持有 AT1 永续资本 —— 在两只标的上 #13 的前提条件都
成立 —— **但陷阱在两者身上都未触发。** 印度银行业将 AT1 计入**借款**科目（依据印度央行巴塞尔 III 框架
及《银行业监管法》报表格式），票息因而列入利息支出，净利润本身已是扣除后的口径。中国财险的资本补充
债券属次级债，逻辑相同。

**判别标准不在于该工具是否被称为"永续"，而在于它究竟坐落在哪个科目。** 若缺少这道闸口，#13 将在每一家
印度银行、以及每一家发行资本补充债券的境内机构上产生误报 —— 而这几乎覆盖了整个金融板块。仅需一行核对
即可避免。

### 5b. State the diagnostic's resolution alongside the result
### 5b. 报告检验结果时必须同时说明其分辨率

Anchor 2's precision is bounded by the **number of decimal places in reported EPS**, and across the
book it varies by roughly two orders of magnitude.

锚点二的精度受**公告每股收益的小数位数**约束；在覆盖范围内，该精度的差异接近两个数量级。

| Name 名称 | Reported EPS 公告每股收益 | Resolution 分辨率 | Smallest detectable distortion 可检出的最小扭曲 |
|---|---|---|---|
| China Taiping 中国太平 | HK$7.251 (3dp 三位小数) | **±0.007%** | Anything 任何幅度 |
| PICC P&C 中国财险 | RMB ~1.815 (3dp 三位小数) | ±0.028% | ~0.1% |
| PICC Group 中国人保 | RMB 1.04 (2dp 两位小数) | **±0.481%** | ~1% |

PICC Group's +0.47% gap is **arithmetically indistinguishable from EPS rounding**. A senior
distribution of up to RMB217mn would produce exactly the number observed. The honest statement is
therefore **"no distortion above roughly 1%"**, not "no distortion."

This also explains why China Taiping was catchable at all: at three decimal places on a HK$7.25
base, the 3.83% gap was **about 550× the diagnostic's resolution**. On a low-EPS name the same
proportional error could hide completely.

中国人保 +0.47% 的差额，在算术上**与每股收益四舍五入的影响无法区分**。一笔不超过人民币 2.17 亿元的
优先级分派，会精确产生所观察到的这一数字。因此，诚实的表述是**"不存在超过约 1% 的扭曲"**，而非
"不存在扭曲"。

这同时解释了中国太平为何能够被检出：在 7.25 港元的基数上保留三位小数，3.83% 的偏差约为该检验分辨率的
**550 倍**。若换成每股收益基数较低的标的，同样比例的错误将被完全掩盖。

> **Rule 规则:** Report Anchor 2 as *"passes at ±X% resolution"* — never as an unqualified pass.
> Where resolution is worse than about 0.5% **and** the name carries equity-classified hybrids,
> confirm against the statement of changes in equity rather than resting on the arithmetic.
>
> 锚点二的结论应表述为**"在 ±X% 分辨率下通过"**，绝不可表述为无条件通过。当分辨率劣于约 0.5%，
> **且**该标的持有计入权益的混合资本工具时，必须回到权益变动表核对，不得仅凭算术验证结案。

---

## 6. The Sweep Found a Larger Problem Than the One It Was Looking For
## 第六节 · 排查发现了比原定目标更大的问题

**ICICI Bank (#13) — the P/B denominator is unresolved, and the gap is roughly 3× the China
Taiping effect.**

**印度工业信贷投资银行（#13）—— 市净率的分母尚未确定，其口径差异约为中国太平个案影响的 3 倍。**

The FY2026 Form 20-F discloses both bases:
FY2026 年度 20-F 文件同时披露了两套口径：

| Basis 口径 | Figure 金额 |
|---|---|
| Stockholders' equity, **US GAAP** · **美国会计准则**下股东权益 | ₹409,093 crore |
| Consolidated net worth, **Indian GAAP** · **印度会计准则**下合并净资产 | ₹363,060 crore |
| **Gap 差额** | **₹46,033 crore = +12.7%** |

The command centre carries **BVPS ₹527 ▲**, single-sourced from Screener, and already flagged as
*"the denominator of every P/B here — verify to filing before acting."* That flag was correct, and
is now quantified: **₹527 sits between the two bases.** At least three readings reproduce it or
come close:

指挥中心记录的每股净资产为 **₹527 ▲**，来源单一（Screener），且早已标注为*"此处全部市净率计算的分母
—— 行动前必须回溯至原始文件核实"*。该标注是正确的，现已被量化：**₹527 恰好落在两套口径之间。** 至少
有三种读法可以复现或接近该数值：

- Indian GAAP consolidated ÷ ~689 crore shares → ₹527 (exact, but the share count looks low)
  印度会计准则合并口径 ÷ 约 68.9 亿股 → ₹527（数值吻合，但该股数偏低）
- Indian GAAP consolidated ÷ ~713 crore shares → ₹509
  印度会计准则合并口径 ÷ 约 71.3 亿股 → ₹509
- US GAAP ÷ ~713 crore shares → ₹574
  美国会计准则口径 ÷ 约 71.3 亿股 → ₹574

**The basis is unidentified, and the plausible range spans roughly ±12%** on the single input that
drives the entire valuation. This is **not** a #13 error — no senior instrument is involved — but
it belongs to the same *class* of error: **an unverified per-share denominator**, surfaced
precisely because the sweep forced an audit of that field.

**口径未能确定，而合理取值区间约为 ±12%** —— 且这一输入项独自驱动着整个估值。这**并非** #13 类错误
（不涉及任何优先级工具），但它属于**同一类错误：未经核实的每股分母**。它之所以浮出水面，恰恰是因为本次
排查强制审计了这一字段。

**PICC P&C (#48) shows the same pattern in milder form.** BVPS RMB13.34 is marked ▲ *derived from
ROE* — that is, reverse-engineered from a ratio rather than read off the balance sheet. It has
never been tied to a filing either.

**中国财险（#48）呈现同一模式，程度较轻。** 其每股净资产 13.34 元标注为 ▲*由净资产收益率倒算得出*
—— 即从比率反推，而非直接读取自资产负债表，同样从未与原始文件建立对应关系。

---

## 7. The Generalizable Finding
## 第七节 · 可推广的结论

Three of the seven names have a weak per-share book-value denominator. **None of them is weak for
the reason #13 predicted.** The failure modes actually found were:

七只标的中有三只的每股账面价值分母存在薄弱环节。**但没有一只是因 #13 所预测的原因而薄弱。** 实际发现的
失效模式为：

1. **GAAP-basis ambiguity** (ICICI — 12.7%) · **会计准则口径歧义**（印度工业信贷投资银行 —— 12.7%）
2. **Derived-not-read figures** (PICC P&C — BVPS backed out of ROE) · **倒算而非读取的数据**（中国财险 —— 每股净资产由净资产收益率反推）
3. **Rounding-limited verification** (PICC Group — cannot resolve below 1%) · **受四舍五入限制的验证**（中国人保 —— 无法分辨 1% 以下的差异）

The book's real per-share exposure is **the provenance of the book-value denominator**, not senior
instruments. #13 is a correct rule that happened to catch a rare instance of a common problem. The
sweep's value lay less in confirming #13 than in forcing the audit that surfaced everything else.

覆盖范围内真正的每股风险敞口，是**账面价值分母的数据来源可追溯性**，而非优先级资本工具。#13 是一条正确
的规则，只是它所捕获的，恰好是一个常见问题的罕见实例。本次排查的价值，与其说在于验证了 #13，不如说在于
它强制推动的那次审计，让其余问题得以暴露。

---

## 8. Recommended Actions
## 第八节 · 建议后续行动

| Priority 优先级 | Action 行动 | Name 标的 |
|---|---|---|
| **1** | Resolve the BVPS basis against the 20-F; restate P/B and fair value on the confirmed figure · 依据 20-F 确定每股净资产口径，并以确认后的数据重述市净率与合理价值 | **ICICI 工业信贷投资银行 (#13)** |
| **2** | Read BVPS from the FY2025 balance sheet; retire the ROE-derived ▲ · 从 FY2025 资产负债表直接读取每股净资产，撤销由净资产收益率倒算的 ▲ 标记 | **PICC P&C 中国财险 (#48)** |
| 3 | Obtain reported basic EPS; complete Test B · 取得公告口径基本每股收益，完成检验 B | PICC P&C 中国财险 (#48) |
| 4 | Record the +0.47% / ±0.48% resolution note so a future session does not re-run it · 记录 +0.47% / ±0.48% 分辨率结论，避免后续重复排查 | PICC Group 中国人保 (#49) |
| 5 | Fold refinements 5a and 5b into `SKILL.md` and `data-sources.md` · 将 5a 与 5b 两项细化写入 `SKILL.md` 与 `data-sources.md` | — |

**No verdict changes.** No fair value moves on the evidence gathered here — but ICICI's could move
on action 1, and that is the one to run next.

**全部投资结论维持不变。** 本次排查所取得的证据不会改变任何合理价值 —— 但印度工业信贷投资银行的合理
价值可能因行动 1 而变动，该项应作为下一步优先执行。

---

## 9. Sources & Data Trail
## 第九节 · 数据台账

| Item 项目 | Source 来源 | Tier 等级 |
|---|---|---|
| PICC P&C FY25 net profit RMB40,377mn, ROE 14.7%, CoR 97.5%, DPS RMB0.68 · 中国财险 FY25 净利润 403.77 亿元、净资产收益率 14.7%、综合成本率 97.5%、每股股息 0.68 元 | 2025 Annual Results presentation, property.picc.com.cn · 2025 年度业绩发布材料 | 1 |
| PICC P&C capital supplementary bonds · 中国财险资本补充债券 | 2024 Annual Report, stock code 2328 · 2024 年年度报告 | 1 |
| PICC Group FY25 NI RMB46.21bn, basic EPS RMB1.04 · 中国人保 FY25 归母净利润 462.1 亿元、基本每股收益 1.04 元 | FY2025 results announcement (1339.HK) · FY2025 业绩公告 | 1 |
| ICICI FY26 US GAAP equity ₹409,093cr vs Indian GAAP net worth ₹363,060cr · 印度工业信贷投资银行 FY26 美国准则股东权益 与 印度准则合并净资产 | Form 20-F, FYE 31-Mar-2026 · 20-F 文件，会计年度截至 2026 年 3 月 31 日 | 1 |
| ICICI FY26 standalone ₹50,146.64cr / consolidated ₹54,207.70cr, DPS ₹12 · 母公司口径 与 合并口径净利润、每股股息 12 卢比 | 6-K, 2026 results release · 6-K 业绩公告 | 1 |
| HDFC Bank AT1 ~0.5% of capital · 住房开发金融银行 AT1 约占资本 0.5% | Moody's rating note (2021) — **dated ▲** · 穆迪评级报告（2021 年）—— **数据陈旧 ▲** | 2 |
| Indian AT1 classified as borrowings · 印度 AT1 计入借款科目 | Sector-level; inferred from RBI Basel III framework + 20-F basis — **not read to a specific balance sheet** ▲ · 行业层面推断，源自印度央行巴塞尔 III 框架及 20-F 编制基础 —— **未逐行核对至具体资产负债表** ▲ | 3 |

> **Open item ▲.** The AT1 classification claim for HDB and IBN is structurally sound and doubly
> protected by magnitude, but has not been confirmed line-by-line against either bank's balance
> sheet. It is the one load-bearing assumption in this sweep resting on tier-3 evidence.
>
> **待办事项 ▲。** 关于两家印度银行 AT1 分类的判断，在结构逻辑上成立，且因规模微小而具有双重保护，
> 但尚未逐行核对至任一家银行的资产负债表。这是本次排查中唯一一项建立在三级证据之上的承重假设。
