from barista_template import BaristaTemplate
from robot_controller.robot_behavior import RinseBehavior,SkipRinse,Rinse
import conf
from time import sleep

class BaristaBasic(BaristaTemplate):
    def _rinse(self):
        rinse_action = RinseBehavior(SkipRinse())
        rinse_action.rinse()
        return

    def _place_coffee_grounds(self):
        print("Place the coffee grounds in the filter paper.")
        self.robot.set_speed(30.0)
        point = conf.place_coffee_grounds_point
        # Gripper - 그리퍼 벌리기 (Open the gripper)
        self.robot.open_gripper()
        # 1.PTP - 원두 컵 앞에 위치 (Locate in front of the cup of coffee beans)
        self.robot.move_PTP(point["J1"])
        # 2.Linear - 원두 컵쪽으로 들어가기 (Move forward to the cup)
        self.robot.move_linear(point["J2"], point["P2"])
        # 3.Linear - 원두 컵 잡기 위해 올림 (Move up to grab the cup)
        self.robot.move_linear(point["J3"], point["P3"])
        # Gripper - 조여서 컵 잡기 (Close the gripper and grap the cup)
        self.robot.control_gripper(0)
        # 4.Linear - 잡은 뒤 컵 올리기 (Pick up the cup)
        self.robot.move_linear(point["J4"], point["P4"])
        # 5.Linear - 붓기 전, 드리퍼 위에 위치시키기 (Locate the cup over the dripper)
        self.robot.move_linear(point["J5"], point["P5"])
        # 6.PTP - 붓기 위해 위치 조정 (Adjust the coordinates to pour it)
        self.robot.move_PTP(point["J6"])
        # 7.PTP - 원두 붓기 (Pour it)
        self.robot.move_PTP(point["J7"], speed=100)
        return

    def _bloom(self, time: int, amount: int):
        print("Bloom: Pour in {0} grams of hot water, wait {1} seconds".format(str(amount), str(time)))
        return

    def _pour(self, time: int, amount: int):
        print("Pour: Pour in {0} grams of hot water, wait {1} seconds".format(str(amount), str(time)))
        return

    def _wait(self, time:int):
        print("Wait {0} seconds".format(str(time)))

    def _exit(self):
        print("Enjoy you coffee!")
        return

if __name__ == "__main__":
    my_recipe = {"bloom":[10, 100], "pour": [10, 90], "wait":[120]}
    barista = BaristaBasic("192.168.58.2")
    barista.make_coffee(my_recipe)