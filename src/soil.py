import random


class Soil:
    def __init__(self):
        # ph is between 4 and 10
        # plants grow better when it's 7
        # it's represented as a number between 0 and 1,
        # where 0 is 4, 1 is 10, 0.5 is 7
        self.__balance: float = random.random()
        self.__quality: float = random.random()

    def get_balance(self) -> float:
        # output 0.5 as 7 etc.
        return round(self.__balance, 2) * 6 + 4

    def get_quality(self) -> float:
        return round(self.__quality, 2)

    def normalize(self) -> None:
        # make the soil balance closer to 0.5 (i.e. 7)
        self.__balance = self.__balance + (0.5 - self.__balance) * 0.333

    def spend_day(self) -> None:
        self.__quality *= (1 - random.random() * 0.15)

    def weed(self) -> None:
        self.__quality = min(1, self.__quality + random.random() * 0.2)

    def fertilize(self) -> None:
        self.__quality = min(1, self.__quality + random.random() * 0.5)

    def cheat_boost(self) -> None:
        self.__quality = 1
        self.__balance = 0.5
