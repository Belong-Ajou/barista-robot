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
        self.set_speed(30.0)
        point = conf.place_coffee_grounds_point
        eP=[0.000,0.000,0.000,0.000]
        dP=[1.000,1.000,1.000,1.000,1.000,1.000]
        # 0. 그리퍼 벌리기
        self.robot.ActGripper(1, 1)
        self.robot.MoveGripper(1, 100, 40, 50, 10000, 0)
        # 1.원두 컵 앞에 위치(PTP)
        pose = self.robot.GetForwardKin(point["J1"])  
        cartesian_pose = [pose[1], pose[2], pose[3], pose[4], pose[5], pose[6]]
        ret = self.robot.MoveJ(point["J1"], cartesian_pose, 0, 0, self.speed, 100.0, 100.0, eP, -1.0, 0, dP)
        # 2. 원두 컵쪽으로 들어가기(Linear)
        ret = self.robot.MoveL(point["J2"], point["P2"], 0, 0, self.speed, 100.0, 100.0, -1.0, eP, 0, 0, dP)
        # 3. 원두 컵 잡기 위해 올림(Linear)
        self.robot.MoveL(point["J3"], point["P3"], 0, 0, self.speed, 100.0, 100.0, -1.0, eP, 0, 0, dP)
        # 3A. 조여서 컵 잡기
        self.robot.ActGripper(1, 1)
        self.robot.MoveGripper(1, 0, 40, 50, 10000, 0)
        # 4. 잡은 뒤 컵 올리기(Linear)
        self.robot.MoveL(point["J4"], point["P4"], 0, 0, self.speed, 100.0, 100.0, -1.0, eP, 0, 0, dP)
        # 5. 붓기 전, 드리퍼 위에 위치시키기(Linear)
        self.robot.MoveL(point["J5"], point["P5"], 0, 0, self.speed, 100.0, 100.0, -1.0, eP, 0, 0, dP)
        # 6. 붓기 위해 각도 조정(PTP)
        pose = self.robot.GetForwardKin(point["J6"])  
        cartesian_pose = [pose[1], pose[2], pose[3], pose[4], pose[5], pose[6]]
        self.robot.MoveJ(point["J6"], cartesian_pose, 0, 0, self.speed, 100.0, 100.0, eP, -1.0, 0, dP)
        # 7. 원두 붓기(PTP), 각도조정(Joint6-120)
        pose = self.robot.GetForwardKin(point["J7"])  
        cartesian_pose = [pose[1], pose[2], pose[3], pose[4], pose[5], pose[6]]
        pour_speed = 100.0
        self.robot.MoveJ(point["J7"], cartesian_pose, 0, 0, pour_speed, 100.0, 100.0, eP, -1.0, 0, dP)
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