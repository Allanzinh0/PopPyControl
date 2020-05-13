from pypot.creatures import PoppyHumanoid
import time

poppy = PoppyHumanoid(simulator = 'vrep')

for motor in poppy.motors:
    motor.complient = True