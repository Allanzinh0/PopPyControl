from library.poppy import Poppy

robot = Poppy()
delay = 1

for id, motor in robot.motors.items():
    motor.update()
    motor.setTorque(0)
    motor.setLED(0)
    motor.setTorqueLimit(1023)

print('-'*50)
robot.status()
robot.clear()
robot.close()
