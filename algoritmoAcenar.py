from PopPyControl.poppy import Poppy
import time

robot = Poppy()

delay = 1

for id, motor in robot.motors.items():
    motor.update()
    motor.setTorque(1)

print('Algoritmo Acenar')

try:
    # Posicao 1
    print('Posicao 1')
    robot.l_ankle.setPosition(1752)
    robot.r_ankle.setPosition(2070)
    time.sleep(delay)
    robot.l_knee.setPosition(979)
    robot.r_knee.setPosition(987)
    time.sleep(delay)
    robot.l_hip_y.setPosition(1155)
    robot.r_hip_y.setPosition(3150)
    time.sleep(delay)
    robot.l_hip_z.setPosition(2167)
    robot.r_hip_z.setPosition(2008)
    time.sleep(delay)
    robot.l_hip_x.setPosition(2135)
    robot.r_hip_x.setPosition(1848)
    time.sleep(delay)
    robot.abs_y.setPosition(2200)
    robot.abs_x.setPosition(2047)
    robot.abs_z.setPosition(2040)
    time.sleep(delay)
    robot.bust_y.setPosition(1933)
    robot.bust_x.setPosition(2291)
    robot.head_z.setPosition(517)
    time.sleep(delay)
    robot.l_shoulder_y.setPosition(2949)
    robot.r_shoulder_y.setPosition(1567)
    robot.head_y.setPosition(414)
    time.sleep(delay)
    robot.l_shoulder_x.setPosition(2858)
    robot.r_shoulder_x.setPosition(1878)
    time.sleep(delay)
    robot.l_arm.setPosition(1810)
    robot.r_arm.setPosition(2551)
    time.sleep(delay)
    robot.l_elbow.setPosition(1701)
    robot.r_elbow.setPosition(3409)
    time.sleep(delay)

    robot.l_knee.setTorqueLimit(300)
    robot.r_knee.setTorqueLimit(300)
    robot.r_elbow.setTorqueLimit(200)
    robot.bust_x.setTorqueLimit(140)

    while True:
        # Posicao 2
        print('Posicao 2')
        robot.r_elbow.setPosition(2646)
        robot.bust_x.setPosition(2110)
        robot.l_knee.setPosition(1250)
        robot.r_knee.setPosition(987)
        time.sleep(delay)

        # Posicao 3
        print('Posicao 3')
        robot.r_elbow.setPosition(3409)
        robot.bust_x.setPosition(2291)
        robot.l_knee.setPosition(979)
        robot.r_knee.setPosition(1250)
except KeyboardInterrupt:
    print('Algoritmo Abortado!')
    robot.clear()
    robot.status()
    robot.close()
    exit()
