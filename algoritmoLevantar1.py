from PopPyControl.poppy import Poppy
import time

robot = Poppy()
delay = 1
semiDelay = 0.7

for id, motor in robot.motors.items():
    motor.setLED(1)
    motor.update()
    motor.setTorque(1)

for id, motor in robot.motors.items():
    motor.setLED(0)

print('\n'*50)
print('Algoritmo para se Levantar 01')

try:
    # Posicao 01 - Inicial
    print('Posicao 01')
    # Perna Esquerda
    robot.l_hip_x.setPosition(2031)
    robot.l_hip_z.setPosition(2260)
    robot.l_hip_y.setPosition(2371)
    robot.l_knee.setPosition(2047)
    robot.l_ankle.setPosition(2358)
    # Perna Direita
    robot.r_hip_x.setPosition(2010)
    robot.r_hip_z.setPosition(2043)
    robot.r_hip_y.setPosition(1856)
    robot.r_knee.setPosition(2046)
    robot.r_ankle.setPosition(1505)
    # Tronco
    robot.abs_y.setPosition(1896)
    robot.abs_x.setPosition(2058)
    robot.abs_z.setPosition(2049)
    robot.bust_y.setPosition(2224)
    robot.bust_x.setPosition(2057)
    # Cabeca
    robot.head_z.setPosition(521)
    robot.head_y.setPosition(475)
    # Braco Esquerdo
    robot.l_shoulder_y.setPosition(1167)
    robot.l_shoulder_x.setPosition(3227)
    robot.l_arm.setPosition(1798)
    robot.l_elbow.setPosition(1021)
    # Braco Direito
    robot.r_shoulder_y.setPosition(2902)
    robot.r_shoulder_x.setPosition(1056)
    robot.r_arm.setPosition(2046)
    robot.r_elbow.setPosition(2032)
    time.sleep(delay)

    # Posicao 02
    print('Posicao 02')
    # Perna Esquerda
    robot.l_hip_x.setPosition(2150)
    robot.l_hip_z.setPosition(2268)
    robot.l_hip_y.setPosition(2388)
    # Perna Direita
    robot.r_hip_x.setPosition(2110)
    robot.r_hip_z.setPosition(2112)
    robot.r_hip_y.setPosition(1812)
    # Tronco
    robot.abs_y.setPosition(2108)
    robot.abs_x.setPosition(1964)
    robot.abs_z.setPosition(1973)
    robot.bust_y.setPosition(2174)
    robot.bust_x.setPosition(2112)
    # Braco Esquerdo
    robot.l_shoulder_y.setPosition(1554)
    robot.l_shoulder_x.setPosition(3229)
    robot.l_arm.setPosition(1903)
    robot.l_elbow.setPosition(1234)
    # Braco Direito
    robot.r_shoulder_y.setPosition(2371)
    robot.r_shoulder_x.setPosition(1052)
    robot.r_arm.setPosition(2129)
    robot.r_elbow.setPosition(2375)
    time.sleep(delay)

    # Posicao 03
    print('Posicao 03')
    # Braco Esquerdo
    robot.l_shoulder_y.setPosition(1245)
    robot.l_shoulder_x.setPosition(3221)
    robot.l_arm.setPosition(1935)
    robot.l_elbow.setPosition(1024)
    # Braco Direito
    robot.r_shoulder_y.setPosition(2298)
    robot.r_shoulder_x.setPosition(1071)
    robot.r_arm.setPosition(1918)
    robot.r_elbow.setPosition(2550)
    time.sleep(delay)

    # Posicao 04
    print('Posicao 04')
    # Tronco
    robot.abs_z.setPosition(1759)
    # Braco Direito
    robot.r_shoulder_y.setPosition(1326)
    time.sleep(semiDelay)
    robot.r_shoulder_x.setPosition(1059)
    robot.r_arm.setPosition(1980)
    robot.r_elbow.setPosition(3531)

    # Posicao 05
    print('Posicao 05')
    # Perna Esquerda
    robot.l_hip_y.setPosition(2081)
    robot.l_knee.setPosition(1717)
    robot.l_ankle.setPosition(1661)
    # Perna Direita
    robot.r_hip_y.setPosition(2099)
    robot.r_knee.setPosition(1736)
    robot.r_ankle.setPosition(2254)
    # Tronco
    robot.abs_z.setPosition(1756)
    time.sleep(delay)

    # Posicao 06
    print('Posicao 06')
    # Tronco
    robot.abs_z.setPosition(2032)
    # Braco Esquerdo
    robot.l_shoulder_y.setPosition(2645)
    robot.l_shoulder_x.setPosition(3257)
    robot.l_arm.setPosition(1907)
    robot.l_elbow.setPosition(2280)
    # Braco Direito
    robot.r_shoulder_y.setPosition(1140)
    time.sleep(delay)

    # Posicao 07
    print('Posicao 07')
    # Perna Esquerda
    robot.l_knee.setPosition(1622)
    # Perna Direita
    robot.r_knee.setPosition(1646)
    # Braco Direito
    robot.r_shoulder_y.setPosition(1295)
    robot.r_shoulder_x.setPosition(1104)
    robot.r_arm.setPosition(1959)
    robot.r_elbow.setPosition(3418)
    time.sleep(delay)

    # Posicao 08
    print('Posicao 08')
    # Perna Esquerda
    robot.l_knee.setPosition(935)
    robot.l_hip_z.setPosition(2167)
    robot.l_hip_y.setPosition(1106)
    # Perna Direita
    robot.r_knee.setPosition(955)
    robot.r_hip_z.setPosition(2225)
    robot.r_hip_y.setPosition(3097)
    # Braco Esquerdo
    robot.l_shoulder_y.setPosition(2337)
    # Braco Direito
    robot.r_shoulder_y.setPosition(1603)
    time.sleep(delay)
except KeyboardInterrupt:
    print('Algoritmo abortado!')
    robot.clear()
    robot.status()
    robot.close()
    exit()

raw_input("Comecar a engatinhar? Aperte ENTER")

try:
    while True:
        time.sleep(0.5)
        print('\nAlgoritmo para Engatinhar')

        # Posicao 01
        print('Posicao 01')
        # Perna Esquerda
        robot.l_hip_y.setPosition(1512)
        robot.l_knee.setPosition(1288)
        robot.l_ankle.setPosition(2029)
        # Perna Direita
        robot.r_hip_y.setPosition(2724)
        robot.r_knee.setPosition(1260)
        robot.r_ankle.setPosition(2017)
        time.sleep(delay)

        # Posicao 02
        print('Posicao 02')
        # Perna Direita
        robot.r_hip_y.setPosition(2537)
        robot.r_knee.setPosition(1361)
        robot.r_ankle.setPosition(2112)
        # Tronco
        robot.abs_z.setPosition(1885)
        time.sleep(delay)

        # Posicao 03
        print('Posicao 03')
        # Perna Esquerda
        robot.l_hip_y.setPosition(1103)
        robot.l_knee.setPosition(750)
        robot.l_ankle.setPosition(1632)
        time.sleep(delay)

        # Posicao 04
        print('Posicao 04')
        # Perna Direita
        robot.r_knee.setPosition(1424)
        # Tronco
        robot.abs_x.setPosition(1806)
        # Braco Direito
        robot.r_shoulder_y.setPosition(2437)
        robot.r_shoulder_x.setPosition(1067)
        robot.r_arm.setPosition(2041)
        robot.r_elbow.setPosition(2567)
        time.sleep(delay)

        # Posicao 05
        print('Posicao 05')
        # Perna Esquerda
        robot.l_knee.setPosition(918)
        # Perna Direita
        robot.r_hip_x.setPosition(1939)
        robot.r_hip_z.setPosition(2329)
        robot.r_hip_y.setPosition(3148)
        robot.r_knee.setPosition(865)
        robot.r_ankle.setPosition(2382)
        # Tronco
        robot.abs_z.setPosition(2143)
        time.sleep(delay)

        # Posicao 06
        print('Posicao 06')
        """
        # Perna Esquerda
        robot.l_hip_y.setPosition(1423)
        robot.l_knee.setPosition(1288)
        robot.l_ankle.setPosition(2029)
        # Perna Direita
        robot.r_hip_y.setPosition(2783)
        robot.r_knee.setPosition(1260)
        robot.r_ankle.setPosition(2017)
        # Tronco
        robot.abs_x.setPosition(2060)
        robot.abs_z.setPosition(2166)
        """
        # Braco direito
        robot.r_elbow.setPosition(3320)
        robot.r_shoulder_y.setPosition(1660)
        time.sleep(delay)
except KeyboardInterrupt:
    print('Algoritmo abortado!')
    robot.clear()
    robot.status()
    robot.close()
    exit()
