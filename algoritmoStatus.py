from PopPyControl.poppy import Poppy
import time

robot = Poppy()

for id, motor in robot.motors.items():
    motor.setLED(1)

time.sleep(1)

for id, motor in robot.motors.items():
    motor.setLED(0)

robot.clear()
robot.close()
