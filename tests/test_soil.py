import unittest

from src.soil import Soil


class TestSoil(unittest.TestCase):
    def test_start_balance(self):
        soil = Soil()
        self.assertLessEqual(soil.get_balance(), 10)
        self.assertGreaterEqual(soil.get_balance(), 4)

    def test_start_quality(self):
        soil = Soil()
        self.assertLessEqual(soil.get_quality(), 1)
        self.assertGreaterEqual(soil.get_quality(), 0)

    def test_normalization(self):
        soil = Soil()
        old_balance = soil.get_balance()
        soil.normalize()
        new_balance = soil.get_balance()
        self.assertGreaterEqual(abs(old_balance - 7), abs(new_balance - 7))

    def test_cheats(self):
        soil = Soil()
        soil.cheat_boost()
        self.assertEqual(soil.get_balance(), 7)
        self.assertEqual(soil.get_quality(), 1)

    def test_spend_day(self):
        soil = Soil()
        old_quality: float = soil.get_quality()
        soil.spend_day()
        new_quality: float = soil.get_quality()
        self.assertGreaterEqual(old_quality, new_quality)

    def test_weed(self):
        soil = Soil()
        old_quality: float = soil.get_quality()
        old_balance: float = soil.get_balance()
        soil.weed()
        new_quality: float = soil.get_quality()
        new_balance: float = soil.get_balance()
        self.assertLess(old_quality, new_quality)
        self.assertEqual(old_balance, new_balance)

    def test_fertilize(self):
        soil = Soil()
        old_quality: float = soil.get_quality()
        old_balance: float = soil.get_balance()
        soil.fertilize()
        new_quality: float = soil.get_quality()
        new_balance: float = soil.get_balance()
        self.assertLess(old_quality, new_quality)
        self.assertEqual(old_balance, new_balance)
