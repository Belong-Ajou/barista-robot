import frrpc
import time

class RobotController():
    def __init__(self, ip="192.168.58.2") -> None:
        print("Connect robot")
        self.robot = frrpc.RPC(ip)
        self.global_speed = 30
        self.speed = 30.0
        self.robot.SetSpeed(self.global_speed)
        self.robot.ResetAllError()

    def set_global_speed(self, speed):
        print("Set global speed:", speed)
        self.global_speed = speed
        self.robot.SetSpeed(speed)

    def set_speed(self, speed):
        print("Set joint speed:", speed)
        self.speed = speed

    def activate_gripper(self):
        print("Activate Gripper")
        self.robot.ActGripper(1,0)
        time.sleep(1)
        self.robot.ActGripper(1, 1)

    def open_gripper(self):
        print("Open gripper")
        self.robot.MoveGripper(1, 100, 40, 50, 10000, 0)

    def close_gripper(self):
        print("Close gripper")
        self.robot.MoveGripper(1, 0, 40, 50, 10000, 0)

    def control_gripper(self, pos, speed=40, force=50, maxtime=10000, block=0):
        print("Control gripper")
        self.robot.MoveGripper(1, pos, speed, force, maxtime, block)

    def move_PTP(self, joint_pose=None, cartesian_pose=None, speed=None):
        print("Move PTP")
        if speed == None:
            speed = self.speed
        eP=[0.000,0.000,0.000,0.000]
        dP=[1.000,1.000,1.000,1.000,1.000,1.000]
        if cartesian_pose == None:
            pose = self.robot.GetForwardKin(joint_pose)
            cartesian_pose = [pose[1], pose[2], pose[3], pose[4], pose[5], pose[6]]
        if joint_pose == None:
            pose = self.robot.GetInverseKin(0,cartesian_pose,-1)
            joint_pose = [pose[1], pose[2], pose[3], pose[4], pose[5], pose[6]]
        ret = self.robot.MoveJ(joint_pose, cartesian_pose, 0, 0, speed, 100.0, 100.0, eP, -1.0, 0, dP)

    def move_linear(self, joint_pose=None, cartesian_pose=None, speed=None):
        print("Move Linear")
        if speed == None:
            speed = self.speed
        eP=[0.000,0.000,0.000,0.000]
        dP=[1.000,1.000,1.000,1.000,1.000,1.000]
        if cartesian_pose == None:
            pose = self.robot.GetForwardKin(joint_pose)
            cartesian_pose = [pose[1], pose[2], pose[3], pose[4], pose[5], pose[6]]
        if joint_pose == None:
            pose = self.robot.GetInverseKin(0,cartesian_pose,-1)
            joint_pose = [pose[1], pose[2], pose[3], pose[4], pose[5], pose[6]]
        ret = self.robot.MoveL(joint_pose, cartesian_pose, 0, 0, speed, 100.0, 100.0, -1.0, eP, 0, 0, dP)

    def move_cartesian(self, cartesian_pose, speed=None):
        print("Move by Cartesian")
        if speed == None:
            speed = self.speed
        self.robot.MoveCart(cartesian_pose,0,0,speed,100.0,100.0,-1.0,-1)
        # time.sleep(10)
    
    def run_program(self, program):
        print(f'run program: /fruser/{program}.lua')
        time.sleep(1)
        self.robot.Mode(0)
        ret = self.robot.ProgramLoad(f'/fruser/{program}.lua')
        self.robot.ProgramRun()
        cnt = 0
        while True:
            state = self.robot.GetProgramState()[1]
            if state == 1: cnt += 1
            elif state == 2: cnt = 0
            if cnt == 2: break
            time.sleep(0.5)
            # print(f"state:{state}")
        time.sleep(0.5)