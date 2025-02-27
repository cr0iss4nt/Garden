import random
from math import ceil

from src.garden import Garden
from src.hoe import Hoe
from src.plant import Plant
from src.recreation_area import RecreationArea

WAGE: int = 200
TOOL_FIX_COST: int = 40
DECORATION_COST: int = 3000
RECREATION_AREA_BUILD_COST: int = 1000
NEW_PLANT_COST: int = 150
SOIL_NORMALIZER_COST: int = 500
SOIL_FERTILIZER_COST: int = 200


class Gardener:
    def __init__(self):
        self.__money: int = round(random.random() * 1000) + 50
        self.__hoe = Hoe()
        self.__soil_normalizer: int = 0
        self.__soil_fertilizer: int = 0

    def get_money_amount(self) -> int:
        return self.__money

    def buy_plant(self, garden: Garden, plant_name: str) -> None:
        if self.can_afford(NEW_PLANT_COST):
            plant = Plant(plant_name)
            garden.add(plant)
        else:
            print("Not enough money to buy a new plant!")

    def buy_soil_fertilizer(self) -> None:
        if self.can_afford(SOIL_FERTILIZER_COST):
            self.__soil_fertilizer += 1
            self.pay(SOIL_FERTILIZER_COST)
            print("Bought a soil fertilizer!")
        else:
            print("Not enough money to buy a soil fertilizer!")

    def buy_soil_normalizer(self) -> None:
        if self.can_afford(SOIL_NORMALIZER_COST):
            self.__soil_normalizer += 1
            self.pay(SOIL_NORMALIZER_COST)
            print("Bought a soil acidity normalizer!")
        else:
            print("Not enough money to buy a soil acidity normalizer!")

    def fix_hoe(self) -> None:
        if self.can_afford(TOOL_FIX_COST):
            self.__hoe.fix()
            self.pay(TOOL_FIX_COST)
            print(f"Fixed the hoe! Current state: {ceil(self.__hoe.get_state() * 100)}")
        else:
            print("Not enough money to fix the hoe!")

    # available only if not built yet
    def build_recreation_area(self, recreation_area: RecreationArea) -> None:
        if self.__money >= RECREATION_AREA_BUILD_COST:
            recreation_area.build()
            self.__money -= RECREATION_AREA_BUILD_COST
            print(f"Good job! Current state: {recreation_area.get_state() * 100}% built")
        else:
            print("Not enough money to build the recreation area!")

    def get_soil_normalizer_number(self) -> int:
        return self.__soil_normalizer

    def get_fertilizer_number(self) -> int:
        return self.__soil_fertilizer

    def use_soil_normalizer(self, garden: Garden) -> None:
        if self.__soil_normalizer > 0:
            self.__soil_normalizer -= 1
            garden.normalize()
        else:
            print("You don't have soil acidity normalizers!")

    def use_soil_fertilizer(self, garden: Garden) -> None:
        if self.__soil_fertilizer > 0:
            self.__soil_fertilizer -= 1
            garden.fertilize()
        else:
            print("You don't have soil fertilizers!")

    def weed(self, garden: Garden) -> None:
        if self.__hoe.is_usable():
            self.__hoe.use()
            garden.weed()
            print("The garden has been weeded!")
        else:
            print("Couldn't weed the garden! Fix your hoe!")

    def decorate(self, garden: Garden) -> None:
        if self.__money >= DECORATION_COST:
            garden.cheat_boost()
            self.pay(DECORATION_COST)
        else:
            print("Not enough money to decorate the garden!")

    def work(self) -> None:
        self.__money += WAGE

    def cheat_boost(self) -> None:
        self.__money += 999999

    def pay(self, amount: int) -> None:
        self.__money -= amount

    def can_afford(self, amount: int) -> bool:
        return self.__money >= amount
