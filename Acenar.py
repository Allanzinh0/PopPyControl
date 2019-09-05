from poppy.creatures import PoppyHumanoid
import time

poppy = PoppyHumanoid(simulator = 'vrep')

for motor in poppy.motors:
    motor.complient = False
    
speed = 0.5

poppy.l_shoulder_x.goto_position(90, speed, wait = False)
poppy.l_shoulder_y.goto_position(-90, speed, wait = True)

for i in [0,1,2,3,4,5,6,7,8,9]:
    poppy.l_elbow_y.goto_position(-120, speed, wait = False)
    time.sleep(0.5)
    poppy.l_elbow_y.goto_position(-60, speed, wait = False)
    time.sleep(0.5)

poppy.l_elbow_y.goto_position(0, speed, wait = False)
poppy.l_shoulder_y.goto_position(0,speed, wait = True)
poppy.l_shoulder_x.goto_position(0,speed, wait = True)