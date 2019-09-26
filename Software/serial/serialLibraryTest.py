import sys
sys.path.insert(0, "/serialCommunication")

from serialCommunication import *
from serial import Serial
import time

torso = Serial('/dev/ttyACM1', 1000000)

setTorque(torso, 54, 1)

for i in range(5):
	goToPosition(torso, 54, 3409)
	time.sleep(1.5)
	goToPosition(torso, 54, 2646)
	time.sleep(1.5)

torso.close()
