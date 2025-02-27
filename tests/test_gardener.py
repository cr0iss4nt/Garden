import unittest

from src.garden import Garden
from src.gardener import Gardener, WAGE, DECORATION_COST
from src.plant import Plant


class TestGardener(unittest.TestCase):
    def test_start(self):
        gardener = Gardener()
        money = gardener.get_money_amount()
        self.assertGreaterEqual(money, 50)
        self.assertLessEqual(money, 1050)
        self.assertEqual(gardener.get_soil_normalizer_number(), 0)
        self.assertEqual(gardener.get_fertilizer_number(), 0)

    def test_work(self):
        gardener = Gardener()
        old_money: int = gardener.get_money_amount()
        gardener.work()
        new_money: int = gardener.get_money_amount()
        self.assertEqual(old_money + WAGE, new_money)

    def test_pay(self):
        gardener = Gardener()
        old_money: int = gardener.get_money_amount()
        gardener.pay(333)
        new_money: int = gardener.get_money_amount()
        self.assertEqual(old_money - 333, new_money)

    def test_soil_normalizer(self):
        gardener = Gardener()
        garden = Garden([Plant("A")])
        gardener.work()
        gardener.work()
        gardener.work()
        old_number: int = gardener.get_soil_normalizer_number()
        gardener.buy_soil_normalizer()
        new_number: int = gardener.get_soil_normalizer_number()
        self.assertEqual(old_number, 0)
        self.assertEqual(new_number, 1)
        gardener.use_soil_normalizer(garden)
        newest_number: int = gardener.get_soil_normalizer_number()
        self.assertEqual(old_number, newest_number)
        gardener.use_soil_normalizer(garden)
        self.assertEqual(gardener.get_soil_normalizer_number(), old_number)

    def test_soil_fertilizer(self):
        gardener = Gardener()
        garden = Garden([Plant("A")])
        gardener.work()
        gardener.work()
        gardener.work()
        old_number: int = gardener.get_fertilizer_number()
        gardener.buy_soil_fertilizer()
        new_number: int = gardener.get_fertilizer_number()
        self.assertEqual(old_number, 0)
        self.assertEqual(new_number, 1)
        gardener.use_soil_fertilizer(garden)
        newest_number: int = gardener.get_fertilizer_number()
        self.assertEqual(old_number, newest_number)
        gardener.use_soil_fertilizer(garden)
        self.assertEqual(gardener.get_soil_normalizer_number(), old_number)

    def test_buy_plant(self):
        gardener = Gardener()
        garden = Garden([])
        gardener.work()
        garden_list_1 = garden.get_plant_list_string()
        self.assertEqual(garden_list_1, "")
        gardener.buy_plant(garden, "A")
        garden_list_2 = garden.get_plant_list_string()
        self.assertEqual(garden_list_2, "A")
        gardener.buy_plant(garden, "B")
        garden_list_3 = garden.get_plant_list_string()
        self.assertEqual(garden_list_3, "A, B")

    def test_fix_hoe(self):
        gardener = Gardener()
        gardener.work()
        old_money = gardener.get_money_amount()
        gardener.fix_hoe()
        new_money = gardener.get_money_amount()
        self.assertGreater(old_money, new_money)

    def test_decorate(self):
        gardener = Gardener()
        for i in range(15):
            gardener.work()
        money_1 = gardener.get_money_amount()
        garden = Garden([Plant("A")])
        gardener.decorate(garden)
        money_2 = gardener.get_money_amount()
        self.assertEqual(money_1, money_2 + DECORATION_COST)
