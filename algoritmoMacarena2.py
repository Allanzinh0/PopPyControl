from PopPyControl.poppy import Poppy
import time

# Variaveis de Tempo
delayStart = 0.5
delay = 2
semiDelay = 0.7

robot = Poppy()

for id, motor in robot.motors.items():
    motor.setLED(1)
    motor.setTorqueLimit(1023)
    motor.setTorque(1)

for id, motor in robot.motors.items():
    motor.setLED(0)

try:
    # Pernas
    robot.l_ankle.setPosition(1733)
    robot.r_ankle.setPosition(2018)
    robot.l_hip_y.setPosition(2151)
    robot.r_hip_y.setPosition(2163)
    time.sleep(delayStart)
    # Tronco
    robot.abs_y.setPosition(2045)
    time.sleep(delayStart)
    # Bracos
    robot.l_arm.setPosition(1764)
    robot.r_arm.setPosition(2045)
    time.sleep(delayStart)
    robot.l_elbow.setPosition(1224)
    robot.r_elbow.setPosition(2192)
    time.sleep(delayStart)
    robot.l_shoulder_y.setPosition(3088)
    robot.r_shoulder_y.setPosition(1008)
    time.sleep(delayStart)
    robot.l_shoulder_x.setPosition(3171)
    robot.r_shoulder_x.setPosition(1034)
    time.sleep(delayStart)
except KeyboardInterrupt:
    print('Algoritmo Abortado!')
    robot.clear()
    robot.status()
    robot.close()
    exit()

for id, motor in robot.motors.items():
    if motor.id in [13, 23, 31, 32]:
        motor.setTorqueLimit(400)
    else:
        motor.setTorqueLimit(512)

print('Algoritmo da macarena - Parte 02')
try:
    # Posicao 01
    print('Posicao 01')
    # Torso
    robot.abs_y.setPosition(2085)
    # Braco Direito
    robot.r_shoulder_y.setPosition(2048)
    robot.r_arm.setPosition(1038)
    robot.r_elbow.setPosition(2060)
    time.sleep(delay)

    # Posicao 02
    print('Posicao 02')
    # Torso
    robot.abs_y.setPosition(2100)
    robot.bust_x.setPosition(2069)
    # Braco Esquerdo
    robot.l_shoulder_y.setPosition(2018)
    robot.l_arm.setPosition(2839)
    robot.l_elbow.setPosition(1063)
    time.sleep(delay)

    # Posicao 03
    print('Posicao 03')
    # Braco Direito
    robot.r_arm.setPosition(3018)
    time.sleep(delay)

    # Posicao 04
    print('Posicao 04')
    # Braco Esquerdo
    robot.l_arm.setPosition(901)
    time.sleep(delay)

    # Posicao 05
    print('Posicao 05')
    # Braco Esquerdo
    robot.l_shoulder_x.setPosition(3120)
    # Braco Direito
    robot.r_arm.setPosition(1084)
    robot.r_shoulder_y.setPosition(1847)
    robot.r_elbow.setPosition(3116)
    time.sleep(delay)

    # Posicao 06
    print('Posicao 06')
    # Braco Esquerdo
    robot.l_shoulder_y.setPosition(1929)
    robot.l_shoulder_x.setPosition(3222)
    robot.l_arm .setPosition(2880)
    robot.l_elbow.setPosition(2066)
    time.sleep(delay)

    # Posicao 07
    print('Posicao 07')
    # Braco Direito - Parte 1
    robot.r_shoulder_x.setPosition(2150)
    robot.r_elbow.setPosition(2060)
    time.sleep(semiDelay)
    # Braco Direito - Parte 2
    robot.r_arm.setPosition(1950)
    robot.r_shoulder_x.setPosition(1187)
    robot.r_elbow.setPosition(3580)
    robot.r_shoulder_y.setPosition(2318)
    time.sleep(delay)

    # Posicao 08
    print('Posicao 08')
    # Braco Esquerdo - Parte 1
    robot.l_shoulder_x.setPosition(3180)
    robot.l_arm.setPosition(1928)
    time.sleep(semiDelay)
    # Braco Esquerdo - Parte 2
    robot.l_shoulder_y.setPosition(1873)
    robot.l_elbow.setPosition(2570)
    time.sleep(delay)

    # Posicao 09
    print('Posicao 09')
    # Braco Direito - Parte 1
    robot.r_shoulder_y.setPosition(1246)
    robot.r_shoulder_x.setPosition(1030)
    time.sleep(semiDelay)
    # Braco Direito - Parte 2
    robot.r_elbow.setPosition(2675)
    robot.r_arm.setPosition(970)
    time.sleep(delay)

    # Posicao 10
    print('Posicao 10')
    # Braco Esquerdo - Parte 1
    robot.l_shoulder_y.setPosition(2777)
    robot.l_shoulder_x.setPosition(3252)
    robot.l_elbow.setPosition(1724)
    time.sleep(semiDelay)
    # Braco Esquerdo - Parte 2
    robot.l_arm.setPosition(2738)
    time.sleep(delay)

    # Posicao 11
    print('Posicao 11')
    # Tronco
    robot.abs_y.setPosition(2045)
    # Braco Direito - Parte 1
    robot.r_shoulder_x.setPosition(1287)
    robot.r_elbow.setPosition(2595)
    robot.r_shoulder_y.setPosition(1133)
    time.sleep(semiDelay)
    # Braco Direito - Parte 2
    robot.r_arm.setPosition(1014)
    robot.r_shoulder_y.setPosition(1008)
    robot.r_shoulder_x.setPosition(1522)
    robot.r_elbow.setPosition(3217)
    time.sleep(delay)

    # Posicao 12
    print('Posicao 12')
    # Braco Esquerdo - Parte 1
    robot.l_shoulder_y.setPosition(3117)
    time.sleep(semiDelay)
    # Braco Esquerdo - Parte 2
    robot.l_shoulder_x.setPosition(2672)
    robot.l_arm.setPosition(2773)
    robot.l_elbow.setPosition(2262)
    time.sleep(delay)
except KeyboardInterrupt:
    print('Algoritmo Abortado!')
    robot.clear()
    robot.status()
    robot.close()
    exit()

robot.status()
robot.close()
