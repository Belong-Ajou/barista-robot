from barista_template import BaristaTemplate
from robot_controller.robot_behavior import RinseBehavior,SkipRinse,Rinse
from robot_controller.robot_controller import RobotController
import conf
from time import sleep
import math

class BaristaBasic(BaristaTemplate):
    def __init__(self, ip):
        super().__init__()
        self.robot = RobotController(ip)
        self.dripper_location = 1
        self.cup_location = 1
    
        return

    def _rinse(self):
        rinse_action = RinseBehavior(SkipRinse())
        rinse_action.rinse()
        self.robot.activate_gripper()
        return

    def _place_coffee_grounds(self):
        print("Place the coffee grounds in the filter paper.")
        self.robot.set_global_speed(50)
        self.robot.set_speed(15.0)
        home_point = conf.home_point
        cup_point = conf.grab_cup_point
        self.robot.move_PTP(cartesian_pose = home_point["P"], joint_pose= home_point["J"])

        cup_offset = (self.cup_location-1)*cup_point["CUP_X_OFFSET"]
        # Gripper - 그리퍼 벌리기 (Open the gripper)
        self.robot.open_gripper()
        # 1.PTP - 원두 컵 앞에 위치 (Locate in front of the cup of coffee beans)
        self.robot.move_cartesian(self._calculate_point(cup_point["P1"], cup_offset, 'x'))
        # 2.Linear - 원두 컵쪽으로 들어가기 (Move forward to the cup)
        self.robot.move_linear(cartesian_pose = self._calculate_point(cup_point["P2"], cup_offset, 'x'))
        # Gripper - 조여서 컵 잡기 (Close the gripper and grap the cup)
        self.robot.close_gripper()
        # 4.Linear - 잡은 뒤 컵 올리기 (Pick up the cup)
        self.robot.move_linear(cartesian_pose = self._calculate_point(cup_point["P1"], cup_offset, 'x'))
        
        dripper_point = conf.locate_coffee_ground_point
        dripper_offset = (self.dripper_location-1)*dripper_point["DRIPPER_Y_OFFSET"]
        # 1.Linear - 붓기 전, 드리퍼 위에 위치시키기 (Locate the cup over the dripper)
        self.robot.move_cartesian(self._calculate_point(dripper_point["P1"], dripper_offset, 'y'))
        # 2.PTP - 붓기 위해 위치 조정 (Adjust the coordinates to pour it)
        self.robot.move_cartesian(self._calculate_point(dripper_point["P2"], dripper_offset, 'y'))
        # 3.PTP - 원두 붓기 (Pour it)
        self.robot.move_cartesian(self._calculate_point(dripper_point["P3"], dripper_offset, 'y'), speed=100.0)
        # 4.PTP - 원두 붓고 원위치
        self.robot.move_cartesian(self._calculate_point(dripper_point["P2"], dripper_offset, 'y'))
        self.robot.move_cartesian(self._calculate_point(dripper_point["P1"], dripper_offset, 'y'))

        # 사용한 컵 두기
        used_cup_point = conf.place_used_cup_point
        self.robot.move_cartesian(used_cup_point["P1"])
        self.robot.move_linear(cartesian_pose = used_cup_point["P2"])
        self.robot.open_gripper()
        sleep(1)
        self.robot.move_cartesian(cartesian_pose = used_cup_point["P1"])

        return

    def _bloom(self, time: int, amount: int):
        print("Bloom: Pour in {0} grams of hot water, wait {1} seconds".format(str(amount), str(time)))
        # 케틀 잡기
        kettle_point = conf.grab_kettle_point
        self.robot.move_cartesian(kettle_point["P1"])
        self.robot.open_gripper()
        self.robot.move_linear(cartesian_pose = kettle_point["P2"])
        self.robot.close_gripper()
        sleep(1)
        self.robot.move_linear(cartesian_pose = kettle_point["P3"])
        self.robot.move_cartesian(kettle_point["P4"])

        return

    def _pour(self, time: int, amount: int):
        print("Pour: Pour in {0} grams of hot water, wait {1} seconds".format(str(amount), str(time)))
        # self.robot.run_program(conf.brewing_program["recipe1_2"])
        return

    def _wait(self, time:int):
        print("Wait {0} seconds".format(str(time)))

    def _exit(self):
        print("Enjoy you coffee!")
        # 케틀 두기
        kettle_point = conf.grab_kettle_point
        self.robot.move_cartesian(kettle_point["P4"])
        self.robot.move_cartesian(kettle_point["P3"])
        self.robot.move_linear(cartesian_pose = kettle_point["P2"])
        self.robot.open_gripper()
        sleep(1)
        self.robot.move_linear(cartesian_pose = kettle_point["P1"])
        self.robot.move_cartesian(kettle_point["P4"])
        
        home_point = conf.home_point
        self.robot.move_PTP(cartesian_pose = home_point["P"], joint_pose= home_point["J"])
        return

    def set_dripper_location(self, dripper_loc):
        self.dripper_location = dripper_loc

    def set_cup_location(self, cup_loc):
        self.cup_location = cup_loc

    def _calculate_point(self, point, offset, axis):
        cal_point = point.copy()
        if axis == "x":
            axis = 0
        elif axis == "y":
            axis = 1
        elif axis == "z":
            axis = 2
        else:
            return cal_point
        
        cal_point[axis] = cal_point[axis] + offset

        return cal_point


if __name__ == "__main__":
    my_recipe = [["bloom", 0, 0], ["pour", 10, 90]]
    barista = BaristaBasic("192.168.58.2")
    # mode = "Debug"
    mode = "Release"
    if mode == "Debug":
        barista.robot.set_global_speed(40)
        barista.robot.set_speed(10.0)
        # barista.set_cup_location(1)
        barista.set_dripper_location(1)
        # barista._pour(1,1)
        # barista.robot.activate_gripper()
        # sleep(1)
        # barista.robot.close_gripper()
        cup_point = conf.grab_kettle_point
        barista.robot.move_cartesian(cup_point["P1"])
        sleep(1)
        barista.robot.move_linear(cartesian_pose = cup_point["P2"])
        sleep(1)
        barista.robot.move_linear(cartesian_pose = cup_point["P3"])
        sleep(1)
        barista.robot.move_cartesian(cup_point["P4"])
    else: 
        barista.set_cup_location(3)
        barista.set_dripper_location(3)
        barista.make_coffee(my_recipe)