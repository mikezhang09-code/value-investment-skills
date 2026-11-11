"""Tests for scenario_dcf.py outputs that are not covered by the data-gate tests.

Run from the repo root:  python3 -m unittest discover -s scripts/tests -v
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(HERE)

BRIDGE = 300.0   # e.g. a listed stake, USD millions
SHARES = 100.0


def config(bridge):
    return {"ticker": "TEST", "owner_earnings": 100.0, "net_debt": -50.0, "diluted_shares": SHARES,
            "price": 20.0, "currency": "USD", "discount_rate_basis": "test",
            "reinvestment": {"ronic": 0.30, "terminal_ronic": 0.12, "basis": "test"},
            "bridge": bridge, "legacy_owner_earnings": 120.0,
            "epv": {"after_tax_operating_earnings": 90.0, "excess_cash": 50.0, "total_debt": 0.0},
            "scenarios": [{"name": "Base", "g1": 0.05, "g2": 0.03, "tg": 0.02, "p": 1.0}]}


def run(cfg):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
        json.dump(cfg, fh)
    try:
        r = subprocess.run([sys.executable, os.path.join(SCRIPTS, "scenario_dcf.py"), fh.name, "--illustrative"],
                           capture_output=True, text=True)
    finally:
        os.unlink(fh.name)
    if r.returncode:
        raise AssertionError(r.stdout + r.stderr)
    return json.loads(r.stdout)


class BridgeItemsReachEveryPerShareFigure(unittest.TestCase):
    """A bridge item (stake +, minority -) moves every per-share output by bridge / shares.
    Case: Zoom pilot 2026-11-10 -- EPV and the legacy print left out $8.39/share of strategic investments."""

    @classmethod
    def setUpClass(cls):
        cls.without = run(config([]))
        cls.with_ = run(config([{"label": "listed stake", "amount": BRIDGE, "reason": "test"}]))
        cls.step = BRIDGE / SHARES

    def moved(self, path):
        a, b = self.without, self.with_
        for k in path:
            a, b = a[k], b[k]
        self.assertAlmostEqual(b - a, self.step, places=1, msg=".".join(map(str, path)))

    def test_scenario_value(self):
        self.assertAlmostEqual(self.with_["scenarios"][0]["value_per_share"]
                               - self.without["scenarios"][0]["value_per_share"], self.step, places=1)

    def test_fair_value(self):
        self.moved(["fair_value"])

    def test_zero_growth_value(self):
        self.moved(["zero_growth_oe_value"])

    def test_epv(self):
        self.moved(["epv_per_share"])

    def test_legacy_method_base(self):
        self.moved(["legacy_method_base", "value_per_share"])


class AlternativeBasis(unittest.TestCase):
    def test_illustrative_run_can_print_a_second_basis(self):
        cfg = config([])
        cfg["alternative_owner_earnings"] = {"basis": "three-year average margin", "value": 80.0}
        out = run(cfg)
        self.assertLess(out["alternative_basis"]["fair_value"], out["fair_value"])

    def test_no_second_basis_unless_given(self):
        self.assertNotIn("alternative_basis", run(config([])))


if __name__ == "__main__":
    unittest.main()
