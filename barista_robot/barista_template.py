from abc import ABC, abstractmethod

class BaristaTemplate(ABC):
    def __init__(self) -> None:
        super().__init__()
        return

    def make_coffee(self, recipe:dict):
        self._rinse()
        self._place_coffee_grounds()
        for step in recipe:
            if step[0] == "bloom":
                self._bloom(step[1], step[2])
            elif step[0] == "pour":
                self._pour(step[1], step[2])
            elif step[0] == "wait":
                self._wait(step[1])
        self._exit()

    @abstractmethod
    def _rinse(self):
        pass

    @abstractmethod
    def _place_coffee_grounds(self):
        pass

    @abstractmethod
    def _bloom(self, time:int, amount:int):
        pass

    @abstractmethod
    def _pour(self, time:int, amount:int):
        pass

    @abstractmethod
    def _wait(self, time:int):
        pass

    @abstractmethod
    def _exit(self):
        pass