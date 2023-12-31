import frrpc
import time

class robotController:
    def __init__(self, config):
        ip = config['ip']

        print(f'connect to {ip}')
        self.robot = frrpc.RPC(ip)

        self.robot.Mode(0)
        self.robot.SetSpeed(30)

        self.robot.ResetAllError()

    def run_program(self, program):
        print(f'run program: /fruser/{program}.lua')
        ret = self.robot.ProgramLoad(f'/fruser/{program}.lua')
        self.robot.ProgramRun()
        cnt = 0
        while True:
            state = self.robot.GetProgramState()[1]
            if state == 1: cnt += 1
            elif state == 2: cnt = 0
            if cnt == 2: break
            time.sleep(0.5)

if __name__ == "__main__":
    robot = robotController({"ip":"192.168.58.2"})
    robot.run_program('Tetsu')