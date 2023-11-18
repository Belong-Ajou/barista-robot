from barista_template import BaristaTemplate
from robot_controller.robot_behavior import RinseBehavior,SkipRinse,Rinse
from robot_controller.robot_controller import RobotController
import conf
from time import sleep

class BaristaBasic(BaristaTemplate):
    def __init__(self, ip):
        super().__init__()
        self.robot = RobotController(ip)
        return

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
        self.robot.move_PTP(cartesian_pose = point["P1"])
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
        self.robot.move_PTP(cartesian_pose = point["P6"])
        # 7.PTP - 원두 붓기 (Pour it)
        self.robot.move_PTP(point["J7"], speed=100)
        # 8.PTP - 원두 붓고 원위치
        self.robot.move_PTP(cartesian_pose = point["P5"])
        # 9.Linear - 컵 놓는 위치 수직선 상에 위치
        self.robot.move_linear(point["J4"], point["P4"])
        # 10.Linear - 컵 정위치
        self.robot.move_linear(point["J2"], point["P2"])
        # Gripper - 컵 놓기
        self.robot.control_gripper(100)

        return

    def _bloom(self, time: int, amount: int):
        print("Bloom: Pour in {0} grams of hot water, wait {1} seconds".format(str(amount), str(time)))
        # self.robot.set_speed(30.0)
        # point = conf.bloom_point
        # # 1.Linear - 주전자 잡으러 가기 1단계 (1st moving step to pick up the kettle)
        # self.robot.move_linear(point["J1"], point["P1"])
        # # 2.PTP - 주전자 잡으러 가기 2단계 (2nd moving step to pick up the kettle)
        # self.robot.move_PTP(point["J2"])
        # # 3.PTP - 주전자 잡으러 가기 3단계 (3rd moving step to pick up the kettle)
        # self.robot.move_PTP(point["J3"])
        # # Gripper - 주전자에 ARM 넣기 전에 조여줌
        # self.robot.control_gripper(50)
        # # 4.Linear - 주전자에 ARM 집어 넣기
        # self.robot.move_linear(point["J4"], point["P4"])
        # # Gripper - 주전자에 잡기
        # self.robot.control_gripper(0)
        # # 5.Linear - 이동 중 턱에 걸리는 것을 방지하기 위해 잡은 상태로 살짝 들어올리기
        # self.robot.move_linear(point["J5"], point["P5"])
        # # 6.PTP - 뜸 들이러 가기 1단계 (1st moving step to bloom)
        # self.robot.move_PTP(point["J6"])
        # # 7.PTP - 뜸 들이러 가기 2단계 (2nd moving step to bloom)
        # self.robot.move_PTP(point["J7"])
        # # 8.PTP - 뜸 들이러 가기 3단계 (3rd moving step to bloom)
        # self.robot.move_PTP(point["J8"])
        return

    def _pour(self, time: int, amount: int):
        print("Pour: Pour in {0} grams of hot water, wait {1} seconds".format(str(amount), str(time)))
        # self.robot.set_speed(30.0)
        # point = conf.pour_point
        # # 1.PTP - 1st Pour를 위한 이동 (Move to pour 1st)
        # self.robot.move_PTP(point["J1"])
        # self.robot.move_Spiral(point["J2"], point["P2"])
        # self.robot.move_PTP(point["J17"])
        # # 2.PTP - 2nd Pour를 위한 이동 (Move to pour 2nd)
        # self.robot.move_PTP(point["J5"])
        # self.robot.move_Spiral(point["J6"], point["P6"])
        # self.robot.move_PTP(point["J17"])
        # # 3.PTP - 3rd Pour를 위한 이동 (Move to pour 3rd)
        # self.robot.move_PTP(point["J9"])
        # self.robot.move_Spiral(point["J10"], point["P10"])
        # self.robot.move_PTP(point["J17"])
        # # 4.PTP - 4th Pour를 위한 이동 (Move to pour 4th)
        # self.robot.move_PTP(point["J9"])
        # self.robot.move_Spiral(point["J10"], point["P10"])
        # self.robot.move_PTP(point["J17"])
        # # 5.PTP - 5th Pour를 위한 이동 (Move to pour 5th)
        # self.robot.move_PTP(point["J13"])
        # self.robot.move_Spiral(point["J14"], point["P14"])
        # self.robot.move_PTP(point["J17"])
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