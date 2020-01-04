import sys
sys.path.insert(0, "/serialCommands")

from serialCommands import *
from serial import Serial
import time

legs = Serial('/dev/ttyACM0', 1000000)
torso = Serial('/dev/ttyACM1', 1000000)

setPositionPredefined(legs, torso, 'standing')

legs.close()
torso.close()

