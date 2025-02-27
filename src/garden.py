from math import ceil

from src.garden_exceptions import NoSuchPlant
from src.plant import Plant
from src.soil import Soil


class Garden:
    def __init__(self, plants: list[Plant]):
        self.__plants: list[Plant] = plants
        self.__soil = Soil()

    def can_be_added(self, plant: Plant) -> bool:
        return not self.has(plant.name)

    def add(self, plant: Plant) -> None:
        if not self.has(plant.name):
            self.__plants.append(plant)

    def get_plant_list_string(self) -> str:
        return ', '.join([i.name for i in self.__plants])

    def get_info(self) -> None:
        if not self.__plants:
            print("Your garden is empty!")
        for plant in self.__plants:
            print(f"""Name: {plant.name}
Size: {plant.get_size()} cm
Health: {plant.get_health()}
Mood: {plant.get_mood()}
""")
        print(f"Soil acidity: {self.__soil.get_balance()}")
        print(f"Soil quality: {ceil(self.__soil.get_quality() * 100)}%")

    def has(self, plant_name: str) -> bool:
        plant_list: list[str] = [i.name for i in self.__plants]
        return plant_name in plant_list

    def get_plant(self, plant_name: str) -> Plant:
        for i in self.__plants:
            if i.name == plant_name:
                return i
        raise NoSuchPlant

    def remove_plant(self, plant_name: str) -> None:
        try:
            plant: Plant = self.get_plant(plant_name)
            self.__plants.remove(plant)
        except NoSuchPlant:
            print("There's no such plant in the garden!")

    def clean_up(self) -> None:
        plants_to_clean_up: list[Plant] = [i for i in self.__plants if not i.is_alive()]
        for i in plants_to_clean_up:
            self.__plants.remove(i)

    def water(self) -> None:
        for i in self.__plants:
            i.water()
        print("Plants have been watered!")

    def cheat_boost(self) -> None:
        for i in self.__plants:
            i.cheat_boost()
        print("You put a gnome in the garden. Plants absolutely love it!")
        self.__soil.cheat_boost()

    def weed(self) -> None:
        self.__soil.weed()

    def normalize(self) -> None:
        self.__soil.normalize()

    def fertilize(self) -> None:
        self.__soil.fertilize()

    def spend_day_if_user_works(self) -> None:
        for i in self.__plants:
            i.spend_day_if_user_works(self.__soil)
        self.clean_up()
        self.__soil.spend_day()

    def spend_day_if_user_rests(self) -> None:
        for i in self.__plants:
            i.spend_day_if_user_rests()
        self.__soil.spend_day()
