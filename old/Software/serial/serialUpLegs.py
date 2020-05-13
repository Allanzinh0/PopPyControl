import sys
sys.path.insert(0, "/serialCommunication")

from serialCommunication import *
from serial import Serial

legs = Serial('/dev/ttyACM0', 1000000)
torso = Serial('/dev/ttyACM1', 1000000)

writeCommand(legs, 14, 24, 1, 1)
writeCommand(legs, 24, 24, 1, 1)
print('Torque Ligado!')
time.sleep(2)
writeCommand(legs, 14, 30, 2, 2000)
writeCommand(legs, 24, 30, 2, 2000)
print('Pernas Levantadas!')
time.sleep(2)
writeCommand(legs, 14, 24, 1, 0)
writeCommand(legs, 24, 24, 1, 0)
print('Torque Desligado')

legs.close()
torso.close()
