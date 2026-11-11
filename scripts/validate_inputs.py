#!/usr/bin/env python3
"""Data gate for the value-investing skill: validate inputs_<ticker>_<date>.json.

Every number that reaches a valuation is declared in one inputs file (spec:
references/data-inputs.md) and checked here. The analysis is always produced; what this
decides is how frankly it must be labelled:

  VERIFIED     everything read and reconciled             -> normal report
  QUALIFIED    gaps only (not read / not explained)       -> report with a data-status box, verdict
                                                             PROVISIONAL, conviction <= 6, margin of safety +10
  UNRESOLVED   a number disagrees with its cross-check    -> report shows value under each reading, NO verdict

Usage:
  python3 validate_inputs.py inputs.json                  # final (the second read is expected)
  python3 validate_inputs.py inputs.json --stage first    # while building, before the second read
  python3 validate_inputs.py inputs.json --status-box     # the data-status box for the report
  python3 validate_inputs.py inputs.json --trail          # the report's Data Trail table

Checks: D1 provenance · D2 units/currency · D3 share count · D4 price · D5 net cash ·
D6 statement articulation · D7 owner-earnings tie · D8 history · D9 matched windows ·
D10 FX · D11 stake containment.

Result per check: PASS · NOTE (passed with a written reconciling note) · FLAG (allowed, must be
shown) · SKIP (not applicable) · GAP (something not read, not recorded or not explained) ·
CONFLICT (two figures disagree, or a figure breaks a rule).
Tolerance ladder for ratio checks: <=2% pass, 2-5% needs a note in "notes", otherwise CONFLICT.
Exit code 1 only when UNRESOLVED.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenario_dcf import build_net_debt  # noqa: E402  (Check 21 R1/R2, reused)

PASS_TOL, NOTE_TOL = 0.02, 0.05
CUM_PASS_TOL, CUM_NOTE_TOL = 0.10, 0.20   # D6c only: a five-year cash identity has more legitimate leaks
UNIT = {"units": 1, "thousands": 1e3, "millions": 1e6, "billions": 1e9}
SOURCE_TIERS = ("filing", "issuer_release", "structured", "aggregator", "wire")
BASES = ("filed", "structured", "filing_summary", "aggregator", "computed", "estimated")
SCOPE_MIN_YEARS = {"deep_dive": 5, "quick": 3, "refresh": 1, "earnings": 1}
LATEST_FACTS = ("revenue", "op_profit", "ni", "da", "capex", "ocf")
AFFECTS = {"D1": "sourcing of verdict-moving numbers", "D2": "units and currency", "D3": "share count",
           "D4": "price", "D5": "net cash", "D6": "statements behind owner earnings", "D7": "owner earnings",
           "D8": "history (growth, normalisation, discount-rate count)", "D9": "trend statements",
           "D10": "currency conversion", "D11": "stake value"}
# What a report must do for each outcome (references/data-inputs.md §1).
CONSEQUENCES = {
    "VERIFIED": {"verdict": "normal", "conviction_cap": None, "margin_of_safety_add_pts": 0},
    "QUALIFIED": {"verdict": "PROVISIONAL tag on the verdict", "conviction_cap": 6, "margin_of_safety_add_pts": 10,
                  "report": "data-status box at the top of every deliverable; gaps become the next refresh's fetch list"},
    "UNRESOLVED": {"verdict": "NO VERDICT until the conflict is resolved", "conviction_cap": None,
                   "margin_of_safety_add_pts": None,
                   "report": "data-status box; value shown under each reading of the conflicting number, no single fair value"},
}


class Report:
    def __init__(self, notes):
        self.rows, self.notes = [], notes or {}

    def add(self, cid, status, detail):
        self.rows.append({"id": cid, "status": status, "affects": AFFECTS.get(cid.split(".")[0], ""), "detail": detail})

    def split(self, cid, gaps, conflicts, ok):
        """One row per kind: what is missing (GAP) and what disagrees (CONFLICT); PASS if neither."""
        if conflicts:
            self.add(cid, "CONFLICT", "; ".join(conflicts))
        if gaps:
            self.add(cid, "GAP", "; ".join(gaps))
        if not gaps and not conflicts:
            self.add(cid, "PASS", ok)

    def ladder(self, cid, label, ours, ref, pass_tol=PASS_TOL, note_tol=NOTE_TOL):
        """Compare two figures on the tolerance ladder; a 2-5% gap passes only with notes[cid]."""
        if ref in (None, 0) or ours is None:
            self.add(cid, "GAP", f"{label}: a figure is missing or zero (ours={ours}, reference={ref})")
            return
        gap = abs(ours - ref) / abs(ref)
        text = f"{label}: {ours:,.6g} vs {ref:,.6g} (gap {gap:.2%})"
        if gap <= pass_tol:
            self.add(cid, "PASS", text)
        elif gap <= note_tol and self.notes.get(cid):
            self.add(cid, "NOTE", f"{text} — {self.notes[cid]}")
        elif gap <= note_tol:
            self.add(cid, "CONFLICT", f"{text} — between {pass_tol:.0%} and {note_tol:.0%}: write the "
                                  f"reconciling item in notes['{cid}'] or re-source")
        else:
            self.add(cid, "CONFLICT", f"{text} — above {note_tol:.0%}; one of the two figures is wrong")

    def status(self):
        st = {r["status"] for r in self.rows}
        return "UNRESOLVED" if "CONFLICT" in st else "QUALIFIED" if "GAP" in st else "VERIFIED"


def num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def parse_date(s):
    try:
        return dt.date.fromisoformat(str(s))
    except ValueError:
        return None


def resolve(data, path):
    """'treasury.debt[0]' or 'statements.years[FY2025].ni' -> value (KeyError if absent)."""
    cur = data
    for part in re.findall(r"[^.\[\]]+|\[[^\]]+\]", path):
        if part.startswith("["):
            key = part[1:-1]
            if not isinstance(cur, list):
                raise KeyError(path)
            if key.isdigit() and int(key) < len(cur) and not isinstance(cur[int(key)], dict):
                cur = cur[int(key)]
                continue
            hit = [e for e in cur if isinstance(e, dict) and key in (str(e.get("fy")), str(e.get("name")), str(e.get("period")))]
            if hit:
                cur = hit[0]
            elif key.isdigit() and int(key) < len(cur):
                cur = cur[int(key)]
            else:
                raise KeyError(path)
        else:
            if not isinstance(cur, dict) or part not in cur:
                raise KeyError(path)
            cur = cur[part]
    return cur


def numbers_in(text):
    """Every number printed in a quoted line, separators removed; (123) reads as 123."""
    out = []
    for tok in re.findall(r"\d[\d,，]*(?:\.\d+)?", str(text)):     # no spaces: columns stay separate
        tok = re.sub(r"[,，]", "", tok)
        try:
            out.append(float(tok))
        except ValueError:
            pass
    return out


def same_number(a, b):
    """Equal allowing for rounding in the last printed digit."""
    return abs(abs(a) - abs(b)) <= max(5e-4 * abs(b), 1e-9)


def fx_rate(data, frm, to):
    """Rate to convert 1 unit of `frm` into `to`, from the dated fx table."""
    if frm == to:
        return 1.0
    for f in data.get("fx", []):
        if num(f.get("rate")) and f["rate"] > 0:
            if (f.get("from"), f.get("to")) == (frm, to):
                return f["rate"]
            if (f.get("from"), f.get("to")) == (to, frm):
                return 1 / f["rate"]
    return None


def sorted_years(data):
    return sorted(data.get("statements", {}).get("years", []), key=lambda y: str(y.get("period_end", y.get("fy"))))


# ---------------------------------------------------------------- D1 provenance

def verdict_movers(data):
    classes = data.get("shares", {}).get("classes") or []
    paths = [f"shares.classes[{c.get('name')}].count" for c in classes] or ["shares.period_end_count"]
    paths += ["shares.ni_attributable", "shares.eps_basic",
              "shares.equity_attributable", "treasury.cash", "treasury.short_term_investments",
              "treasury.term_deposits"]
    debt = data.get("treasury", {}).get("debt")
    paths += [f"treasury.debt[{i}]" for i in range(len(debt))] if isinstance(debt, list) else ["treasury.debt"]
    if data.get("shares", {}).get("senior_instrument", {}).get("classification") == "equity":
        paths.append("shares.senior_instrument.distribution")
    years = sorted_years(data)
    if years:
        paths += [f"statements.years[{years[-1].get('fy')}].{k}" for k in LATEST_FACTS]
    for s in data.get("stakes", []):
        paths += [f"stakes[{s.get('name')}].shares_held", f"stakes[{s.get('name')}].carrying_value"]
    oe = data.get("owner_earnings") or {}
    sc = oe.get("structural_cause")
    if oe.get("method") == "latest_margin" and isinstance(sc, dict):
        if isinstance(sc.get("window_start"), dict):
            paths.append("owner_earnings.structural_cause.window_start.value")
        for p_ in sc.get("periods") or []:
            if isinstance(p_, dict) and p_.get("period"):
                base = f"owner_earnings.structural_cause.periods[{p_['period']}]"
                paths += [f"{base}.value", f"{base}.prior_value"]
    return paths


def check_provenance(data, rep, stage):
    sources = {s.get("id"): s for s in data.get("sources", [])}
    for s in sources.values():
        if s.get("tier") not in SOURCE_TIERS:
            rep.add("D1.sources", "GAP", f"source '{s.get('id')}' tier '{s.get('tier')}' is not one of {SOURCE_TIERS}")
    scope = data.get("meta", {}).get("scope", "deep_dive")
    if scope == "deep_dive" and not any(s.get("tier") == "filing" and s.get("annual") for s in sources.values()):
        rep.add("D1.annual", "GAP", "a deep dive needs at least one annual report in sources "
                                     "(tier 'filing', annual: true); otherwise relabel the scope")
    prov = data.get("provenance", {})
    bad, unread = 0, []
    for path in verdict_movers(data):
        try:
            value = resolve(data, path)
        except KeyError:
            rep.add("D1", "GAP", f"{path}: value missing from the inputs file")
            bad += 1
            continue
        p = prov.get(path)
        problems, clash = [], []
        if not p:
            problems.append("no provenance entry")
        else:
            src = sources.get(p.get("source"))
            if p.get("basis") not in ("filed", "structured"):
                problems.append(f"basis '{p.get('basis')}' — a verdict-moving number must be 'filed' or 'structured'")
            if not src:
                problems.append(f"source '{p.get('source')}' not in sources")
            elif p.get("basis") == "filed" and src.get("tier") not in ("filing", "issuer_release"):
                problems.append(f"basis 'filed' but source tier is '{src.get('tier')}'")
            elif p.get("basis") == "structured" and src.get("tier") != "structured":
                problems.append(f"basis 'structured' but source tier is '{src.get('tier')}'")
            if not str(p.get("page", "")).strip():
                problems.append("no page / table reference")
            quote = str(p.get("quote", "")).strip()
            if not quote:
                problems.append("no quoted line")
            elif num(value) and value != 0:
                scale, printed = p.get("quote_scale", 1), numbers_in(quote)
                parts = p.get("quoted_values")
                if parts:      # a figure built from several printed lines (e.g. depreciation + amortisation)
                    absent = [x for x in parts if not any(same_number(q, x) for q in printed)]
                    if absent:
                        clash.append(f"quoted_values {absent} do not appear in the quote")
                    elif not same_number(sum(parts) * scale, value):
                        clash.append(f"quoted_values sum to {sum(parts) * scale:,} (quote_scale {scale}), not {value:,}")
                elif not any(same_number(q * scale, value) for q in printed):
                    clash.append(f"quote does not contain the value {value:,} "
                                    f"(quote_scale {scale}): transcription or scale error")
            if stage == "final":
                v = (p.get("verified") or {}).get("value_read")
                if not num(v):
                    unread.append(path)
                elif num(value) and not same_number(v, value):
                    clash.append(f"second pass read {v:,} but the file holds {value:,}")
        if clash:
            bad += 1
            rep.add("D1", "CONFLICT", f"{path}: " + "; ".join(clash))
        if problems:
            bad += 1
            rep.add("D1", "GAP", f"{path}: " + "; ".join(problems))
    if unread:
        bad += 1
        rep.add("D1", "GAP", f"second read not done for {len(unread)} verdict-moving number(s) "
                             f"(verified.value_read): {', '.join(unread)}")
    if not bad:
        rep.add("D1", "PASS", f"{len(verdict_movers(data))} verdict-moving numbers carry source, page, "
                              f"matching quote" + (" and second-pass read" if stage == "final" else ""))


# ---------------------------------------------------------------- D2 units / currency

def check_units(data, rep):
    meta, sh, px = data.get("meta", {}), data.get("shares", {}), data.get("price", {})
    probs, clash = [], []
    if meta.get("unit") not in UNIT:
        probs.append(f"meta.unit '{meta.get('unit')}' must be one of {sorted(UNIT)}")
    if not meta.get("currency"):
        probs.append("meta.currency (reporting currency) missing")
    if not meta.get("fiscal_year_end"):
        probs.append("meta.fiscal_year_end missing")
    if sh.get("per_share_currency", meta.get("currency")) != meta.get("currency"):
        clash.append("shares.per_share_currency differs from the reporting currency: restate EPS/BVPS/DPS "
                     "in the reporting currency")
    if px.get("currency") and px["currency"] != meta.get("currency") and fx_rate(data, px["currency"], meta.get("currency")) is None:
        probs.append(f"price is in {px['currency']} but statements are in {meta.get('currency')} and no fx "
                     f"entry converts between them")
    ratio = meta.get("ads_ratio")
    if meta.get("is_depositary") and not num(ratio):
        probs.append("depositary listing but meta.ads_ratio (ordinary shares per ADS) is missing")
    if num(ratio):
        for field, holder in (("count_basis", sh), ("eps_basis", sh), ("basis", px)):
            if holder.get(field) not in ("ordinary", "ads"):
                probs.append(f"ads_ratio set: {'price' if holder is px else 'shares'}.{field} must be 'ordinary' or 'ads'")
    rep.split("D2", probs, clash,
              f"unit {meta.get('unit')}, reporting currency {meta.get('currency')}, price currency {px.get('currency')}")


def to_ordinary(value, basis, ratio, per_share):
    """Put a count or a per-share figure on the ordinary-share basis."""
    if not num(ratio) or basis != "ads":
        return value
    return value / ratio if per_share else value * ratio


# ---------------------------------------------------------------- D3 share count

def check_shares(data, rep):
    meta, sh, px = data.get("meta", {}), data.get("shares", {}), data.get("price", {})
    need = ("period_end_count", "period_end_date", "valuation_count", "ni_attributable", "eps_basic", "eps_dp")
    missing = [k for k in need if sh.get(k) is None]
    if missing:
        rep.add("D3", "GAP", f"shares block missing {missing}")
        return None
    ratio = meta.get("ads_ratio")
    count = to_ordinary(sh["period_end_count"], sh.get("count_basis"), ratio, False)

    classes = sh.get("classes") or []
    if not classes:
        rep.add("D3.classes", "GAP", "shares.classes is empty: list every share class with its count and source")
    else:
        total = sum(c.get("count", 0) for c in classes)
        gap = abs(total - sh["period_end_count"]) / sh["period_end_count"]
        rep.add("D3.classes", "PASS" if gap <= 0.005 else "CONFLICT",
                f"sum of {len(classes)} class(es) {total:,.6g} vs period-end count {sh['period_end_count']:,.6g} (gap {gap:.2%})")

    expect = sh["period_end_count"] + sh.get("dilutive", 0)
    ok = abs(expect - sh["valuation_count"]) <= 0.001 * expect
    rep.add("D3.valuation_count", "PASS" if ok else "CONFLICT",
            f"valuation count {sh['valuation_count']:,.6g} vs period-end {sh['period_end_count']:,.6g} + "
            f"dilution {sh.get('dilutive', 0):,.6g}" + ("" if ok else " — use the latest period-end count plus "
                                                        "dilution, never a weighted average"))

    # Anchor 2: EPS back-check, senior-instrument gate first.
    senior = sh.get("senior_instrument") or {}
    cls = senior.get("classification")
    if cls not in ("none", "equity", "liability"):
        rep.add("D3.senior", "GAP", "shares.senior_instrument.classification must be 'none', 'equity' or "
                                     "'liability' — read the capital stack before the EPS back-check")
        return count
    dist = senior.get("distribution", 0) if cls == "equity" else 0
    if cls == "equity" and not dist:
        rep.add("D3.senior", "GAP", "equity-classified senior instrument but no distribution recorded")
        return count
    eps = to_ordinary(sh["eps_basic"], sh.get("eps_basis"), ratio, True)
    implied = (sh["ni_attributable"] - dist) / eps
    resolution = 0.5 * 10 ** (-sh["eps_dp"]) / abs(sh["eps_basic"])
    wavg = sh.get("weighted_avg_basic")
    ref = to_ordinary(wavg, sh.get("count_basis"), ratio, False) if num(wavg) else count
    gap = abs(implied - ref) / ref
    text = (f"(NI {sh['ni_attributable']:,.6g} − senior {dist:,.6g}) ÷ EPS {sh['eps_basic']} = {implied:,.6g} vs "
            f"{'weighted average' if num(wavg) else 'period-end'} {ref:,.6g} (gap {gap:.2%}); "
            f"passes at ±{resolution:.3%} resolution; senior gate = {cls}")
    if gap <= max(PASS_TOL, resolution) and num(wavg):
        rep.add("D3.eps", "PASS", text)
    elif gap <= max(PASS_TOL, resolution) and (gap <= 0.005 or rep.notes.get("D3.eps")):
        rep.add("D3.eps", "NOTE" if gap > 0.005 else "PASS", text + (f" — {rep.notes.get('D3.eps')}" if gap > 0.005 else ""))
    elif gap <= max(PASS_TOL, resolution):
        rep.add("D3.eps", "GAP", text + " — no weighted-average count given: add shares.weighted_avg_basic or "
                                         "explain the gap in notes['D3.eps']")
    else:
        rep.add("D3.eps", "CONFLICT", text + " — the share count, the profit line or a senior distribution is wrong")
    if cls == "equity" and resolution > 0.005 and not sh.get("senior_confirmed_in_equity_statement"):
        rep.add("D3.senior", "GAP", f"EPS resolution ±{resolution:.2%} is too coarse to rest on arithmetic: confirm "
                                     "the distribution in the statement of changes in equity and set "
                                     "shares.senior_confirmed_in_equity_statement")
    if num(wavg):
        wgap = abs(ref - count) / count
        if wgap > PASS_TOL and not rep.notes.get("D3.weighted"):
            rep.add("D3.weighted", "GAP", f"weighted average {ref:,.6g} vs period-end {count:,.6g} (gap {wgap:.2%}): "
                                           "name the buyback, placement or split in notes['D3.weighted']")
        else:
            rep.add("D3.weighted", "NOTE" if wgap > PASS_TOL else "PASS",
                    f"weighted average vs period-end gap {wgap:.2%}" +
                    (f" — {rep.notes['D3.weighted']}" if wgap > PASS_TOL else ""))

    # Anchor 3
    if num(sh.get("bvps")) and num(sh.get("equity_attributable")):
        bv = to_ordinary(sh["bvps"], sh.get("eps_basis"), ratio, True)
        rep.ladder("D3.bvps", "BVPS × shares vs equity attributable", bv * count, sh["equity_attributable"])
    elif sh.get("bvps") is None and num(sh.get("equity_attributable")):
        rep.add("D3.bvps", "SKIP", "issuer does not report book value per share (required where a method rests on P/B — Check 14)")
    else:
        rep.add("D3.bvps", "GAP", "shares.equity_attributable is required, and shares.bvps where the issuer reports it")
    if num(sh.get("dps")) and num(sh.get("dividends_declared")) and sh["dividends_declared"]:
        dps = to_ordinary(sh["dps"], sh.get("eps_basis"), ratio, True)
        rep.ladder("D3.dps", "DPS × shares vs dividends declared", dps * ref, sh["dividends_declared"])
    else:
        rep.add("D3.dps", "SKIP", "no dividend declared for the period")

    # Anchor 1: market cap, in the price currency, on the ordinary-share basis.
    if num(px.get("value")):
        price = to_ordinary(px["value"], px.get("basis"), ratio, True)
        ours = count * price
        caps = sh.get("published_market_caps") or []
        if not caps:
            rep.add("D3.mcap", "GAP", "shares.published_market_caps is empty: record at least one published figure")
        for i, c in enumerate(caps):
            rate = fx_rate(data, c.get("currency", px.get("currency")), px.get("currency"))
            if rate is None or not num(c.get("value")):
                rep.add("D3.mcap", "GAP", f"published market cap from {c.get('source')} cannot be converted to {px.get('currency')}")
                continue
            ref_cap = c["value"] * rate
            cid = "D3.mcap" if i == 0 else f"D3.mcap{i + 1}"
            before = len(rep.rows)
            rep.ladder(cid, f"shares × price vs published market cap ({c.get('source')})", ours, ref_cap)
            if rep.rows[before]["status"] == "CONFLICT":
                implied_px = ref_cap / count
                near = [o.get("label") for o in sh.get("other_listing_prices", [])
                        if num(o.get("value")) and abs(implied_px - o["value"]) / o["value"] <= 0.03]
                rep.rows[before]["detail"] += (f"; implied price {implied_px:,.6g}" +
                                               (f" matches {near} — the published figure is struck on another listing"
                                                if near else ""))
    return count


# ---------------------------------------------------------------- D4 price

def check_price(data, rep):
    meta, px = data.get("meta", {}), data.get("price", {})
    if not num(px.get("value")) or px["value"] <= 0 or not parse_date(px.get("date")):
        rep.add("D4", "GAP", "price.value and price.date are required")
        return
    value, pdate = px["value"], parse_date(px["date"])
    adate = parse_date(meta.get("analysis_date"))
    srcs = px.get("sources") or []
    if not str(px.get("p1_timestamp", "")).strip():
        rep.add("D4.P1", "GAP", "price.p1_timestamp is empty: record where on the page the quote's own date was read")
    else:
        late = [s.get("name") for s in srcs if parse_date(s.get("date")) != pdate]
        rep.add("D4.P1", "CONFLICT" if late else "PASS",
                f"quote date differs from price.date for {late}: reject those sources" if late
                else f"timestamp read: {px['p1_timestamp']}")
    if adate is None:
        rep.add("D4.P2", "GAP", "meta.analysis_date missing")
    else:
        age = (adate - pdate).days
        if 0 <= age <= 4:
            rep.add("D4.P2", "PASS", f"quote is {age} calendar day(s) old")
        elif px.get("vintage_label"):
            rep.add("D4.P2", "FLAG", f"quote is {age} days old — labelled: {px['vintage_label']}")
        else:
            rep.add("D4.P2", "GAP", f"quote is {age} days old and carries no vintage_label")
    on_file = [o for o in px.get("on_file", []) if num(o.get("value")) and parse_date(o.get("date"))
               and 0 <= (pdate - parse_date(o["date"])).days <= 365]
    stale = []
    for s in srcs:
        for o in on_file:
            if num(s.get("week52_low")) and s["week52_low"] > o["value"] * 1.001:
                stale.append(f"{s.get('name')}: 52-week low {s['week52_low']} is above {o['value']} on file ({o.get('label')})")
            if num(s.get("week52_high")) and s["week52_high"] < o["value"] * 0.999:
                stale.append(f"{s.get('name')}: 52-week high {s['week52_high']} is below {o['value']} on file ({o.get('label')})")
    rep.add("D4.P3", "CONFLICT" if stale else "PASS",
            "stale page — reject the source: " + "; ".join(stale) if stale
            else f"52-week ranges contain all {len(on_file)} price(s) on file")
    agree = [s for s in srcs if num(s.get("value")) and abs(s["value"] - value) / value <= 0.02]
    if on_file:
        last = max(on_file, key=lambda o: o["date"])
        move = value / last["value"] - 1
        if abs(move) <= 0.10:
            rep.add("D4.P4", "PASS", f"move vs last price on file ({last['value']}, {last['date']}): {move:+.1%}")
        elif len(agree) >= 2 or str(px.get("move_event", "")).strip():
            rep.add("D4.P4", "NOTE", f"move {move:+.1%} vs {last['value']} — " +
                    (px.get("move_event") or f"{len(agree)} sources agree"))
        else:
            rep.add("D4.P4", "GAP", f"move {move:+.1%} vs last price on file ({last['value']}) needs a second "
                                     "source within ±2% or a dated price.move_event")
    else:
        rep.add("D4.P4", "SKIP", "no price on file for this name")
    if len(agree) >= 2:
        rep.add("D4.P5", "PASS", f"{len(agree)} sources within ±2% of {value}")
    elif len(agree) == 1:
        rep.add("D4.P5", "FLAG", f"single source ({agree[0].get('name')}) — print ▲ beside the price")
    else:
        rep.add("D4.P5", "CONFLICT", "no recorded source is within ±2% of price.value")


# ---------------------------------------------------------------- D5 net cash

def check_treasury(data, rep):
    t = data.get("treasury")
    if not t:
        rep.add("D5", "GAP", "treasury block missing: net cash is built from every line, never typed")
        return None
    try:
        net_debt, info = build_net_debt(t)
    except SystemExit as e:
        msg = str(e).replace("STOP: ", "")
        rep.add("D5", "GAP" if msg.startswith("treasury.") else "CONFLICT", msg)
        return None
    rep.add("D5", "PASS", f"gross cash-like {info['gross_cash_like']:,.6g} − debt {info['total_debt']:,.6g} "
                          f"+ subsequent events {info['subsequent_events']:,.6g} = net cash {info['net_cash']:,.6g}"
            + (f"; {info['issuer_liquidity_gap_pct']}% from the issuer's own figure" if "issuer_liquidity_gap_pct" in info
               else "; issuer publishes no liquidity figure"))
    sdate = data.get("shares", {}).get("period_end_date")
    if t.get("as_of") != sdate:
        ok = bool(rep.notes.get("D5.dates"))
        rep.add("D5.dates", "NOTE" if ok else "GAP",
                f"treasury as of {t.get('as_of')} but share count as of {sdate}" +
                (f" — {rep.notes['D5.dates']}" if ok else ": use one balance-sheet date or explain in notes['D5.dates']"))
    else:
        rep.add("D5.dates", "PASS", f"cash, debt and share count all as of {sdate}")
    return net_debt


# ---------------------------------------------------------------- D6 articulation, D8 history

def check_history(data, rep):
    scope = data.get("meta", {}).get("scope", "deep_dive")
    years = sorted_years(data)
    need = SCOPE_MIN_YEARS.get(scope, 5)
    if len(years) < need and not rep.notes.get("D8.years"):
        rep.add("D8.years", "GAP", f"{len(years)} fiscal year(s) on file; scope '{scope}' needs {need} "
                                    "(or state why fewer exist in notes['D8.years'])")
    else:
        rep.add("D8.years", "PASS" if len(years) >= need else "NOTE", f"{len(years)} fiscal year(s) on file")
    probs, usable = [], []
    latest = years[-min(3, len(years)):]
    for y in years:
        b = y.get("basis")
        if b not in BASES:
            probs.append(f"{y.get('fy')}: basis '{b}' unknown")
        elif y in latest and b != "filed":
            probs.append(f"{y.get('fy')}: one of the latest three years but basis is '{b}' — read it from the filing")
        elif b in ("aggregator", "estimated", "computed") and not y.get("context_only"):
            probs.append(f"{y.get('fy')}: basis '{b}' may not feed growth, normalisation or the profit-decline count — "
                         "tie it to the filing's multi-year summary or mark context_only")
        elif not y.get("context_only"):
            usable.append(y.get("fy"))
    rep.add("D8.basis", "GAP" if probs else "PASS", "; ".join(probs) or f"usable history: {usable}")
    breaks = []
    for prev, cur in zip(years, years[1:]):
        for key, lo, hi in (("revenue", -0.30, 0.50), ("shares_end", -0.20, 0.20)):
            if num(prev.get(key)) and num(cur.get(key)) and prev[key]:
                ch = cur[key] / prev[key] - 1
                if not lo <= ch <= hi and not cur.get("break_note"):
                    breaks.append(f"{cur.get('fy')} {key} {ch:+.0%} with no break_note (split, acquisition, restatement?)")
    rep.add("D8.breaks", "GAP" if breaks else "PASS", "; ".join(breaks) or "no unexplained discontinuity")
    return usable


def check_articulation(data, rep):
    years = sorted_years(data)
    if not years:
        rep.add("D6", "GAP", "statements.years is empty")
        return
    cash_f = ("cash_begin", "ocf", "icf", "cff", "cash_end")
    eq_f = ("equity_begin", "ni", "equity_end")
    latest = years[-min(3, len(years)):]
    for y in years:
        fy = y.get("fy")
        if all(num(y.get(k)) for k in cash_f):
            calc = y["cash_begin"] + y["ocf"] + y["icf"] + y["cff"] + y.get("fx_effect", 0)
            base = max(abs(y["cash_end"]), abs(y["ocf"]), 1e-9)
            rep.ladder(f"D6.cash.{fy}", f"{fy} cash roll-forward", base + (calc - y["cash_end"]), base)
        elif y in latest:
            rep.add(f"D6.cash.{fy}", "GAP", f"{fy}: cash-flow totals missing {[k for k in cash_f if not num(y.get(k))]}")
        if all(num(y.get(k)) for k in eq_f):
            other = y.get("oci_and_other", 0)
            calc = (y["equity_begin"] + y["ni"] - y.get("dividends", 0) - y.get("buybacks", 0)
                    + y.get("issuance", 0) + other)
            rep.ladder(f"D6.equity.{fy}", f"{fy} equity roll-forward", calc, y["equity_end"])
            if abs(other) > 0.10 * abs(y["ni"]) and not y.get("equity_note"):
                rep.add(f"D6.equity_other.{fy}", "GAP", f"{fy}: 'oci_and_other' is {other:,.6g}, over 10% of profit — "
                                                         "itemise it in equity_note (OCI, share-based pay, senior distributions, NCI)")
        elif y in latest:
            rep.add(f"D6.equity.{fy}", "GAP", f"{fy}: equity roll-forward lines missing {[k for k in eq_f if not num(y.get(k))]}")
    # Cumulative identity: free cash flow must have gone somewhere.
    window = [(p, c) for p, c in zip(years, years[1:]) if num(p.get("net_cash_end"))][-5:]
    rows = [c for _, c in window]
    if len(rows) >= 2 and all(num(r.get(k)) for r in rows for k in ("ocf", "capex", "net_cash_end")):
        fcf = sum(r["ocf"] - r["capex"] for r in rows)
        uses = sum(r.get("dividends", 0) + r.get("buybacks", 0) - r.get("issuance", 0) + r.get("acquisitions", 0)
                   + r.get("other_cash_uses", 0) for r in rows)
        d_net = rows[-1]["net_cash_end"] - window[0][0]["net_cash_end"]
        base = max(abs(fcf), 1e-9)
        rep.ladder("D6.cumulative", f"{len(rows)}-year free cash flow {fcf:,.6g} vs distributions, acquisitions and "
                                    f"change in net cash {uses + d_net:,.6g}", base + (fcf - uses - d_net), base,
                   CUM_PASS_TOL, CUM_NOTE_TOL)
    elif data.get("meta", {}).get("scope", "deep_dive") == "deep_dive":
        rep.add("D6.cumulative", "GAP", "cumulative cash identity cannot run: each year needs ocf, capex and "
                                         "net_cash_end (plus the year before the window)")
    else:
        rep.add("D6.cumulative", "SKIP", "reduced scope: fewer than two years with net cash on file")


# ---------------------------------------------------------------- D7 owner earnings

def oe_year(c):
    """Operating owner earnings for one year (intrinsic-value.md Method 1 Step 1): pre-interest, after tax,
    stock compensation left as an expense."""
    return ((c["op_profit"] - c.get("non_operating", 0)) * (1 - c["tax_rate"]) + c["da"]
            - c["maintenance_capex"] + c.get("wc_adjustment", 0))


def check_owner_earnings(data, rep, usable):
    oe = data.get("owner_earnings")
    if not oe or not num(oe.get("value")):
        rep.add("D7", "GAP", "owner_earnings block with a 'value' is required")
        return None, None
    by_fy = {y.get("fy"): y for y in sorted_years(data)}
    comps, probs, clash, totals, fcfs = oe.get("components") or {}, [], [], [], []
    if not comps:
        probs.append("owner_earnings.components is empty")
    for fy, c in comps.items():
        y = by_fy.get(fy)
        if y is None:
            probs.append(f"{fy}: not in statements.years")
            continue
        if fy not in usable:
            probs.append(f"{fy}: year is not usable history (D8)")
        for k in ("op_profit", "da"):
            if not num(c.get(k)) or not num(y.get(k)) or not same_number(c[k], y[k]):
                clash.append(f"{fy}: component {k} {c.get(k)} does not equal the statement line {y.get(k)}")
        if c.get("other_non_cash") or "ni" in c:
            clash.append(f"{fy}: owner earnings start from operating profit, not net income, and stock compensation "
                         "or other non-cash charges are not added back (use 'adjustments' for a true one-off)")
        t = c.get("tax_rate")
        if not num(t) or not 0 <= t <= 0.5:
            probs.append(f"{fy}: tax_rate missing or outside 0-50%")
        elif num(y.get("tax")) and num(y.get("pretax")) and y["pretax"] > 0 \
                and abs(t - y["tax"] / y["pretax"]) > 0.05 and not rep.notes.get("D7.tax"):
            probs.append(f"{fy}: tax_rate {t:.1%} is more than 5 points from the reported {y['tax'] / y['pretax']:.1%} — "
                         "explain the normal rate in notes['D7.tax']")
        if c.get("non_operating") and not oe.get("non_operating_note"):
            probs.append(f"{fy}: non_operating {c['non_operating']} taken out of operating profit needs non_operating_note "
                         "(interest, investment gains, fair-value changes, associates)")
        mc = c.get("maintenance_capex")
        if not num(mc) or mc < 0:
            probs.append(f"{fy}: maintenance_capex missing")
        elif num(y.get("capex")) and mc > y["capex"] * 1.001:
            clash.append(f"{fy}: maintenance_capex {mc} exceeds total capex {y['capex']}")
        if all(num(c.get(k)) for k in ("op_profit", "tax_rate", "da", "maintenance_capex")):
            totals.append(oe_year(c))
        if num(y.get("ocf")) and num(y.get("capex")):
            fcfs.append(y["ocf"] - y["capex"])
    for key, what in (("maintenance_capex_basis", "how maintenance capex was estimated"),
                      ("tax_rate_basis", "where the normal tax rate comes from")):
        if not str(oe.get(key, "")).strip():
            probs.append(f"{key} missing: state {what}")
    for a in oe.get("adjustments", []):
        if not num(a.get("amount")) or not a.get("reason"):
            probs.append(f"adjustment '{a.get('label')}' needs an amount and a reason")
    if probs:
        rep.add("D7", "GAP", "; ".join(probs))
    if not totals:
        if clash:
            rep.add("D7", "CONFLICT", "; ".join(clash))
        return oe["value"], None
    method, alt = oe.get("method", "average"), None
    if method == "latest_margin":
        base_val, alt, how = check_structural_cause(data, rep, comps, by_fy)
        if base_val is None:
            return oe["value"], None
    elif method == "margin":      # normalise the margin, not the scale: latest revenue x average owner-earnings margin
        pairs = [(oe_year(c), by_fy[fy].get("revenue")) for fy, c in comps.items()
                 if fy in by_fy and all(num(c.get(k)) for k in ("op_profit", "tax_rate", "da", "maintenance_capex"))]
        latest_rev = sorted_years(data)[-1].get("revenue")
        if not num(latest_rev) or not all(num(r_) and r_ > 0 for _, r_ in pairs):
            rep.add("D7", "GAP", "method 'margin' needs revenue for every component year and for the latest year")
            return oe["value"], None
        base_val = latest_rev * sum(v_ / r_ for v_, r_ in pairs) / len(pairs)
        how = f"latest revenue {latest_rev:,.6g} × {len(pairs)}-year average owner-earnings margin"
    elif method == "average":
        base_val, how = sum(totals) / len(totals), f"{len(totals)}-year average of components"
    else:
        rep.add("D7", "GAP", f"owner_earnings.method '{method}' must be 'average', 'margin' or 'latest_margin'")
        return oe["value"], None
    adj_total = sum(a["amount"] for a in oe.get("adjustments", []) if num(a.get("amount")))
    computed = base_val + adj_total
    if alt is not None:
        alt = {"basis": "three-year average margin", "value": round(alt + adj_total, 4),
               "note": "printed through to fair value beside the latest-margin basis (intrinsic-value.md Step 1, rule 6)"}
    gap = abs(computed - oe["value"]) / max(abs(computed), 1e-9)
    text = (f"operating owner earnings handed to the valuation {oe['value']:,.6g} vs computed ({how}) "
            f"{computed:,.6g} (gap {gap:.2%})")
    if gap > 0.01 or clash:
        rep.add("D7", "CONFLICT", "; ".join(clash + ([text] if gap > 0.01 else [])))
    elif not probs:
        rep.add("D7", "PASS", text)
    if fcfs:
        fcf = sum(fcfs) / len(fcfs)
        if fcf <= 0 or oe["value"] > 1.25 * fcf:
            ok = bool(rep.notes.get("D7.vs_fcf"))
            rep.add("D7.vs_fcf", "NOTE" if ok else "GAP",
                    f"owner earnings {oe['value']:,.6g} vs average free cash flow {fcf:,.6g} over the same years" +
                    (f" — {rep.notes['D7.vs_fcf']}" if ok else ": more than 25% above cash actually produced — "
                     "explain in notes['D7.vs_fcf'] (growth capex, working-capital build, interest paid) or lower it"))
        else:
            rep.add("D7.vs_fcf", "PASS", f"owner earnings {oe['value']:,.6g} vs average free cash flow {fcf:,.6g}")
    return oe["value"], alt


STRUCTURAL_SHARE = 0.5   # the cause, after tax, must explain at least half of the gap between the two bases


def margin_basis(comps, by_fy, latest_rev):
    """Latest revenue x average owner-earnings margin over the component years (None if revenue missing)."""
    pairs = [(oe_year(c), by_fy[fy].get("revenue")) for fy, c in comps.items() if fy in by_fy]
    if not num(latest_rev) or not pairs or not all(num(r_) and r_ > 0 for _, r_ in pairs):
        return None
    return latest_rev * sum(v_ / r_ for v_, r_ in pairs) / len(pairs)


def check_structural_cause(data, rep, comps, by_fy):
    """method 'latest_margin' (intrinsic-value.md Method 1 Step 1, rule 6 exception). The latest full year's
    actual margin replaces the three-year average only when a filed, quantified cause explains the shift and
    shows in the last two reported periods. Any failure is a CONFLICT: the figure is not a permitted basis.
    Returns (latest-year owner earnings, three-year-margin owner earnings, description) or (None, None, None)."""
    oe, years = data["owner_earnings"], sorted_years(data)
    sc, bad = oe.get("structural_cause"), []
    latest = years[-1] if years else {}
    lfy = latest.get("fy")
    fail = lambda: (rep.add("D7.structural", "CONFLICT", "method 'latest_margin': " + "; ".join(bad)), (None, None, None))[1]
    if lfy not in comps:
        bad.append(f"the latest full year {lfy} must be an owner-earnings component (its margin is the one used)")
    cyc = data.get("meta", {}).get("cyclical")
    if cyc is True:
        bad.append("meta.cyclical is true: a cyclical's margin rise is the cycle until shown otherwise — use the "
                   "mid-cycle base (intrinsic-value.md Method 1 Step 1), not the latest year's margin")
    elif cyc is not False:
        bad.append("meta.cyclical must be stated as true or false before the latest year's margin can be used "
                   "(autos, semiconductors, batteries, materials, shipping, airlines are cyclical)")
    if len(comps) < 3:
        bad.append(f"needs at least three component years so the three-year-margin basis can print beside it "
                   f"(has {len(comps)})")
    if not isinstance(sc, dict):
        bad.append("structural_cause is required: the line, kind, reason, amount, window_start and the last two "
                   "reported periods, each figure quoted from a filing")
        return fail()
    if not str(sc.get("line", "")).strip():
        bad.append("structural_cause.line missing: name the income-statement line that moved")
    if sc.get("kind") not in ("cost", "income"):
        bad.append("structural_cause.kind must be 'cost' or 'income'")
    if not str(sc.get("reason", "")).strip():
        bad.append("structural_cause.reason missing: say why the shift is structural, not cyclical")
    amount = sc.get("amount")
    if not num(amount) or amount == 0:
        bad.append("structural_cause.amount missing: the cause must be a figure from the filings, not a narrative")
    if bad:
        return fail()
    sign = -1 if sc["kind"] == "cost" else 1               # a cost that falls raises the margin
    first_fy = sorted(comps, key=lambda fy: str(by_fy.get(fy, {}).get("period_end", fy)))[0]
    ws = sc.get("window_start") or {}
    if ws.get("period") != first_fy or not num(ws.get("value")):
        bad.append(f"window_start must give the line's value for {first_fy}, the first component year")
    periods = [p_ for p_ in sc.get("periods") or [] if isinstance(p_, dict)]
    by_label = {p_.get("period"): p_ for p_ in periods}
    ytd = (data.get("statements") or {}).get("ytd") or {}
    second = ytd.get("label") if ytd.get("label") else (years[-2].get("fy") if len(years) > 1 else None)
    need = [x for x in (lfy, second) if x]
    if len(by_label) < 2:
        bad.append(f"the cause must show in at least the last two reported periods; {len(by_label)} given")
    missing = [x for x in need if x not in by_label]
    if missing:
        bad.append(f"periods must include the last two reported periods {need}; missing {missing}")
    for p_ in periods:
        if not (num(p_.get("value")) and num(p_.get("prior_value"))):
            bad.append(f"period {p_.get('period')}: value and prior_value (same window a year earlier) are required")
    if bad:
        return fail()
    latest_line = by_label[lfy]["value"]
    if not same_number(latest_line - ws["value"], amount) or (latest_line - ws["value"]) * amount < 0:
        bad.append(f"amount {amount:,.6g} is not the filed change in the line, {lfy} {latest_line:,.6g} less "
                   f"{first_fy} {ws['value']:,.6g} = {latest_line - ws['value']:,.6g}")
    latest_oe = oe_year(comps[lfy])
    three_year = margin_basis(comps, by_fy, latest.get("revenue"))
    if three_year is None:
        bad.append("revenue missing for a component year or the latest year: the three-year-margin basis cannot print")
        return fail()
    shift = latest_oe - three_year
    effect = sign * amount * (1 - comps[lfy]["tax_rate"])  # after-tax effect on owner earnings
    moves = [sign * (p_["value"] - p_["prior_value"]) for p_ in periods]
    direction = 1 if (shift if abs(shift) > 0.01 * abs(three_year) else effect) > 0 else -1
    against = [p_["period"] for p_, m in zip(periods, moves) if m * direction <= 0]
    if against:
        bad.append(f"the line did not move the margin the same way in {against}: the shift is not persistent")
    if abs(shift) > 0.01 * abs(three_year):
        if effect * shift <= 0:
            bad.append(f"the cause moves owner earnings by {effect:+,.6g} after tax but the latest margin is "
                       f"{'above' if shift > 0 else 'below'} the three-year average")
        elif abs(effect) < STRUCTURAL_SHARE * abs(shift):
            bad.append(f"the cause explains {abs(effect):,.6g} after tax of a {abs(shift):,.6g} gap between the two "
                       f"bases ({abs(effect) / abs(shift):.0%}); at least {STRUCTURAL_SHARE:.0%} must be explained")
    if bad:
        return fail()
    rep.add("D7.structural", "PASS",
            f"{sc['line']} {ws['value']:,.6g} ({first_fy}) -> {latest_line:,.6g} ({lfy}), {amount:+,.6g}; after tax "
            f"{effect:+,.6g} of a {shift:+,.6g} gap between the bases; same direction in "
            f"{', '.join(p_['period'] for p_ in periods)} — {sc['reason']}")
    return latest_oe, three_year, (f"latest full year {lfy} actual margin (structural cause: {sc['line']}); "
                                   f"three-year-margin basis {three_year:,.6g} printed beside it")


def measured_roic(data, usable):
    """Average and incremental return on invested capital over the usable years, where each year carries
    'invested_capital'. Feeds the RONIC choice in the valuation (intrinsic-value.md Method 1 Step 2b)."""
    comps = (data.get("owner_earnings") or {}).get("components") or {}
    rates = [c["tax_rate"] for c in comps.values() if num(c.get("tax_rate"))]
    if not rates:
        return None
    t = sum(rates) / len(rates)
    def pair(key):
        rows = [y for y in sorted_years(data) if y.get("fy") in usable and num(y.get(key)) and y[key] > 0
                and num(y.get("op_profit"))]
        if len(rows) < 2:
            return None, None, None
        nopat = [y["op_profit"] * (1 - t) for y in rows]
        d_ic = rows[-1][key] - rows[0][key]
        return (round(sum(n / y[key] for n, y in zip(nopat, rows)) / len(rows), 4),
                round((nopat[-1] - nopat[0]) / d_ic, 4) if d_ic > 0 else None, f"{rows[0]['fy']}-{rows[-1]['fy']}")
    avg, inc, window = pair("invested_capital")
    o_avg, o_inc, o_window = pair("invested_capital_organic")
    if avg is None and o_avg is None:
        return None
    return {"window": window or o_window, "tax_rate_used": round(t, 4), "average": avg, "incremental": inc,
            "organic_average": o_avg, "organic_incremental": o_inc,
            "note": "organic = invested capital excluding goodwill and acquired intangibles; use it for growth "
                    "that does not rely on acquisitions"}


# ---------------------------------------------------------------- D9 windows

def check_windows(data, rep):
    st = data.get("statements", {})
    ytd, prior, years = st.get("ytd"), st.get("ytd_prior"), sorted_years(data)
    if not ytd:
        rep.add("D9", "SKIP", "no year-to-date period on file; trends rest on full fiscal years")
        return None
    if not prior or prior.get("months") != ytd.get("months"):
        rep.add("D9", "GAP", f"year-to-date '{ytd.get('label')}' has no matching prior-year window of "
                              f"{ytd.get('months')} months: a stub may not sit beside a full year")
        return None
    fy = years[-1] if years else {}
    ttm, probs = {}, []
    for k in ("revenue", "op_profit", "ni", "ocf", "capex"):
        if all(num(d.get(k)) for d in (fy, prior, ytd)):
            ttm[k] = fy[k] - prior[k] + ytd[k]
    for k, v in (st.get("ttm") or {}).items():
        if k in ttm and num(v) and abs(v - ttm[k]) > 0.01 * max(abs(ttm[k]), 1e-9):
            probs.append(f"stated TTM {k} {v:,.6g} but FY − prior YTD + YTD = {ttm[k]:,.6g}")
    ratios = {name: round(d["ocf"] / d["ni"], 2) for name, d in
              (("FY", fy), (prior.get("label", "prior YTD"), prior), (ytd.get("label", "YTD"), ytd), ("TTM", ttm))
              if num(d.get("ocf")) and num(d.get("ni")) and d["ni"]}
    rep.add("D9", "CONFLICT" if probs else "PASS", "; ".join(probs) or f"matched windows — OCF/NI {ratios}")
    return {"ttm": ttm, "ocf_to_ni": ratios}


# ---------------------------------------------------------------- D10 FX, D11 stakes

def check_fx(data, rep):
    meta, px = data.get("meta", {}), data.get("price", {})
    adate, probs = parse_date(meta.get("analysis_date")), []
    for f in data.get("fx", []):
        pair = f"{f.get('from')}/{f.get('to')}"
        if not num(f.get("rate")) or f["rate"] <= 0:
            probs.append(f"{pair}: rate missing")
        if f.get("basis") != "fixing":
            probs.append(f"{pair}: basis '{f.get('basis')}' — only a dated official fixing is allowed, never an assumed rate")
        if not parse_date(f.get("date")) or not str(f.get("source", "")).strip():
            probs.append(f"{pair}: date and fixing source are required")
        elif adate and (adate - parse_date(f["date"])).days > 7 and not rep.notes.get("D10.age"):
            probs.append(f"{pair}: fixing dated {f['date']} is more than 7 days before the analysis date "
                         "(explain in notes['D10.age'] or refresh)")
    needed = {(c, meta.get("currency")) for c in [px.get("currency")] + [s.get("quote_currency") for s in data.get("stakes", [])]
              if c and c != meta.get("currency")}
    for frm, to in needed:
        if fx_rate(data, frm, to) is None:
            probs.append(f"no fx entry for {frm}/{to}")
    if not data.get("fx") and not needed:
        rep.add("D10", "SKIP", "single-currency analysis")
    else:
        rep.add("D10", "GAP" if probs else "PASS", "; ".join(probs) or f"{len(data.get('fx', []))} dated fixing(s)")


def check_stakes(data, rep):
    meta = data.get("meta", {})
    stakes = data.get("stakes", [])
    if not stakes:
        rep.add("D11", "SKIP", "no listed stake carries value")
        return
    div = UNIT.get(meta.get("unit"), 1)
    for s in stakes:
        cid = f"D11.{s.get('name')}"
        if not all(num(s.get(k)) for k in ("shares_held", "quote", "carrying_value")) or not parse_date(s.get("quote_date")):
            rep.add(cid, "GAP", "stake needs shares_held (absolute count), quote, quote_date and carrying_value")
            continue
        if not str(s.get("holder_filing", "")).strip():
            rep.add(cid, "GAP", "holder_filing missing: the share count must be read from the investee's own ownership filing")
            continue
        rate = fx_rate(data, s.get("quote_currency"), meta.get("currency"))
        if rate is None:
            rep.add(cid, "GAP", f"no fx entry to convert {s.get('quote_currency')} to {meta.get('currency')}")
            continue
        value = s["shares_held"] * s["quote"] * rate / div
        text = f"{s['shares_held']:,} shares × {s['quote']} × {rate:.4g} = {value:,.6g} vs carrying value {s['carrying_value']:,.6g}"
        if s.get("accounting") == "equity_method":
            rep.add(cid, "PASS", text + " (equity-method line: containment not applicable)")
        elif value <= s["carrying_value"] * (1 + PASS_TOL):
            rep.add(cid, "PASS", text)
        elif rep.notes.get(cid):
            rep.add(cid, "NOTE", f"{text} — {rep.notes[cid]}")
        else:
            rep.add(cid, "CONFLICT", text + " — a component cannot exceed the balance-sheet line that holds it: the share "
                                        f"count is wrong, or the dates differ (explain in notes['{cid}'])")


# ---------------------------------------------------------------- driver

def validate(data, stage="final"):
    rep = Report(data.get("notes"))
    check_provenance(data, rep, stage)
    check_units(data, rep)
    count = check_shares(data, rep)
    check_price(data, rep)
    net_debt = check_treasury(data, rep)
    usable = check_history(data, rep)
    check_articulation(data, rep)
    oe, oe_alt = check_owner_earnings(data, rep, usable)
    windows = check_windows(data, rep)
    check_fx(data, rep)
    check_stakes(data, rep)
    meta, px, sh = data.get("meta", {}), data.get("price", {}), data.get("shares", {})
    status = rep.status()
    if status == "VERIFIED" and stage != "final":
        status = "PENDING_SECOND_PASS"
    rate = fx_rate(data, px.get("currency"), meta.get("currency")) if px.get("currency") else None
    return {
        "ticker": meta.get("ticker"), "stage": stage, "status": status,
        "summary": {s: sum(r["status"] == s for r in rep.rows) for s in ("PASS", "NOTE", "FLAG", "SKIP", "GAP", "CONFLICT")},
        "consequences": CONSEQUENCES.get(status, {}),
        "conflicts": [f"{r['id']} ({r['affects']}): {r['detail']}" for r in rep.rows if r["status"] == "CONFLICT"],
        "gaps": [f"{r['id']} ({r['affects']}): {r['detail']}" for r in rep.rows if r["status"] == "GAP"],
        "derived": {
            "owner_earnings": oe, "owner_earnings_alternative": oe_alt, "valuation_count": sh.get("valuation_count"), "net_debt": net_debt,
            "price": px.get("value"), "price_currency": px.get("currency"),
            "price_in_reporting_currency": None if rate is None or not num(px.get("value")) else px["value"] * rate,
            "reporting_currency": meta.get("currency"), "unit": meta.get("unit"),
            "ordinary_share_count": count, "usable_history": usable, "windows": windows,
            "roic": measured_roic(data, usable or []),
            "cyclical": meta.get("cyclical") if isinstance(meta.get("cyclical"), bool) else None,
        },
        "checks": rep.rows,
    }


def trail(data):
    """The report's Data Trail table, generated from the inputs file (never typed)."""
    src = {s.get("id"): s for s in data.get("sources", [])}
    lines = ["| Metric | Value | Source | Page | Quoted line | Basis | Second pass |", "|---|---|---|---|---|---|---|"]
    for path, p in data.get("provenance", {}).items():
        try:
            value = resolve(data, path)
        except KeyError:
            value = "MISSING"
        s = src.get(p.get("source"), {})
        v = (p.get("verified") or {}).get("value_read")
        lines.append(f"| {path} | {value:,} | {s.get('doc', p.get('source'))} ({s.get('period', '')}) | {p.get('page', '')} | "
                     f"{str(p.get('quote', '')).replace('|', '/')} | {p.get('basis', '')} | "
                     f"{'✓ ' + format(v, ',') if num(v) else '—'} |" if num(value) else
                     f"| {path} | {value} | {s.get('doc', p.get('source'))} | {p.get('page', '')} | | {p.get('basis', '')} | — |")
    px = data.get("price", {})
    for s in px.get("sources", []):
        lines.append(f"| price ({s.get('name')}) | {s.get('value')} | {s.get('name')} | — | quote dated {s.get('date')} | quote | — |")
    for f in data.get("fx", []):
        lines.append(f"| FX {f.get('from')}/{f.get('to')} | {f.get('rate')} | {f.get('source')} | — | fixing dated {f.get('date')} | {f.get('basis')} | — |")
    return "\n".join(lines)


def status_box(result):
    """The data-status box that opens every deliverable (report-template.md)."""
    st, c = result["status"], result.get("consequences", {})
    n = result["summary"]
    out = [f"> **Data status: {st}** — {n['PASS'] + n['NOTE'] + n['FLAG']} checks passed"
           f" ({n['NOTE']} with a note, {n['FLAG']} flagged), {n['GAP']} gap(s), {n['CONFLICT']} conflict(s)."]
    if st == "QUALIFIED":
        out.append(f"> Verdict is **PROVISIONAL**; conviction capped at {c['conviction_cap']}/10; required margin of "
                   f"safety +{c['margin_of_safety_add_pts']} points. The conclusions below rest on the gaps listed.")
    elif st == "UNRESOLVED":
        out.append("> **No verdict.** A number that drives value disagrees with its cross-check. Value is shown under "
                   "each reading; no single fair value is given until the conflict is resolved.")
    elif st == "PENDING_SECOND_PASS":
        out.append("> Second read of the sources not yet done.")
    for title, key in (("Conflicts — must be resolved", "conflicts"), ("Gaps — not read or not explained", "gaps")):
        if result.get(key):
            out.append(f">\n> **{title}:**")
            out += [f"> - {x}" for x in result[key]]
    for r in result["checks"]:
        if r["status"] in ("NOTE", "FLAG"):
            out.append(f"> - {r['status']} {r['id']}: {r['detail']}")
    return "\n".join(out)


def file_hash(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description="Validate a value-investing inputs file.")
    ap.add_argument("inputs")
    ap.add_argument("--stage", choices=("first", "final"), default="final")
    ap.add_argument("--out", help="write the validation result here (default: validation_<inputs name>)")
    ap.add_argument("--trail", action="store_true", help="print the Data Trail table and exit")
    ap.add_argument("--status-box", action="store_true", help="print the data-status box for the report and exit")
    args = ap.parse_args()
    with open(args.inputs, encoding="utf-8") as fh:
        data = json.load(fh)
    if args.trail:
        print(trail(data))
        return
    result = validate(data, args.stage)
    if args.status_box:
        print(status_box(result))
        return
    result["inputs_file"] = os.path.basename(args.inputs)
    result["inputs_sha256"] = file_hash(args.inputs)
    base = os.path.basename(args.inputs)
    out = args.out or os.path.join(os.path.dirname(os.path.abspath(args.inputs)),
                                   "validation_" + (base[len("inputs_"):] if base.startswith("inputs_") else base))
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, ensure_ascii=False)
    for r in result["checks"]:
        if r["status"] != "PASS":
            print(f"{r['status']:8} {r['id']}: {r['detail']}")
    print(f"{result['status']} — {result['summary']} — written to {out}")
    # The analysis is produced in every case; the exit code only tells a script whether a verdict is allowed.
    sys.exit(1 if result["status"] == "UNRESOLVED" else 0)


if __name__ == "__main__":
    main()
