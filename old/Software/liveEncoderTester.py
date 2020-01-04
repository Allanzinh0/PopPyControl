import time
from pypot.creatures import PoppyHumanoid
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def motorPosition(ID):
    for motor in poppy.motors:
        if ID == int(motor.id):
            return int(motor.present_position)   

while 1:
    simulationCheck = raw_input('\n\nDeseja realizar uma simulacao v-rep[s] ou testes no humanoide[t]? (s/t)\n\n')

    if simulationCheck == 's':
        poppy = PoppyHumanoid(simulator = 'vrep')
        break
    elif simulationCheck == 't':
        poppy = PoppyHumanoid()
        break
    else:
        print('\nResposta invalida!\n')
    clear()

IDs = []

for motor in poppy.motors:
    IDs.append(motor.id)

print(IDs)    

while 1:

    print('-'*47)
    for motor in poppy.motors:
        print('| {:<13}   id: {:<2}    initialPos:{:>7} |'.format(str(motor.name), str(motor.id), str(motor.present_position)))
    print('-'*47)

    motorId = raw_input('\nInsira aqui o ID do motor que deseja acompanhar: ')

    if int(motorId) in IDs:
        while 1:
            testTime = input('\nPor quantos segundos deseja realizar a verificacao em tempo real? ')
            if int(testTime) > 0:
                break
            else:
                print('Valor invalido!')     
        initialize = time.time()
        timeRemaining = True

        while timeRemaining:
            print(motorPosition(int(motorId)))
            liveTimer = time.time() - initialize
            if liveTimer == int(testTime):
                timeRemaining = False
            time.sleep(0.35)
        
        print('Teste finalizado!\n')


    else:
        print('ID invalido . . .')
        time.sleep(1.5)
            

        
