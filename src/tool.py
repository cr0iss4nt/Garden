import random


class Tool:
    def __init__(self):
        self.__durability: float = random.random() * 0.8 + 0.2

    def get_state(self) -> float:
        return self.__durability

    def is_usable(self) -> bool:
        return self.__durability >= 0.125

    def use(self) -> None:
        self.__durability -= 0.125

    def fix(self) -> None:
        self.__durability = min(1, self.__durability + 0.25)
