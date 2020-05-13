from PopPyControl.poppy import Poppy
import time


def readAlgorithm(robot, algorithmName):
    try:
        algorithmMetaFile = open(f"algorithms/{algorithmName}_meta.csv")
        algorithmMetaFile.readline()
        algorithmMeta = algorithmMetaFile.readline().replace('\n', '').split(',')
        algorithmMetaFile.close()

        torque = eval(algorithmMeta[0])
        delay = int(algorithmMeta[1])
        isLoop = eval(algorithmMeta[2])
        status = eval(algorithmMeta[3])
        algorithmType = int(algorithmMeta[4])
    except ValueError:
        print("Algo deu errado na leitura dos metadados do algoritmo.")
        return
    except FileNotFoundError:
        print(f"O algoritmo {algorithmName} nao existe.")

    print("-" * 36)
    print(f"Torque inicial definido como: {torque}")
    print(f"Tempo entre passos definido como: {delay}")
    print(f"Algoritmo definido como ciclo infinito: {isLoop}")
    print(f"Algoritmo mostrara um log das acoes: {status}")
    print(f"Tipo de algoritmo definido: {algorithmType}")
    print("-" * 36)

    torqueLimitsFile = open(f"algorithms/{algorithmName}_torqueLimit.csv")
    torqueLimitsFile.readline()
    while True:
        line = torqueLimitsFile.readline().replace('\n', '').split(',')
        if line == ['']:
            break
        motorID = line[0]
        torquelimit = line[1]
        if status:
            print(f"Definindo torque {torquelimit} para o motor {motorID}")
    torqueLimitsFile.close()

    try:
        while True:
            time.sleep(delay)
            algorithm = open(f"algorithms/{algorithmName}.csv")
            algorithm.readline()
            prevStep = 0
            step = 0
            while True:
                line = algorithm.readline().replace('\n', '').split(',')
                if line == ['']:
                    break
                if algorithmType == 1:
                    step = int(line[0])
                    motorID = int(line[1])
                    angle = int(line[2])
                    if prevStep != step:
                        time.sleep(delay * (step - prevStep))
                        prevStep = step

                    print(f"Passo {step} movendo {motorID} para {angle}")
                elif algorithmType == 2:
                    motorID = int(line[0])
                    angle = int(line[1])
                    delay = int(line[2])

                    print(f"Passo {step} movendo {motorID} para {angle}")
                    time.sleep(delay)
                    step += 1
            algorithm.close()
            if not isLoop:
                break
    except KeyboardInterrupt:
        print("\nAlgoritmo Abortado.")


if __name__ == "__main__":
    robot = Poppy()

    while True:
        try:
            algorithmName = str(input("Digite o algoritmo desejado: "))
        except KeyboardInterrupt:
            # robot.close()
            print('\n')
            break

        readAlgorithm("robot", algorithmName)
