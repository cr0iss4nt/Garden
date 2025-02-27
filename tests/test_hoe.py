import unittest

from src.hoe import Hoe


class TestHoe(unittest.TestCase):
    def test_start_state(self):
        hoe = Hoe()
        state: float = hoe.get_state()
        self.assertLessEqual(state, 1)
        self.assertGreaterEqual(state, 0.2)

    def test_usage(self):
        hoe = Hoe()
        self.assertTrue(hoe.is_usable())
        while hoe.get_state() > 0.125:
            hoe.use()
        self.assertFalse(hoe.is_usable())

    def test_fixing(self):
        hoe = Hoe()
        old_state: float = hoe.get_state()
        hoe.fix()
        new_state: float = hoe.get_state()
        self.assertGreaterEqual(new_state, old_state)
