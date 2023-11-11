import frrpc
from abc import ABC, abstractmethod

class BaristaTemplate(ABC):
    def __init__(self, ip) -> None:
        super().__init__()
        try:
            self.robot = frrpc.RPC(ip)
            self.speed = 10
            self.robot.SetSpeed(self.speed)
        except Exception as e:
            print("[Error]",e)
            self.robot = None
        return

    def set_speed(self, speed):
        self.speed = speed

    def make_coffee(self, recipe:dict):
        self._rinse()
        self._place_coffee_grounds()
        for step in recipe:
            if step == "bloom":
                self._bloom(recipe[step][0], recipe[step][1])
            elif step == "pour":
                self._pour(recipe[step][0], recipe[step][1])
            elif step == "wait":
                self._wait(recipe[step][0])
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