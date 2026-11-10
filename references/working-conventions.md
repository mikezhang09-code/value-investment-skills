# Working Conventions — Stage 0, Stage 6 and Session Rules

> Operating rules that `SKILL.md` relies on but does not spell out. They make the skill runnable
> from this repository alone. Analytical rules live in `SKILL.md`, `process-lessons.md` and
> `data-sources.md`; this file holds only procedure.
>
> **In a Claude Project** the project instructions may restate these and add project-specific items
> (for example a pilot step or a flat-folder path mapping). Where the two differ on procedure, follow
> the project instructions and report the difference so one of them can be corrected.

---

## 1. Stage 0 — what to read on every run

List the skill directory (an actual listing, never from memory), then read these before any other
work:

| File | Why |
|---|---|
| `SKILL.md` | workflow, scope routing, gates |
| `assets/report-template.md` | the three deliverables and the Step 10.5 manifest |
| `references/process-lessons.md` (+ any `process-lessons-ADDENDUM_*`) | error classes and checks; addendum items marked PROPOSED are not binding |
| `references/data-sources.md` | source tiers, the live-price gate P1–P5, the RF list |
| `command-center.md` | the coverage universe; needed to position the name and for Stage 6 |

Load the other reference files when the step that needs them is reached (Reference Files table in
`SKILL.md`). For any bank, insurer or financial holding company, load
`references/industry-playbooks.md` at scoping, not at Step 5.

Confirm with a one-line load report. If `command-center.md` is absent, say so and proceed. Never
reconstruct its prior contents from memory.

## 2. Scope and source tier

- Confirm ticker and exchange; ask which listing if the name is dual-listed.
- Classify the request with the scope routing table in `SKILL.md`. Default to a full deep dive when
  the scope is not stated. Note any specific angle the user asked for.
- Run exactly the steps in that scope's row, without asking for confirmation between stages.
- Declare the source tier before starting. A full deep dive needs at least one annual report in the
  source trail. Wire-flash data may not move any verdict field: mark the entry PENDING-PRIMARY.
- Never skipped at any scope: the live-price gate (P1–P5), Step 2.5, Step 6.5 and Step 10.5.

## 3. Fetch budgets

Ceilings on filing and data fetches, not targets:

| Scope | Budget |
|---|---|
| Full deep dive | about 12 (annual reports, 8 quarters, two call transcripts, peers, price) |
| Quick thesis | about 6 |
| Thesis refresh / earnings reaction | about 5 (new filing, issuer release, transcript, price and its second source) |
| Stage 6 and deliverable building | no new fetches except the live-price check |

If the budget runs out, finish with what is in hand and list what was not obtained under "Data
gaps". Label a self-imposed budget limit as a budget limit, not as a data-availability gap. An empty
debt, share-count or tax field never reaches the valuation.

## 4. Thesis refresh

Find the original thesis first: the command-center row and the prior report. Structure the refresh
as:

1. What changed
2. Does the verdict hold
3. Updated fair value
4. Updated entry zone and position guidance
5. What to watch next

Honour pre-committed tripwires as written. Do not move them on the day they are tested. If a fair
value is corrected the same day (supersede in place), re-levelled tripwires must say so and give the
reason.

## 5. Deliverables and presentation order

Per the Step 10.5 manifest in `SKILL.md`:

- HTML dashboard `report_<ticker>_<YYYY-MM-DD>.html`: full deep dive only (optional for comparison).
- Markdown report `report_<ticker>_<YYYY-MM-DD>.md`: every scope.
- Bilingual EN/简体中文 summary `summary_<ticker>_<YYYY-MM-DD>_EN-CN.md`: every scope, derived from
  the finished report.
- Stage 6 command-center update: every scope that creates or changes a verdict.

Present in this order: HTML dashboard, Markdown report, bilingual summary, then
`command-center.html`. Formal deliverables carry bilingual EN/ZH headings.

**Verdict vocabulary.** Exactly one of BUY / ACCUMULATE / WATCHLIST / HOLD / PASS / AVOID, with
conviction out of 10. The same word goes in the report, dashboard, summary and the command-center
JSON row. No hybrid labels. SELL is an action on a held position, recorded in the note.

## 6. Stage 6 — command-center update (mandatory final step)

`command-center.md` is the source of truth; `command-center.html` is generated from its JSON block.
Both are revised in place: same filenames, one copy.

1. **Parity first.** Parse the fenced `json` block in `command-center.md` and the `const DATA` array
   in `command-center.html`. Assert they are equal and that IDs are contiguous 1→N. Do this before
   assigning any new ID.
2. **Row.** Add or replace the company's row in BOTH the master table and the JSON block: verdict,
   conviction, base fair value, current price and its date, entry zone, position cap, next catalyst,
   short note, and the rate fields (`dr`, `drBasis`, `impRet`). Flag approximate figures with ▲.
   Edit by a unique anchor string and assert the anchor occurs exactly once. Never edit by line
   number.
3. **HTML.** Regenerate `command-center.html` by replacing its embedded DATA array with the same
   serialised JSON. Keep the page's existing structure; do not rebuild it from the report template.
4. **Change log.** Add one dated line. When a same-day correction supersedes an entry, say so in the
   new line.
5. **Assertions.** Header universe size == JSON record count == master-table row count, and every
   table row has the header's cell count. Check that the HTML's DATA array still parses as
   JavaScript.
6. **Save and hand over.** Write both files back to the canonical location (Project Knowledge, or
   this repository) and present `command-center.html`. Ask the user to confirm the stored
   `command-center.md` is the new version. A missed save is the most common cause of ID drift.

Derive every figure in the row from the report's canonical figure block (Key Principle 14). Skipping
Stage 6 leaves the name out of the universe; that has happened before and went unnoticed for months.

## 7. Final chat summary

Verdict, conviction, fair value, current price and its date, margin of safety, entry zone, position
cap, top two risks, next review trigger, and the Step 10.5 manifest result (each artifact: done, not
applicable, or failed).

---

## Change log

- **2026-11-10** — Created, so the skill can run from the repository without the Claude Project's
  instructions. Content taken from the Stock Deep Analysis project instructions as of this date.
  Not included: the project's pilot Step 4.5 (management evidence ledger) and its flat-folder path
  mapping, which are project-specific.
