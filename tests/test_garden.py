import unittest

from src.garden import Garden
from src.plant import Plant


class TestGarden(unittest.TestCase):
    def test_add(self):
        plant_a = Plant("A")
        garden = Garden([plant_a])
        garden_str_1 = garden.get_plant_list_string()
        self.assertEqual(garden_str_1, "A")
        self.assertFalse(garden.can_be_added(plant_a))
        plant_b = Plant("B")
        self.assertTrue(garden.can_be_added(plant_b))
        garden.add(plant_b)
        garden_str_2 = garden.get_plant_list_string()
        self.assertEqual(garden_str_2, "A, B")
        garden.add(plant_a)
        garden_str_3 = garden.get_plant_list_string()
        self.assertEqual(garden_str_3, "A, B")

    def test_delete(self):
        garden = Garden([Plant("A")])
        garden_str = garden.get_plant_list_string()
        self.assertEqual(garden_str, "A")
        garden.remove_plant("A")
        garden_str = garden.get_plant_list_string()
        self.assertEqual(garden_str, "")
        garden.remove_plant("A")
        garden_str = garden.get_plant_list_string()
        self.assertEqual(garden_str, "")

    def test_spend_day(self):
        garden = Garden([Plant("A"), Plant("B")])
        garden_str_1 = garden.get_plant_list_string()
        for i in range(1000):
            garden.spend_day_if_user_rests()
        garden_str_2 = garden.get_plant_list_string()
        self.assertEqual(len(garden_str_1), len(garden_str_2))
        for i in range(1000):
            garden.spend_day_if_user_works()
        garden_str_3 = garden.get_plant_list_string()
        self.assertGreaterEqual(len(garden_str_2), len(garden_str_3))
