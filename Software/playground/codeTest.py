import time

from poppy.creatures import PoppyHumanoid
from os import system, name

poppy = PoppyHumanoid(simulator = 'vrep')

def findMotorIndex(ID):
    for index, motor in enumerate(poppy.motors):
        if ID == int(motor.id):
            return index

# 42 l_shoulder_y

print(poppy.motors[findMotorIndex(42)].name)