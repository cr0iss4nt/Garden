import unittest

from src.recreation_area import RecreationArea


class TestRecreationArea(unittest.TestCase):
    def test_get_state(self):
        area = RecreationArea()
        self.assertEqual(area.get_state(), 0)

    def test_build(self):
        area = RecreationArea()
        for i in range(5):
            self.assertFalse(area.is_built())
            self.assertAlmostEqual(area.get_state(), 0 + i * 0.2)
            area.build()
        self.assertTrue(area.is_built())
        self.assertAlmostEqual(area.get_state(), 1)
