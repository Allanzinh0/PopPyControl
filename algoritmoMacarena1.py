from library.poppy import Poppy
import time

robot = Poppy()
delayStart = 0.5

for id, motor in robot.motors.items():
    motor.setLED(1)
    motor.update()
    motor.setTorqueLimit(1023)
    motor.setTorque(1)

for id, motor in robot.motors.items():
    motor.setLED(0)

print('Algoritmo da macarena - Parte 01')

try:
    # Posicao 01
    print('Posicao 01')
    # Pernas
    robot.l_ankle.setPosition(1733)
    robot.r_ankle.setPosition(2018)
    time.sleep(delayStart)
    robot.l_knee.setPosition(1941)
    robot.r_knee.setPosition(1950)
    time.sleep(delayStart)
    robot.l_hip_y.setPosition(2151)
    robot.r_hip_y.setPosition(2163)
    time.sleep(delayStart)
    robot.l_hip_z.setPosition(2118)
    robot.r_hip_z.setPosition(2117)
    time.sleep(delayStart)
    robot.l_hip_x.setPosition(2100)
    robot.r_hip_x.setPosition(1840)
    time.sleep(delayStart)
    # Tronco
    robot.abs_y.setPosition(2045)
    robot.abs_x.setPosition(2093)
    robot.abs_z.setPosition(2046)
    time.sleep(delayStart)
    robot.bust_y.setPosition(2147)
    robot.bust_x.setPosition(2098)
    time.sleep(delayStart)
    # Cabeca e Bracos
    robot.head_z.setPosition(503)
    robot.l_shoulder_y.setPosition(3088)
    robot.r_shoulder_y.setPosition(1008)
    robot.head_y.setPosition(409)
    time.sleep(delayStart)
    # Bracos
    robot.l_shoulder_x.setPosition(3171)
    robot.r_shoulder_x.setPosition(1034)
    time.sleep(delayStart)
    robot.l_arm.setPosition(1764)
    robot.r_arm.setPosition(2045)
    time.sleep(delayStart)
    robot.l_elbow.setPosition(1224)
    robot.r_elbow.setPosition(2192)
    time.sleep(delayStart)
except KeyboardInterrupt:
    print('Algoritmo Abortado!')
    robot.clear()
    robot.status()
    robot.close()
    exit()

robot.status()
robot.close()
