import sys
sys.path.insert(0, "/serialCommands")

from serialCommands import *
from serial import Serial
import time

legs = Serial('/dev/ttyACM0', 1000000)
torso = Serial('/dev/ttyACM1', 1000000)

idsLegs = [11, 12, 13, 14, 15, 21, 22, 23, 24, 25]
idsTorso = [31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 51, 52, 53, 54]

startTime = 0.5
executionTime = 1
bufferTime = 0.2

defineAngleLimitsFromJSON(legs, torso)

setTorques(legs, idsLegs, 1)
time.sleep(startTime)
setTorques(torso, idsTorso, 1)
time.sleep(startTime)

goToPosition(legs, 15, 1752)
time.sleep(startTime)
goToPosition(legs, 25, 2070)
time.sleep(startTime)
goToPosition(legs, 14, 979)
time.sleep(startTime)
goToPosition(legs, 24, 987)
time.sleep(startTime)
goToPosition(legs, 13, 1155)
time.sleep(startTime)
goToPosition(legs, 23, 3150)
time.sleep(startTime)
goToPosition(legs, 12, 2167)
time.sleep(startTime)
goToPosition(legs, 22, 2008)
time.sleep(startTime)
goToPosition(legs, 11, 2135)
time.sleep(startTime)
goToPosition(legs, 21, 1848)
time.sleep(startTime)
goToPosition(torso, 31, 2200)
time.sleep(startTime)
goToPosition(torso, 32, 2047)
time.sleep(startTime)
goToPosition(torso, 33, 2040)
time.sleep(startTime)
goToPosition(torso, 34, 1933)
time.sleep(startTime)
goToPosition(torso, 35, 2291)
time.sleep(startTime)
goToPosition(torso, 36, 517)
time.sleep(startTime)
goToPosition(torso, 41, 2949)
time.sleep(startTime)
goToPosition(torso, 51, 1567)
time.sleep(startTime)
goToPosition(torso, 37, 414)
time.sleep(startTime)
goToPosition(torso, 42, 2858)
time.sleep(startTime)
goToPosition(torso, 52, 1878)
time.sleep(startTime)
goToPosition(torso, 43, 1810)
time.sleep(startTime)
goToPosition(torso, 53, 2551)
time.sleep(startTime)
goToPosition(torso, 44, 1701)
time.sleep(startTime)
goToPosition(torso, 54, 3409)
time.sleep(startTime)

setTorquesPower(legs, [14,24], 400)
time.sleep(startTime)
setTorquesPower(torso, [35, 54], 200)
time.sleep(startTime)

while True:
    goToPosition(torso, 54, 2646)
    time.sleep(bufferTime)
    goToPosition(torso, 35, 2110)
    time.sleep(bufferTime)
    goToPosition(torso, 14, 1250)
    time.sleep(bufferTime)
    goToPosition(torso, 24, 987)
    time.sleep(executionTime)

    goToPosition(torso, 54, 3409)
    time.sleep(bufferTime)
    goToPosition(torso, 35, 2291)
    time.sleep(bufferTime)
    goToPosition(torso, 14, 979)
    time.sleep(bufferTime)
    goToPosition(torso, 24, 1250)
    time.sleep(executionTime)

torso.close()
legs.close()
