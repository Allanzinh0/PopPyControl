import time, datetime

from pypot.creatures import PoppyHumanoid
from os import system, name

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
    


def findMotor(ID):
    for motor in poppy.motors:
        if ID == int(motor.id):
            return str(motor.name)

def defineComplients(state, ID=None):
    if ID == None:
        for motor in poppy.motors:
            motor.complient = state
    else:
        currentMotor = findMotor(ID)
        getattr(poppy, currentMotor).complient = state

def motorPosition(ID):
    for motor in poppy.motors:
        if ID == int(motor.id):
            return int(motor.present_position)

defineComplients(False)

for motor in poppy.motors:
    motor.complient = False

# Criando uma lista com todos os ID's
IDs = []

for motor in poppy.motors:
    IDs.append(motor.id)

# Criando a lista do historico

hist = {}

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()

while True:
    print('-'*47)
    for motor in poppy.motors:
        print('| {:<13}   id: {:<2}    initialPos:{:>6} |'.format(str(motor.name), str(motor.id), str(motor.present_position)))
    print('-'*47)

    choice = str(raw_input('Deseja mover, verificar o encoder, acessar o historico, analisar posicoes ou salvar os testes realizados? (m|v|h|a|s): '))

    if choice == 'v':

        idMotor = input('\nDigite o id do motor a ser verificado: ')

        if idMotor in IDs:
            for motor in poppy.motors:
                if idMotor == int(motor.id):
                    print("\nPosicao atual: {0}".format(motor.present_position))
                    if str(motor.name) in hist and hist[str(motor.name)] == 'Movido':
                        hist[str(motor.name)] = 'Movido e Verificado'
                    elif not str(motor.name) in hist:
                        hist[str(motor.name)] = 'Verificado'
        else:
            print('\nO ID fornecido nao esta registrado.')
        
        final = raw_input('\nPressione [ENTER] para continuar. . .')

    elif choice == 'm':

        idMotor = input('\nDigite o id do motor a ser movido: ')

        if idMotor in IDs:
            angle = input('\nDigite o angulo desejado: ')
            if angle <= 359 and angle >= -359:
                for motor in poppy.motors:
                    if idMotor == int(motor.id):
                        motor.goto_position(angle, 0.5, wait = True)
                        if str(motor.name) in hist and hist[str(motor.name)] == 'Verificado':
                            hist[str(motor.name)] = 'Movido e Verificado'
                        elif not str(motor.name) in hist:
                            hist[str(motor.name)] = 'Movido'
            else:
                print('\nO angulo fornecido e invalido.')
    
                final = raw_input('\nPressione [ENTER] para continuar. . .')

        else:
            print('\n\nO ID fornecido nao esta registrado.')
            
            final = raw_input('\nPressione [ENTER] para continuar. . .')


    elif choice == 'h':
        print('')
        print('-'*42)
        for motor, action in hist.items():
            print('| {:<13} foi {:<20} |'.format(str(motor), str(action)))
        print('-'*42)
        final = raw_input('\nPressione [ENTER] para continuar. . .')

    elif choice == 'a':
        idMotor = input('\nDigite o id do motor a ser analisado: ')

        if idMotor in IDs:
            currentMotor = findMotor(idMotor)
            defineComplients(True, idMotor)
            print('\nComplient ligado!')
            time.sleep(2)
            readyCheck = raw_input('\nPressione [ENTER] para desligar o complient de {0}.\n'.format(currentMotor))
            defineComplients(False, idMotor)
            print('O motor em questao ({0}) esta na posicao: {1} graus.'.format(currentMotor, motorPosition(idMotor)))
            finalCheck = raw_input('\n\nPressione [ENTER] para continuar . . .')
        else:
            print('\nO ID fornecido nao esta registrado.')
            time.sleep(2)            
    elif choice == 's':
        now = datetime.datetime.now()
        today = now.strftime('%x')
    
        fileName = raw_input('\nQual vai ser o nome do arquivo? (insira o mesmo nome do anterior caso ja tenha criado um)\n\n')
        
        register = open(str('../Data/motorTester/' + fileName + '.txt'), 'w+')
        register.write(today)
        
        for motor, action in hist.items():
            register.write('\n{0} foi {1}'.format(str(motor), str(action)))
        
        register.close()
    
    else:
        print('\nOpcao invalida! Reiniciando o programa . . .')
        time.sleep(3)

    clear()