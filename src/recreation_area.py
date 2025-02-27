class RecreationArea:
    def __init__(self):
        self.__state: float = 0

    def is_built(self) -> bool:
        return self.__state == 1

    def build(self) -> None:
        if not self.is_built():
            self.__state += 0.2

    def get_state(self) -> float:
        return round(self.__state, 2)
