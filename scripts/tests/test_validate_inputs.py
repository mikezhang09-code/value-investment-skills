"""Tests for the data gate. Run from the repo root:  python3 -m unittest discover -s scripts/tests -v

The clean fixture is a synthetic company. The failure fixtures graft onto it the figures recorded in
references/process-lessons.md and SKILL.md for each past error; lines the repo does not record
(for example a debt balance) keep their synthetic values and are marked as such.
"""
import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(HERE)
sys.path.insert(0, SCRIPTS)
import validate_inputs as vi  # noqa: E402


def clean():
    """A five-year synthetic company whose statements articulate exactly. USD millions."""
    years, cash, equity, debt, rev = [], 500.0, 2000.0, 200.0, 1000.0
    prev_net = cash - debt
    for i, fy in enumerate(range(2021, 2026)):
        rev = round(rev * 1.08, 1)
        ni, da, capex = round(rev * 0.10, 1), round(rev * 0.03, 1), round(rev * 0.04, 1)
        ocf, div = round(ni + da, 1), round(ni * 0.4, 1)
        row = {"fy": f"FY{fy}", "period_end": f"{fy}-12-31", "basis": "filed" if i >= 2 else "filing_summary",
               "source": "AR25", "revenue": rev, "op_profit": round(rev * 0.13, 1), "ni": ni, "da": da,
               "capex": capex, "ocf": ocf, "icf": -capex, "cff": -div, "fx_effect": 0,
               "cash_begin": round(cash, 1), "equity_begin": round(equity, 1), "dividends": div,
               "buybacks": 0, "issuance": 0, "acquisitions": 0, "oci_and_other": 0, "shares_end": 1000,
               "invested_capital": round(rev * 0.5, 1)}
        cash = round(cash + ocf - capex - div, 1)
        equity = round(equity + ni - div, 1)
        row.update(cash_end=cash, equity_end=equity, net_cash_end=round(cash - debt, 1))
        years.append(row)
    last = years[-1]
    comps = {y["fy"]: {"op_profit": y["op_profit"], "tax_rate": 0.25, "da": y["da"],
                       "maintenance_capex": round(y["capex"] * 0.75, 2), "wc_adjustment": 0} for y in years[-3:]}
    oe = sum(vi.oe_year(c) for c in comps.values()) / 3
    data = {
        "meta": {"ticker": "TEST", "listing": "NYSE", "analysis_date": "2026-11-10", "fiscal_year_end": "12-31",
                 "currency": "USD", "unit": "millions", "scope": "deep_dive", "ads_ratio": None},
        "sources": [{"id": "AR25", "tier": "filing", "annual": True, "doc": "FY2025 annual report",
                     "url": "https://example.invalid/ar25.pdf", "period": "FY2025", "retrieved": "2026-11-10"}],
        "shares": {"classes": [{"name": "ordinary", "count": 1000, "source": "AR25 cover"}],
                   "period_end_count": 1000, "period_end_date": "2025-12-31", "dilutive": 10,
                   "valuation_count": 1010, "weighted_avg_basic": 1000,
                   "senior_instrument": {"classification": "none"},
                   "ni_attributable": last["ni"], "eps_basic": round(last["ni"] / 1000, 3), "eps_dp": 3,
                   "bvps": round(last["equity_end"] / 1000, 2), "equity_attributable": last["equity_end"],
                   "dps": round(last["dividends"] / 1000, 4), "dividends_declared": last["dividends"],
                   "published_market_caps": [{"source": "Exchange page", "value": 30100, "currency": "USD"}]},
        "price": {"value": 30.0, "currency": "USD", "date": "2026-11-09", "p1_timestamp": "quote line: 9 Nov close",
                  "sources": [{"name": "A", "value": 30.0, "date": "2026-11-09", "week52_low": 22, "week52_high": 35},
                              {"name": "B", "value": 30.05, "date": "2026-11-09"}],
                  "on_file": [{"label": "prior report", "value": 28.5, "date": "2026-08-01"}]},
        "treasury": {"as_of": "2025-12-31", "cash": last["cash_end"], "short_term_investments": 0,
                     "term_deposits": 0, "debt": [200.0]},
        "statements": {"years": years},
        "owner_earnings": {"components": comps, "maintenance_capex_basis": "75% of capex: store refits vs new stores, AR25 p.40",
                           "tax_rate_basis": "statutory 25%, in line with the five-year effective rate",
                           "adjustments": [], "value": round(oe, 2)},
        "fx": [], "stakes": [], "notes": {}, "provenance": {},
    }
    return with_provenance(data)


def with_provenance(data):
    data["provenance"] = {}
    for path in vi.verdict_movers(data):
        value = vi.resolve(data, path)
        data["provenance"][path] = {"basis": "filed", "source": "AR25", "page": "57",
                                    "quote": f"line item {value:,}" if value else "no balance reported",
                                    "verified": {"value_read": value}}
    return data


RANK = ["SKIP", "PASS", "FLAG", "NOTE", "GAP", "CONFLICT"]


def run(data, stage="final"):
    """Result plus the worst status recorded under each check id."""
    res = vi.validate(data, stage)
    st = {}
    for r in res["checks"]:
        if r["id"] not in st or RANK.index(r["status"]) > RANK.index(st[r["id"]]):
            st[r["id"]] = r["status"]
    return res, st


class CleanFixture(unittest.TestCase):
    def test_passes_final(self):
        res, st = run(clean())
        self.assertEqual(res["status"], "VERIFIED", [r for r in res["checks"] if r["status"] in ("GAP", "CONFLICT")])
        self.assertEqual(res["derived"]["valuation_count"], 1010)

    def test_first_stage_is_pending(self):
        d = clean()
        for p in d["provenance"].values():
            del p["verified"]
        self.assertEqual(run(d, "first")[0]["status"], "PENDING_SECOND_PASS")
        self.assertEqual(run(d, "final")[0]["status"], "QUALIFIED")     # an unread second pass is a gap, not a stop


class Outcomes(unittest.TestCase):
    def test_gaps_only_gives_a_qualified_analysis(self):
        d = clean()
        d["statements"]["years"][-1]["basis"] = "filing_summary"      # latest year not read from the filing
        res, _ = run(d)
        self.assertEqual(res["status"], "QUALIFIED")
        self.assertEqual(res["consequences"]["conviction_cap"], 6)
        self.assertEqual(res["consequences"]["margin_of_safety_add_pts"], 10)
        self.assertTrue(res["gaps"] and not res["conflicts"])
        self.assertIsNotNone(res["derived"]["owner_earnings"])        # the valuation can still run
        self.assertIn("PROVISIONAL", vi.status_box(res))

    def test_a_conflict_outranks_gaps(self):
        d = clean()
        d["statements"]["years"][-1]["basis"] = "filing_summary"
        d["shares"]["valuation_count"] = 5000
        res, _ = run(d)
        self.assertEqual(res["status"], "UNRESOLVED")
        self.assertIn("No verdict", vi.status_box(res))

    def test_missing_treasury_line_leaves_net_debt_unvalidated(self):
        d = clean()
        del d["treasury"]["term_deposits"]
        res, _ = run(d)
        self.assertEqual(res["status"], "QUALIFIED")
        self.assertIsNone(res["derived"]["net_debt"])


class Provenance(unittest.TestCase):
    def test_quote_must_contain_value(self):
        d = clean()
        d["provenance"]["shares.ni_attributable"]["quote"] = "Profit for the year 999.9"
        self.assertEqual(run(d)[1]["D1"], "CONFLICT")

    def test_scale_slip_is_caught_and_quote_scale_fixes_it(self):
        d = clean()
        p = d["provenance"]["treasury.cash"]
        p["quote"] = f"Cash and cash equivalents {d['treasury']['cash'] * 1000:,.0f}"   # filing prints thousands
        self.assertEqual(run(d)[1]["D1"], "CONFLICT")
        p["quote_scale"] = 0.001
        self.assertEqual(run(d)[1]["D1"], "PASS")

    def test_aggregator_cannot_back_a_verdict_mover(self):
        d = clean()
        d["sources"].append({"id": "AGG", "tier": "aggregator", "doc": "data site"})
        d["provenance"]["shares.classes[ordinary].count"].update(basis="aggregator", source="AGG")
        self.assertEqual(run(d)[1]["D1"], "GAP")

    def test_figure_built_from_several_printed_lines(self):
        d = clean()
        da = d["statements"]["years"][-1]["da"]
        p = d["provenance"]["statements.years[FY2025].da"]
        p.update(quote=f"Depreciation {da - 10:,} ... Amortisation 10.0", quoted_values=[da - 10, 10.0])
        self.assertEqual(run(d)[1]["D1"], "PASS")
        p["quoted_values"] = [da - 10, 11.0]          # a part that is not in the quote
        self.assertEqual(run(d)[1]["D1"], "CONFLICT")
        p.update(quote=f"Depreciation {da - 10:,} ... Amortisation 11.0")   # parts present but do not sum
        self.assertEqual(run(d)[1]["D1"], "CONFLICT")

    def test_multi_column_line_as_printed(self):
        # A real statement line carries a note reference and two years; each column is its own number.
        self.assertEqual(vi.numbers_in("Balance at close of the month 2,296,439,000 22,337,000 2,318,776,000"),
                         [2296439000.0, 22337000.0, 2318776000.0])
        d = clean()
        d["provenance"]["shares.eps_basic"]["quote"] = f"(I) Basic earnings per share  VI.54  {d['shares']['eps_basic']}  1.49"
        self.assertEqual(run(d)[1]["D1"], "PASS")

    def test_second_pass_disagreement(self):
        d = clean()
        d["provenance"]["shares.eps_basic"]["verified"]["value_read"] = 9.99
        self.assertEqual(run(d)[1]["D1"], "CONFLICT")

    def test_deep_dive_needs_an_annual_report(self):
        d = clean()
        d["sources"][0]["annual"] = False
        self.assertEqual(run(d)[1]["D1.annual"], "GAP")


class Units(unittest.TestCase):
    def test_unknown_unit(self):
        d = clean()
        d["meta"]["unit"] = "亿"
        self.assertEqual(run(d)[1]["D2"], "GAP")

    def test_depositary_listing_needs_ratio(self):
        d = clean()
        d["meta"]["is_depositary"] = True
        self.assertEqual(run(d)[1]["D2"], "GAP")

    def test_price_currency_needs_fx(self):
        d = clean()
        d["price"]["currency"] = "HKD"
        _, st = run(d)
        self.assertEqual(st["D2"], "GAP")
        self.assertEqual(st["D10"], "GAP")


class ShareCount(unittest.TestCase):
    def test_byd_h_share_float_used_as_total(self):
        # SKILL.md Anchor 2: NI RMB32.62B, EPS RMB3.58 -> 9.11B shares; 3.04B was used.
        d = clean()
        d["shares"].update(ni_attributable=32620, eps_basic=3.58, eps_dp=2, period_end_count=3040,
                           valuation_count=3040, dilutive=0, weighted_avg_basic=None)
        self.assertEqual(run(d)[1]["D3.eps"], "CONFLICT")

    def test_china_taiping_perpetual_distribution(self):
        # SKILL.md amendment #13: 27,059.28 / 7.251 = 3,731.8 vs true 3,594.2 (3.83%); distribution 997.63.
        d = clean()
        d["shares"].update(ni_attributable=27059.28, eps_basic=7.251, eps_dp=3, period_end_count=3594.2,
                           weighted_avg_basic=3594.2, valuation_count=3594.2, dilutive=0,
                           classes=[{"name": "ordinary", "count": 3594.2}])
        self.assertEqual(run(d)[1]["D3.eps"], "CONFLICT")
        d["shares"]["senior_instrument"] = {"classification": "equity", "distribution": 997.63}
        self.assertEqual(run(d)[1]["D3.eps"], "PASS")

    def test_senior_classification_must_be_stated(self):
        d = clean()
        d["shares"]["senior_instrument"] = {}
        self.assertEqual(run(d)[1]["D3.senior"], "GAP")

    def test_picc_market_cap_struck_on_other_listing(self):
        # SKILL.md Anchor 1 reverse: HK$331.40B beside HK$5.40 with 44,224mn shares -> implied HK$7.49 (A-share).
        d = clean()
        d["shares"].update(period_end_count=44224, valuation_count=44224, dilutive=0,
                           classes=[{"name": "A+H", "count": 44224}],
                           published_market_caps=[{"source": "aggregator", "value": 331400, "currency": "USD"}],
                           other_listing_prices=[{"label": "A-share converted", "value": 7.49}])
        d["price"]["value"] = 5.40
        res, st = run(d)
        self.assertEqual(st["D3.mcap"], "CONFLICT")
        self.assertIn("A-share converted", next(r["detail"] for r in res["checks"] if r["id"] == "D3.mcap"))

    def test_weighted_average_is_not_the_valuation_count(self):
        d = clean()
        d["shares"]["valuation_count"] = 1050
        self.assertEqual(run(d)[1]["D3.valuation_count"], "CONFLICT")

    def test_tolerance_ladder_needs_a_note_between_2_and_5_percent(self):
        d = clean()
        d["shares"]["bvps"] = round(d["shares"]["bvps"] * 1.03, 2)
        self.assertEqual(run(d)[1]["D3.bvps"], "CONFLICT")
        d["notes"]["D3.bvps"] = "BVPS quoted includes non-controlling interests"
        self.assertEqual(run(d)[1]["D3.bvps"], "NOTE")
        d["shares"]["bvps"] = round(d["shares"]["bvps"] * 1.05, 2)
        self.assertEqual(run(d)[1]["D3.bvps"], "CONFLICT")


class Price(unittest.TestCase):
    def test_great_wall_stale_quote(self):
        # data-sources.md RF-8: HK$8.64 page with a 52-week low of HK$8.23; HK$7.58 already on file (11 Sep).
        d = clean()
        d["meta"]["analysis_date"] = "2026-10-08"
        d["price"].update(value=8.64, date="2026-10-07",
                          sources=[{"name": "Investing.com", "value": 8.64, "date": "2026-10-07", "week52_low": 8.23}],
                          on_file=[{"label": "command center", "value": 7.58, "date": "2026-09-11"}])
        _, st = run(d)
        self.assertEqual(st["D4.P3"], "CONFLICT")
        self.assertEqual(st["D4.P4"], "GAP")     # +14% move, one source, no event

    def test_single_source_is_a_flag_not_a_pass(self):
        d = clean()
        d["price"]["sources"] = d["price"]["sources"][:1]
        self.assertEqual(run(d)[1]["D4.P5"], "FLAG")

    def test_old_quote_needs_a_vintage_label(self):
        d = clean()
        d["meta"]["analysis_date"] = "2026-11-30"
        self.assertEqual(run(d)[1]["D4.P2"], "GAP")


class Treasury(unittest.TestCase):
    def test_trip_com_omitted_deposits(self):
        # process-lessons.md Check 21: issuer headline RMB105.8B vs RMB39.8B gross used in October.
        d = clean()
        d["treasury"].update(cash=39800, issuer_liquidity=105800)     # debt line stays synthetic
        self.assertEqual(run(d)[1]["D5"], "CONFLICT")

    def test_missing_line_stops(self):
        d = clean()
        del d["treasury"]["term_deposits"]
        self.assertEqual(run(d)[1]["D5"], "GAP")

    def test_dates_must_align(self):
        d = clean()
        d["treasury"]["as_of"] = "2026-06-30"
        self.assertEqual(run(d)[1]["D5.dates"], "GAP")


class Statements(unittest.TestCase):
    def test_cash_does_not_roll(self):
        d = clean()
        d["statements"]["years"][-1]["cash_end"] *= 1.2
        self.assertEqual(run(d)[1]["D6.cash.FY2025"], "CONFLICT")

    def test_unexplained_equity_plug(self):
        d = clean()
        y = d["statements"]["years"][-1]
        y["oci_and_other"] = -0.3 * y["ni"]
        y["equity_end"] += y["oci_and_other"]
        self.assertEqual(run(d)[1]["D6.equity_other.FY2025"], "GAP")

    def test_free_cash_flow_that_went_nowhere(self):
        d = clean()
        for y in d["statements"]["years"]:
            y["net_cash_end"] = 300.0          # five years of free cash flow, no build in net cash
        self.assertEqual(run(d)[1]["D6.cumulative"], "CONFLICT")


class OwnerEarnings(unittest.TestCase):
    def test_typed_figure_differs_from_components(self):
        d = clean()
        d["owner_earnings"]["value"] *= 1.1
        self.assertEqual(run(d)[1]["D7"], "CONFLICT")

    def test_component_must_equal_statement_line(self):
        d = clean()
        d["owner_earnings"]["components"]["FY2025"]["op_profit"] += 20
        self.assertEqual(run(d)[1]["D7"], "CONFLICT")

    def test_net_income_base_or_stock_comp_add_back_is_rejected(self):
        d = clean()
        d["owner_earnings"]["components"]["FY2025"]["other_non_cash"] = 30     # e.g. stock compensation added back
        self.assertEqual(run(d)[1]["D7"], "CONFLICT")

    def test_financial_items_inside_operating_profit_need_a_note(self):
        d = clean()
        for c in d["owner_earnings"]["components"].values():
            c["non_operating"] = 5.0                # investment gains booked inside operating profit
        d["owner_earnings"]["value"] = round(sum(vi.oe_year(c) for c in d["owner_earnings"]["components"].values()) / 3, 2)
        self.assertEqual(run(d)[1]["D7"], "GAP")
        d["owner_earnings"]["non_operating_note"] = "investment gains and fair-value changes, income statement note"
        self.assertEqual(run(d)[1]["D7"], "PASS")

    def test_margin_method_scales_to_latest_revenue(self):
        d = clean()
        oe = d["owner_earnings"]
        rev = {y["fy"]: y["revenue"] for y in d["statements"]["years"]}
        margin = sum(vi.oe_year(c) / rev[fy] for fy, c in oe["components"].items()) / 3
        oe["method"] = "margin"
        self.assertEqual(run(d)[1]["D7"], "CONFLICT")                 # the three-year average no longer matches
        oe["value"] = round(rev["FY2025"] * margin, 2)
        self.assertEqual(run(d)[1]["D7"], "PASS")

    def test_organic_roic_excludes_acquired_capital(self):
        d = clean()
        for y in d["statements"]["years"]:
            y["invested_capital_organic"] = y["invested_capital"] / 2
        roic = run(d)[0]["derived"]["roic"]
        self.assertAlmostEqual(roic["organic_average"], 2 * roic["average"], places=3)

    def test_measured_roic_is_derived(self):
        roic = run(clean())[0]["derived"]["roic"]
        self.assertAlmostEqual(roic["average"], 0.13 * 0.75 / 0.5, places=3)
        self.assertAlmostEqual(roic["incremental"], 0.13 * 0.75 / 0.5, places=2)

    def test_owner_earnings_far_above_free_cash_flow(self):
        d = clean()
        for fy, c in d["owner_earnings"]["components"].items():
            c["maintenance_capex"] = 0
            c["tax_rate"] = 0.0
        comps = d["owner_earnings"]["components"].values()
        d["owner_earnings"]["value"] = round(sum(vi.oe_year(c) for c in comps) / 3, 2)
        self.assertEqual(run(d)[1]["D7.vs_fcf"], "GAP")


class History(unittest.TestCase):
    def test_latest_years_must_be_filed(self):
        d = clean()
        d["statements"]["years"][-1]["basis"] = "aggregator"
        self.assertEqual(run(d)[1]["D8.basis"], "GAP")

    def test_aggregator_history_only_as_context(self):
        d = clean()
        d["statements"]["years"][0]["basis"] = "aggregator"
        self.assertEqual(run(d)[1]["D8.basis"], "GAP")
        d["statements"]["years"][0]["context_only"] = True
        res, st = run(d)
        self.assertEqual(st["D8.basis"], "PASS")
        self.assertNotIn("FY2021", res["derived"]["usable_history"])

    def test_unexplained_break(self):
        d = clean()
        d["statements"]["years"][2]["shares_end"] = 3000      # a split nobody noted
        self.assertEqual(run(d)[1]["D8.breaks"], "GAP")

    def test_too_few_years(self):
        d = clean()
        d["statements"]["years"] = d["statements"]["years"][-3:]
        self.assertEqual(run(d)[1]["D8.years"], "GAP")


class Windows(unittest.TestCase):
    def anker(self):
        # process-lessons.md Class 3 case 1: 9M-25 OCF -865 / NI 1,933; 9M-26 +378 / 2,261; Q4-25 +1,346 / 612.
        d = clean()
        d["statements"]["years"][-1].update(ocf=481, ni=2545)
        d["statements"]["ytd_prior"] = {"label": "9M-2025", "months": 9, "ocf": -865, "ni": 1933}
        d["statements"]["ytd"] = {"label": "9M-2026", "months": 9, "ocf": 378, "ni": 2261}
        return d

    def test_anker_ttm_is_computed(self):
        res, st = run(self.anker())
        self.assertEqual(st["D9"], "PASS")
        self.assertEqual(res["derived"]["windows"]["ttm"]["ocf"], 1724)
        self.assertEqual(res["derived"]["windows"]["ocf_to_ni"]["TTM"], 0.6)

    def test_anker_estimated_ttm_rejected(self):
        d = self.anker()
        d["statements"]["ttm"] = {"ocf": 0}        # the "~0.0" estimate
        self.assertEqual(run(d)[1]["D9"], "CONFLICT")

    def test_stub_without_matching_prior_window(self):
        d = self.anker()
        del d["statements"]["ytd_prior"]
        self.assertEqual(run(d)[1]["D9"], "GAP")


class FxAndStakes(unittest.TestCase):
    def test_shenzhen_international_assumed_rate(self):
        # process-lessons.md Class 2: RMB/HKD assumed at 1.10 vs the CFETS 6-Nov-2026 fixing of 1.1667.
        d = clean()
        d["fx"] = [{"from": "CNY", "to": "HKD", "rate": 1.10, "basis": "assumed", "date": "2026-11-06", "source": ""}]
        self.assertEqual(run(d)[1]["D10"], "GAP")
        d["fx"] = [{"from": "CNY", "to": "HKD", "rate": 1.1667, "basis": "fixing", "date": "2026-11-06",
                    "source": "CFETS central parity"}]
        self.assertEqual(run(d)[1]["D10"], "PASS")

    def stake(self, shares):
        d = clean()
        d["stakes"] = [{"name": "Spotify", "shares_held": shares, "quote": 596, "quote_currency": "USD",
                        "quote_date": "2026-10-23", "carrying_value": 3750, "accounting": "fair_value",
                        "holder_filing": "Schedule 13G filed on Spotify, 2019-02-01"}]
        return with_provenance(d)

    def test_tme_spotify_stake_containment(self):
        # process-lessons.md Check 22: 8,552,440 shares at ~US$596 = US$5.10bn inside a US$3.75bn line.
        self.assertEqual(run(self.stake(8552440))[1]["D11.Spotify"], "CONFLICT")
        self.assertEqual(run(self.stake(4276200))[1]["D11.Spotify"], "PASS")


class DcfGate(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = self.tmp.name
        self.data = clean()
        self.inputs = os.path.join(self.dir, "inputs_TEST_2026-11-10.json")
        self.write_inputs()
        self.validate()
        d = vi.validate(self.data)["derived"]
        self.cfg = {"ticker": "TEST", "validation": "validation_TEST_2026-11-10.json",
                    "owner_earnings": d["owner_earnings"], "treasury": self.data["treasury"],
                    "diluted_shares": d["valuation_count"], "price": d["price"], "currency": "USD",
                    "reinvestment": {"ronic": 0.19, "terminal_ronic": 0.11, "basis": "measured ROIC, FY2021-FY2025"},
                    "scenarios": [{"name": "Base", "g1": 0.05, "g2": 0.03, "tg": 0.02, "p": 1.0}]}

    def tearDown(self):
        self.tmp.cleanup()

    def write_inputs(self):
        with open(self.inputs, "w") as fh:
            json.dump(self.data, fh)

    def validate(self):
        return subprocess.run([sys.executable, os.path.join(SCRIPTS, "validate_inputs.py"), self.inputs],
                              capture_output=True, text=True)

    def dcf(self, *flags):
        path = os.path.join(self.dir, "dcf.json")
        with open(path, "w") as fh:
            json.dump(self.cfg, fh)
        return subprocess.run([sys.executable, os.path.join(SCRIPTS, "scenario_dcf.py"), path, *flags],
                              capture_output=True, text=True)

    def test_runs_with_a_valid_stamp(self):
        r = self.dcf()
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(json.loads(r.stdout)["data_gate"]["status"], "VERIFIED")

    def test_refuses_without_validation(self):
        del self.cfg["validation"]
        r = self.dcf()
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("no 'validation'", r.stderr)

    def test_refuses_when_inputs_changed_after_validation(self):
        self.data["price"]["value"] = 31.0
        self.write_inputs()
        self.assertIn("changed after it was validated", self.dcf().stderr)

    def test_refuses_a_retyped_figure(self):
        self.cfg["owner_earnings"] *= 1.05
        self.assertIn("not the validated figure", self.dcf().stderr)

    def test_qualified_data_still_values_and_says_so(self):
        for p in self.data["provenance"].values():
            del p["verified"]                                   # second read never done: a gap
        self.write_inputs()
        self.assertEqual(self.validate().returncode, 0)
        r = self.dcf()
        self.assertEqual(r.returncode, 0, r.stderr)
        out = json.loads(r.stdout)
        self.assertEqual(out["data_gate"]["status"], "QUALIFIED")
        self.assertEqual(out["data_gate"]["consequences"]["conviction_cap"], 6)
        self.assertTrue(out["data_gate"]["gaps"])
        self.assertTrue(any("PROVISIONAL" in w for w in out["warnings"]))

    def test_unresolved_data_runs_only_as_a_named_reading(self):
        self.data["shares"]["valuation_count"] = 5000           # contradicts period-end + dilution
        self.write_inputs()
        self.assertEqual(self.validate().returncode, 1)
        self.assertIn("UNRESOLVED", self.dcf().stderr)
        self.cfg["diluted_shares"] = 5000
        r = self.dcf("--reading", "count as typed (5,000m)")
        self.assertEqual(r.returncode, 0, r.stderr)
        out = json.loads(r.stdout)
        self.assertEqual(out["data_gate"]["reading"], "count as typed (5,000m)")
        self.assertTrue(any("No verdict" in w for w in out["warnings"]))

    def test_pending_second_pass_is_not_a_final_validation(self):
        r = subprocess.run([sys.executable, os.path.join(SCRIPTS, "validate_inputs.py"), self.inputs, "--stage", "first"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0)
        self.assertIn("final stage", self.dcf().stderr)

    def test_growth_is_charged_for_reinvestment(self):
        base = json.loads(self.dcf().stdout)["scenarios"][0]["value_per_share"]
        self.cfg["reinvestment"]["ronic"] = 0.10            # same growth needs twice the capital
        self.assertLess(json.loads(self.dcf().stdout)["scenarios"][0]["value_per_share"], base)

    def test_terminal_growth_adds_almost_nothing_when_terminal_ronic_equals_the_rate(self):
        self.cfg["reinvestment"]["terminal_ronic"] = 0.10   # equals the USD base rate used here
        a = json.loads(self.dcf().stdout)["scenarios"][0]["value_per_share"]
        self.cfg["scenarios"][0]["tg"] = 0.0
        b = json.loads(self.dcf().stdout)["scenarios"][0]["value_per_share"]
        self.assertAlmostEqual(a, b, delta=0.025 * b)       # only the first year's 2% step remains

    def test_net_cash_is_counted_once(self):
        out = json.loads(self.dcf().stdout)
        br = out["scenarios"][0]["per_share_bridge"]
        self.assertAlmostEqual(br["operations_years_1_10"] + br["terminal"] + br["net_cash"] + br["other"],
                               out["scenarios"][0]["value_per_share"], places=1)
        self.assertAlmostEqual(br["net_cash"], -out["net_debt_used"] / self.cfg["diluted_shares"], places=2)

    def test_headline_fair_value_is_the_lower_of_base_and_weighted(self):
        self.cfg["scenarios"] = [{"name": "Bear", "g1": 0.0, "g2": 0.0, "tg": 0.0, "p": 0.5, "oe_factor": 0.8,
                                  "oe_factor_reason": "margin compression"},
                                 {"name": "Base", "g1": 0.05, "g2": 0.03, "tg": 0.02, "p": 0.5}]
        out = json.loads(self.dcf().stdout)
        base = next(x["value_per_share"] for x in out["scenarios"] if x["name"] == "Base")
        self.assertLess(out["weighted_iv"], base)
        self.assertEqual(out["fair_value"], out["weighted_iv"])
        self.cfg["scenarios"][0].update(name="Bull", g1=0.10, g2=0.06, oe_factor=1.0)
        out = json.loads(self.dcf().stdout)
        self.assertEqual(out["fair_value"], next(x["value_per_share"] for x in out["scenarios"] if x["name"] == "Base"))

    def test_missing_reinvestment_inputs_stop_the_run(self):
        del self.cfg["reinvestment"]
        self.assertIn("Growth is not free", self.dcf().stderr)

    def test_ronic_above_measured_return_is_flagged(self):
        self.cfg["reinvestment"]["ronic"] = 0.40
        self.assertTrue(any("above the measured return" in w for w in json.loads(self.dcf().stdout)["warnings"]))

    def test_illustrative_runs_and_is_labelled(self):
        del self.cfg["validation"]
        r = self.dcf("--illustrative")
        self.assertEqual(r.returncode, 0, r.stderr)
        out = json.loads(r.stdout)
        self.assertEqual(out["data_gate"]["status"], "UNVALIDATED")
        self.assertTrue(any("UNVALIDATED" in w for w in out["warnings"]))


if __name__ == "__main__":
    unittest.main()
