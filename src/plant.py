import random

from src.soil import Soil

class Plant:
    def __init__(self, name: str):
        self.name: str = name
        self.__mood: float = random.random()
        self.__health: float = random.random()
        self.__size: float = random.random() * 100
        self.__mood_boost_used = False
        self.__alive = True

    def get_mood(self) -> str:
        if self.__mood > 0.666:
            return 'happy'
        elif self.__mood > 0.333:
            return 'ok'
        else:
            return 'sad'

    def get_health(self) -> str:
        if self.__health > 0.666:
            return 'healthy'
        elif self.__health > 0.333:
            return 'ok'
        else:
            return 'sick'

    def get_size(self) -> float:
        return round(self.__size, 2)

    def is_alive(self) -> bool:
        return self.__alive

    def water(self) -> None:
        self.__health = min(1, self.__health + 0.03)
        self.__mood = min(1, self.__mood + 0.01)

    def boost_mood(self) -> None:
        if not self.__mood_boost_used:
            phrases = [f"You pet {self.name}.",
                       f"You remove a bug from {self.name}.",
                       f"You cut {self.name}'s ill leaves."]
            print(random.choice(phrases))
            print("They appreciate your care!")
            self.__mood = min(1, self.__mood * 1.5)
            self.__health = min(1, self.__mood * 1.2)
            self.__mood_boost_used = True
        else:
            print(f"{self.name} needs some space. Leave them alone until tomorrow.")

    def cheat_boost(self) -> None:
        self.__mood = 1
        self.__health = 1
        self.__size *= 2

    def spend_day_if_user_works(self, soil: Soil) -> None:
        self.__health *= pow(soil.get_quality(), 0.5)
        self.__health = self.__health - 0.1 * abs(soil.get_balance() - 7)

        if self.__health > 0:
            self.__mood = max(0, self.__mood - pow(1 - soil.get_quality(), 2))
            self.__mood_boost_used = False
        else:
            self.__alive = False
            print(f"{self.name} is dead!")

    def spend_day_if_user_rests(self) -> None:
        self.__mood = min(1, self.__mood * 1.25)
        self.__mood_boost_used = False
