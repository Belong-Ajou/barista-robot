import frrpc

class RobotController():
    def __init__(self, ip="192.168.58.2") -> None:
        print("Connect robot")
        self.robot = frrpc.RPC(ip)
        self.global_speed = 30
        self.speed = 30
        self.robot.SetSpeed(self.global_speed)

    def set_global_speed(self, speed):
        print("Set global speed:", speed)
        self.global_speed = speed
        self.robot.SetSpeed(speed)

    def set_speed(self, speed):
        print("Set joint speed:", speed)
        self.speed = speed

    def open_gripper(self):
        print("Open gripper")
        self.robot.ActGripper(1, 1)
        self.robot.MoveGripper(1, 100, 40, 50, 10000, 0)

    def close_gripper(self):
        print("Close gripper")
        self.robot.ActGripper(1, 1)
        self.robot.MoveGripper(1, 0, 40, 50, 10000, 0)

    def control_gripper(self, pos, speed=40, force=50, maxtime=10000, block=0):
        print("Control gripper")
        self.robot.ActGripper(1, 1)
        self.robot.MoveGripper(1, pos, speed, force, maxtime, block)

    def move_PTP(self, joint_pose=None, cartesian_pose=None, speed=None):
        print("Move PTP")
        if speed == None:
            speed = self.speed
        eP=[0.000,0.000,0.000,0.000]
        dP=[1.000,1.000,1.000,1.000,1.000,1.000]
        if joint_pose == None:
            pose = self.robot.GetForwardKin(joint_pose)
            cartesian_pose = [pose[1], pose[2], pose[3], pose[4], pose[5], pose[6]]
        if cartesian_pose == None:
            pose = self.robot.GetInverseKin(0,joint_pose,-1)
            joint_pose = [pose[1], pose[2], pose[3], pose[4], pose[5], pose[6]]
        ret = self.robot.MoveJ(joint_pose, cartesian_pose, 0, 0, speed, 100.0, 100.0, eP, -1.0, 0, dP)

    def move_linear(self, joint_pose, cartesian_pose, speed=None):
        print("Move Linear")
        if speed == None:
            speed = self.speed
        eP=[0.000,0.000,0.000,0.000]
        dP=[1.000,1.000,1.000,1.000,1.000,1.000]
        ret = self.robot.MoveL(joint_pose, cartesian_pose, 0, 0, speed, 100.0, 100.0, -1.0, eP, 0, 0, dP)