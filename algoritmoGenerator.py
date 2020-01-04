import json

motorsValue = {}

with open("data/motors.json") as motors:
    motorsData = json.load(motors)['motors']
    for name, motor in motorsData.items():
        motorsValue[motor['id']] = motor['name']
while True:
    nome = raw_input('Digite o nome do algoritmo: ').capitalize()
    if nome != '':
        break

while True:
    delay = raw_input('Digite o delay entre cada posicao: ')
    if delay != '':
        break

nomeAlgoritmo = 'algoritmo' + nome + '.py'

with open(nomeAlgoritmo, 'w') as algoritmo:
    algoritmo.write("from library.poppy import Poppy\n")
    algoritmo.write("import time\n\n")
    algoritmo.write("robot = Poppy()\n\n")
    algoritmo.write("delay = {}\n\n".format(delay))
    algoritmo.write("for id, motor in robot.motors.items():\n")
    algoritmo.write("    motor.update()\n")
    algoritmo.write("    motor.setTorque(1)\n\n")
    algoritmo.write("print('Algoritmo {}')\n\n".format(nome))
    algoritmo.write("try:\n")

    posicao = 1
    algoritmo.write("    # Posicao {}\n".format(posicao))
    algoritmo.write("    print('Posicao {}')\n".format(posicao))

    while True:
        command = []
        while True:
            command = raw_input(">>>").lower().split(' ')
            if command[0] != '':
                break

        if command[0] == 'exit':
            break
        elif command[0] == 'next':
            algoritmo.write("    time.sleep(delay)\n\n")
            posicao += 1
            algoritmo.write("    # Posicao {}\n".format(posicao))
            algoritmo.write("    print('Posicao {}')\n".format(posicao))
            continue

        elif command[0] == 'delay':
            if command[1].isdigit():
                algoritmo.write("    time.sleep({})\n".format(command[1]))
            else:
                print('Delay invalido!')

        elif command[0] == 'torque':
            try:
                algoritmo.write("    robot.{}.setTorque({})\n".format(
                    motorsValue[int(command[1])],
                    command[2]
                ))
            except KeyError:
                print('ID invalido!')
            except ValueError:
                print('Posicao/ID invalido!')

        elif command[0] == 'torquelimit':
            try:
                if 0 <= int(command[2]) <= 1023:
                    algoritmo.write("    robot.{}.setTorqueLimit({})\n".format(
                        motorsValue[int(command[1])],
                        command[2]
                    ))
                else:
                    print('O TorqueLimit esta fora do alcance!')
            except KeyError:
                print('ID invalido!')
            except ValueError:
                print('TorqueLimit/ID invalido!')

        elif len(command[0]) == 2:
            try:
                if 0 <= int(command[1]) <= 4095:
                    algoritmo.write("    robot.{}.setPosition({})\n".format(
                        motorsValue[int(command[0])],
                        command[1]
                    ))
                else:
                    print('A posicao esta fora do alcance!')
            except KeyError:
                print('ID invalido!')
            except ValueError:
                print('Posicao/ID invalido!')
            except IndexError:
                print('Posicao invalida')

        else:
            print('Comando nao encontrado!')

    algoritmo.write("except KeyboardInterrupt:\n")
    algoritmo.write("    print('Algoritmo abortado!')\n")
    algoritmo.write("    robot.clear()\n")
    algoritmo.write("    robot.status()\n")
    algoritmo.write("    robot.close()\n")
    algoritmo.write("    exit()\n")
    algoritmo.write("\nrobot.status()\n")
    algoritmo.write("robot.close()\n")
