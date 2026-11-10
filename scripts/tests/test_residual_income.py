"""Tests for the residual-income script. Run:  python3 -m unittest discover -s scripts/tests"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SCRIPTS)
import residual_income as ri  # noqa: E402


def run(cfg):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
        json.dump(cfg, fh)
    try:
        r = subprocess.run([sys.executable, os.path.join(SCRIPTS, "residual_income.py"), fh.name], capture_output=True, text=True)
        return json.loads(r.stdout)
    finally:
        os.unlink(fh.name)


BASE = {"bvps": 100.0, "roe": 0.15, "payout": 0.32, "r": 0.12, "fade_years": 20, "terminal_roe_spread": 0.02,
        "terminal_growth": 0.055, "price": 150.0}


class ResidualIncome(unittest.TestCase):
    def test_roe_equal_to_cost_of_equity_is_worth_book(self):
        v, pv, tv = ri.value(100.0, 0.12, 0.3, 0.12, 20, 0.12, 0.04)
        self.assertAlmostEqual(v, 100.0, places=6)

    def test_constant_roe_matches_the_closed_form(self):
        # ROE held at 15% for ever with full fade length irrelevant: compare a long fade-free run with Gordon.
        roe, pay, r = 0.14, 0.5, 0.12
        g = roe * (1 - pay)
        closed = 100 + (roe - r) * 100 / (r - g)
        v, _, _ = ri.value(100.0, roe, pay, r, 30, roe, g)
        self.assertAlmostEqual(v, closed, places=4)

    def test_longer_fade_and_higher_terminal_roe_raise_value(self):
        out = run(BASE)
        by = {(x["fade_years"], x["terminal_roe"]): x["value_per_share"] for x in out["fade_ladder"]}
        self.assertLess(by[(10, 0.12)], by[(20, 0.14)])
        self.assertLess(by[(20, 0.14)], by[(30, 0.14)])
        self.assertTrue(out["fade_ladder_spread_pct"] > 0)

    def test_justified_pb_is_void_where_growth_reaches_r(self):
        # ICICI case in intrinsic-value.md: ROE 16%, payout 15.5% -> g 13.5% vs r 12%.
        out = run({**BASE, "roe": 0.16, "payout": 0.155})
        self.assertEqual(out["justified_pb"]["status"], "VOID")
        none = next(x for x in out["fade_ladder"] if x["fade_years"] == "none")
        self.assertIsNone(none["value_per_share"])            # stated as undefined, not omitted

    def test_hdfc_case_is_fragile_not_void(self):
        # HDFC case: ROE 15%, retention 68.1% -> g 10.2%, r - g about 1.8 points, justified P/B about 2.68x.
        out = run({**BASE, "roe": 0.15, "payout": 0.319})
        self.assertEqual(out["justified_pb"]["status"], "USABLE")
        self.assertAlmostEqual(out["justified_pb"]["multiple"], 2.68, delta=0.05)


if __name__ == "__main__":
    unittest.main()
