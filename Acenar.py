from poppy.creatures import PoppyHumanoid
import time

poppy = PoppyHumanoid(simulator = 'vrep')

for motor in poppy.motors:
    motor.complient = false
    
speed = 1

poppy.
