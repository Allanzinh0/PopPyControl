import sys
sys.path.insert(0, "/serialCommands")

from serialCommands import *
from serial import Serial
import time

legs = Serial('/dev/ttyACM0', 1000000)
torso = Serial('/dev/ttyACM1', 1000000)

idsLegs = [11, 12, 13, 14, 15, 21, 22, 23, 24, 25]
idsTorso = [31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 51, 52, 53, 54]

startTime = 0.7
executionTime = 1
bufferTime = 0.1

defineAngleLimitsFromJSON(legs, torso)
print('Definido limites de angulos dos motores!')

setTorques(legs, idsLegs, 1)
print('Ativando o travamento dos motores da perna!')
time.sleep(startTime)
setTorques(torso, idsTorso, 1)
print('Ativando o travamento dos motores do torso!')
time.sleep(startTime)

goToPosition(legs, 15, 1752)
print('Colocando o pe esquerdo em posicao!')
time.sleep(startTime)
goToPosition(legs, 25, 2070)
print('Colocando o pe direito em posicao!')
time.sleep(startTime)
goToPosition(legs, 14, 979)
print('Colocando o joelho esquerdo em posicao!')
time.sleep(startTime)
goToPosition(legs, 24, 987)
print('Colocando o joelho direito em posicao!')
time.sleep(startTime)
goToPosition(legs, 13, 1155)
print('Colocando a coxa esquerda em relacao ao Y em posicao!')
time.sleep(startTime)
goToPosition(legs, 23, 3150)
print('Colocando a coxa direita em relacao ao Y em posicao!')
time.sleep(startTime)
goToPosition(legs, 12, 2167)
print('Colocando a coxa esquerda em relacao ao Z em posicao!')
time.sleep(startTime)
goToPosition(legs, 22, 2008)
print('Colocando a coxa direita em relacao ao Z em posicao!')
time.sleep(startTime)
goToPosition(legs, 11, 2135)
print('Colocando a coxa esquerda em relacao ao X em posicao!')
time.sleep(startTime)
goToPosition(legs, 21, 1848)
print('Colocando a coxa direita em relacao ao X em posicao!')
time.sleep(startTime)
goToPosition(torso, 31, 2200)
print('Colocando o abdomen em relacao ao Y em posicao!')
time.sleep(startTime)
goToPosition(torso, 32, 2047)
print('Colocando o abdomen em relacao ao X em posicao!')
time.sleep(startTime)
goToPosition(torso, 33, 2040)
print('Colocando o abdomen em relacao ao Z em posicao!')
time.sleep(startTime)
goToPosition(torso, 34, 1933)
print('Colocando o torax em relacao ao Y em posicao!')
time.sleep(startTime)
goToPosition(torso, 35, 2291)
print('Colocando o torax em relacao ao X em posicao!')
time.sleep(startTime)
goToPosition(torso, 36, 517)
print('Colocando a cabeca em relacao ao Z em posicao!')
time.sleep(startTime)
goToPosition(torso, 41, 2949)
print('Colocando o ombro esquerdo em relacao ao Y em posicao!')
time.sleep(startTime)
goToPosition(torso, 51, 1567)
print('Colocando o ombro direito em relacao ao Y em posicao!')
time.sleep(startTime)
goToPosition(torso, 37, 414)
print('Colocando a cabeca em relacao ao Y em posicao!')
time.sleep(startTime)
goToPosition(torso, 42, 2858)
print('Colocando o ombro esquerdo em relacao ao X em posicao!')
time.sleep(startTime)
goToPosition(torso, 52, 1878)
print('Colocando o ombro direito em relacao ao X em posicao!')
time.sleep(startTime)
goToPosition(torso, 43, 1810)
print('Colocando o braco esquerdo em posicao!')
time.sleep(startTime)
goToPosition(torso, 53, 2551)
print('Colocando o braco direito em posicao!')
time.sleep(startTime)
goToPosition(torso, 44, 1701)
print('Colocando o antebraco esquerdo em posicao!')
time.sleep(startTime)
goToPosition(torso, 54, 3409)
print('Colocando o antebraco direito em posicao!')
time.sleep(startTime)

setTorquesPower(legs, [14,24], 300)
print('Definindo velocidade das pernas!')
time.sleep(startTime)

setTorquePower(torso, 54, 200)
print('Definindo velocidade do antebraco direito!')
time.sleep(startTime)

setTorquePower(torso, 35, 140)
print('Definindo velocidade do torax!')
time.sleep(startTime)

print('\n\n\n\n\n\n' + '-'*50)
print('Executando programacao de Acenar!')

while True:
    goToPosition(torso, 54, 2646)
    time.sleep(bufferTime)
    goToPosition(torso, 35, 2110)
    time.sleep(bufferTime)
    goToPosition(legs, 14, 1250)
    time.sleep(0.01)
    goToPosition(legs, 24, 987)
    print('Ativando posicao 1!')
    time.sleep(executionTime)

    goToPosition(torso, 54, 3409)
    time.sleep(bufferTime)
    goToPosition(torso, 35, 2291)
    time.sleep(bufferTime)
    goToPosition(legs, 14, 979)
    time.sleep(0.01)
    goToPosition(legs, 24, 1250)
    print('Ativando posicao 2!')
    time.sleep(executionTime)

torso.close()
legs.close()
