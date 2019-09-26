import sys
sys.path.insert(0, "/serialCommunication")

from serialCommunication import *
from serial import Serial
import time

legs = Serial('/dev/ttyACM0', 1000000)
# torso = Serial('/dev/ttyACM1', 1000000)

idsLegs = [11, 12, 13, 14, 15, 21, 22, 23, 24, 25]
idsTorso = [31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 51, 52, 53, 54]

setTorques(legs, idsLegs, 1)
# setTorques(torso, idsTorso, 1)

goToPosition(legs, 15, 1752)
goToPosition(legs, 25, 2070)
time.sleep(0.1)

goToPosition(legs, 14, 979)
goToPosition(legs, 24, 987)
time.sleep(0.1)

goToPosition(legs, 13, 1155)
goToPosition(legs, 23, 3150)
time.sleep(0.1)

goToPosition(legs, 12, 2167)
goToPosition(legs, 22, 2008)
time.sleep(0.1)

goToPosition(legs, 11, 2135)
goToPosition(legs, 21, 1848)
time.sleep(0.1)
