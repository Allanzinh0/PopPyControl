import sys
sys.path.insert(0, "/serialCommands")

from serialCommands import *
from serial import Serial
import time

legs = Serial('/dev/ttyACM0', 1000000)
torso = Serial('/dev/ttyACM1', 1000000)

idsLegs = [11, 12, 13, 14, 15, 21, 22, 23, 24, 25]
idsTorso = [31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 51, 52, 53, 54]

defineAngleLimitsFromJSON(legs, torso)

setTorques(legs, idsLegs, 0)
time.sleep(0.5)
setTorques(torso, idsTorso, 0)
time.sleep(0.5)

legs.close()
torso.close()
