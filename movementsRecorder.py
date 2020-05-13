from PopPyControl.poppy import Poppy
from datetime import datetime

algorythmName = ""
algorythmDelay = 0
algorythmTimestamp = ""
idsList = []

while True:
    try:
        algorythmName = str(input("\nDigite o nome deste novo algoritmo: "))
        algorythmDelay = float(input("Digite o tempo entre cada passo do algoritmo em segundos: "))
        algorythmTimestamp = f"{datetime.timestamp(datetime.now())}".split('.')[0]

        if algorythmName != "" and algorythmDelay > 0:
            break
        else:
            print("Algo foi digitado incorretamente!")
    except ValueError as error:
        print(error)

with open(f"recorders/{algorythmName}-{algorythmTimestamp}_meta.csv", "w") as metaFile:
    metaFile.write("torque,delay,loop,status,type\n")
    metaFile.write(f"True,{algorythmDelay},False,False,3\n")

with open(f"recorders/{algorythmName}-{algorythmTimestamp}_torqueLimit.csv", "w") as torqueLimitFile:
    metaFile.write("motorID,torqueLimit")

with open(f"recorders/{algorythmName}-{algorythmTimestamp}.csv", "w") as algorythmFile:
    try:
        robot = Poppy()

        for id, motor in robot.motors.items():
            idsList.append(id)

        algorythmFile.write(",".join(str(x) for x in idsList))
        algorythmFile.write("\n")

        while True:
            movementsLine = []

            for id in idsList:
                movementsLine.append(robot.motors[id].getPosition())

            algorythmFile.write(",".join(str(x) for x in idsList))
            algorythmFile.write("\n")
    except:
        robot.close()
