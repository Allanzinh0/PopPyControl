import time

from poppy.creatures import PoppyHumanoid
from os import system, name

poppy = PoppyHumanoid(simulator = 'vrep')

# def findMotorName(ID):
#     for motor in poppy.motors:
#         if ID == int(motor.id):
#             return str(motor.name)
            
# def findMotorObject(ID):
#     for motor in poppy.motors:
#         if ID == int(motor.id):
#             return motor

# def defineComplients(state, ID=None):
#     if ID == None:
#         for motor in poppy.motors:
#             motor.complient = state
#     else:
#         currentMotor = findMotorObject(ID)
#         poppy.motors.currentMotor.complient = state
    

# defineComplients(False)

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
    print('-'*24)
    for motor in poppy.motors:
        print('| {:<13} id: {:<2} |'.format(str(motor.name), str(motor.id)))
    print('-'*24)

    choice = raw_input('Deseja mover, verificar o encoder, acessar o historico ou analisar posicoes? (m|v|h|a): ')

    if choice == 'v':

        idMotor = input('Digite o id do motor a ser verificado: ')

        if idMotor in IDs:
            for motor in poppy.motors:
                if idMotor == int(motor.id):
                    print("Posicao atual: {0}".format(motor.present_position))
                    if str(motor.name) in hist and hist[str(motor.name)] == 'Movido':
                        hist[str(motor.name)] = 'Movido e Verificado'
                    elif not str(motor.name) in hist:
                        hist[str(motor.name)] = 'Verificado'
        else:
            print('O ID fornecido nao esta registrado.')
            time.sleep(2)
        
        final = raw_input('Pressione [ENTER] para continuar. . .')

    if choice == 'm':

        idMotor = input('Digite o id do motor a ser movido: ')

        if idMotor in IDs:
            angle = input('Digite o angulo desejado: ')
            if angle <= 359 and angle >= -359:
                for motor in poppy.motors:
                    if idMotor == int(motor.id):
                        motor.goto_position(angle, 0.5, wait = True)
                        if str(motor.name) in hist and hist[str(motor.name)] == 'Verificado':
                            hist[str(motor.name)] = 'Movido e Verificado'
                        elif not str(motor.name) in hist:
                            hist[str(motor.name)] = 'Movido'
            else:
                print('\n\nO angulo fornecido e invalido.')
        else:
            print('\n\nO ID fornecido nao esta registrado.')
            time.sleep(2)

    if choice == 'h':
        print('-'*42)
        for motor, action in hist.items():
            print('| {:<13} foi {:<20} |'.format(str(motor), str(action)))
        print('-'*42)
        final = raw_input('Pressione [ENTER] para continuar. . .')

    if choice == 'a':
        idMotor = input('Digite o id do motor a ser analisado: ')

        if idMotor in IDs:
            # currentMotor = findMotorName(idMotor)
            # currentMotorObject = findMotorObject(idMotor)
            currentMotor = ''
            currentPosition = 0
            for motor in poppy.motors:
                if int(motor.id) == idMotor:
                    motor.complient = True
                    currentMotor = motor.name
                    
            print('\nComplient ligado!')
            time.sleep(2)
            readyCheck = raw_input('\nPressione [ENTER] para desligar o complient de {0}.\n'.format(currentMotor))
            for motor in poppy.motors:
                if int(motor.id) == idMotor:
                    motor.complient = False
                    currentPosition = motor.present_position
            print('O motor em questao ({0}) esta na posicao: {1} graus.'.format(currentMotor, currentPosition))
            finalCheck = raw_input('\n\nPressione [ENTER] para continuar . . .')

    clear()