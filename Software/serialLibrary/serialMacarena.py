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
bufferTime = 0.01

defineAngleLimitsFromJSON(legs, torso)
print('Definido limites de angulos dos motores!')

setTorques(legs, idsLegs, 1)
time.sleep(startTime)
setTorques(torso, idsTorso, 1)
time.sleep(startTime)

goToPosition(legs, 15, 1808)
time.sleep(startTime)
goToPosition(legs, 25, 1993)
time.sleep(startTime)
goToPosition(legs, 14, 1941)
time.sleep(startTime)
goToPosition(legs, 24, 1950)
time.sleep(startTime)
goToPosition(legs, 13, 2111)
time.sleep(startTime)
goToPosition(legs, 23, 2193)
time.sleep(startTime)
goToPosition(legs, 12, 2118)
time.sleep(startTime)
goToPosition(legs, 22, 2117)
time.sleep(startTime)
goToPosition(legs, 11, 2100)
time.sleep(startTime)
goToPosition(legs, 21, 1840)
time.sleep(startTime)
goToPosition(torso, 31, 1943)
time.sleep(startTime)
goToPosition(torso, 32, 2093)
time.sleep(startTime)
goToPosition(torso, 33, 2046)
time.sleep(startTime)
goToPosition(torso, 34, 2140)
time.sleep(startTime)
goToPosition(torso, 35, 2098)
time.sleep(startTime)
goToPosition(torso, 36, 503)
time.sleep(startTime)
goToPosition(torso, 41, 3088)
time.sleep(startTime)
goToPosition(torso, 51, 1008)
time.sleep(startTime)
goToPosition(torso, 37, 409)
time.sleep(startTime)
goToPosition(torso, 42, 3225)
time.sleep(startTime)
goToPosition(torso, 52, 1034)
time.sleep(startTime)
goToPosition(torso, 43, 1764)
time.sleep(startTime)
goToPosition(torso, 53, 2045)
time.sleep(startTime)
goToPosition(torso, 44, 1227)
time.sleep(startTime)
goToPosition(torso, 54, 2192)
time.sleep(startTime)

setTorquesPower(legs, [11, 12, 14, 15, 21, 22, 24, 25], 512)
setTorquesPower(torso, [33, 34, 35, 36, 37, 41, 42, 43, 44, 51, 52, 53, 54], 512)
print('Definindo velocidade dos motores MX-28AT!')
time.sleep(startTime)

setTorquesPower(legs, [13, 23], 400)
setTorquesPower(torso, [31, 32], 400)
print('Definindo velocidade dos motores MX-64AT!')
time.sleep(startTime)

print('\n\n\n\n\n\n' + '-'*50)
print('Executando programacao da Macarena em...')
time.sleep(1.5)
print('3...')
time.sleep(1.5)
print('2...')
time.sleep(1.5)
print('1...')
time.sleep(1.5)
print('0\n\n\n')

# Posicao 01
print('\nAtivando posicao 1!')
goToPosition(torso, 51, 2048)
time.sleep(bufferTime)
goToPosition(torso, 53, 1038)
time.sleep(bufferTime)
goToPosition(torso, 54, 2060)
time.sleep(executionTime)

# Posicao 02
print('\nAtivando posicao 2!')
goToPosition(torso, 31, 2062)
time.sleep(bufferTime)
goToPosition(torso, 35, 2069)
time.sleep(bufferTime)
goToPosition(torso, 41, 2018)
time.sleep(bufferTime)
goToPosition(torso, 43, 2839)
time.sleep(bufferTime)
goToPosition(torso, 44, 1063)
time.sleep(executionTime)

# Posicao 03
print('\nAtivando posicao 3!')
goToPosition(torso, 53, 3018)
time.sleep(executionTime)

# Posicao 04
print('\nAtivando posicao 4!')
goToPosition(torso, 43, 901)
time.sleep(executionTime)

# Posicao 05
print('\nAtivando posicao 5!')
goToPosition(torso, 42, 3120)
time.sleep(bufferTime)
goToPosition(torso, 53, 1084)
time.sleep(bufferTime)
goToPosition(torso, 51, 1847)
time.sleep(bufferTime)
goToPosition(torso, 54, 3116)
time.sleep(executionTime)

# Posicao 06
print('\nAtivando posicao 6!')
goToPosition(torso, 41, 1929)
time.sleep(bufferTime)
goToPosition(torso, 42, 3222)
time.sleep(bufferTime)
goToPosition(torso, 43, 2880)
time.sleep(bufferTime)
goToPosition(torso, 44, 2066)
time.sleep(executionTime)

# Posicao 07
print('\nAtivando posicao 7!')
goToPosition(torso, 52, 1293)
time.sleep(bufferTime)
goToPosition(torso, 54, 2812)
time.sleep(executionTime/4)
goToPosition(torso, 51, 2318)
time.sleep(bufferTime)
goToPosition(torso, 52, 1187)
time.sleep(bufferTime)
goToPosition(torso, 53, 1888)
time.sleep(bufferTime)
goToPosition(torso, 54, 3580)
time.sleep(executionTime)

# Posicao 08
print('\nAtivando posicao 8!')
goToPosition(torso, 41, 1873)
time.sleep(bufferTime)
goToPosition(torso, 42, 3180)
time.sleep(bufferTime)
goToPosition(torso, 43, 2000)
time.sleep(bufferTime)
goToPosition(torso, 44, 2582)
time.sleep(executionTime)

torso.close()
legs.close()
