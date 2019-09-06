import time

from poppy.creatures import PoppyHumanoid
from os import system

poppy = PoppyHumanoid(simulator = 'vrep')

for motor in poppy.motors:
    motor.complient = False

# Criando uma lista com todos os ID's
IDs = []

for motor in poppy.motors:
    IDs.append(motor.id)

# Criando a lista do historico

hist = {}

def clear():
    if __name__ == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()

while True:
    print('-'*24)
    for motor in poppy.motors:
        print('| {:<13} id: {:<2} |'.format(str(motor.name), str(motor.id)))
    print('-'*24)

    idMotor = input('Digite o id do motor desejado: ')
    choice = raw_input('Deseja mover, verificar o encoder ou acessar o historico? (m|v|h): ')

    if choice == v:
        if idMotor in IDs:
            for motor in poppy.motors:
                if idMotor == int(motor.id):
                    print("Posicao atual: {0}".format(motor.present_position))
                    if hist[motor.name] == 'Movido':
                        hist[motor.name] = 'Movido e Verificado'
                    elif not motor.name in hist:
                        hist[motor.name] = 'Verificado'
        else:
            print('O ID fornecido nao esta registrado.')
            time.sleep(2)

    if choice == 'm':
        if idMotor in IDs:
            angle = input('Digite o angulo desejado: ')

            for motor in poppy.motors:
                if idMotor == int(motor.id) and angle <= 359 and angle >= -359:
                    motor.goto_position(angle, 0.5, wait = True)
                    if hist[motor.name] == 'Verificado':
                        hist[motor.name] = 'Movido e Verificado'
                    elif not motor.name in hist:
                        hist[motor.name] = 'Movido'
                else:
                    print('\n\nO angulo fornecido e invalido.')
        else:
            print('\n\nO ID fornecido nao esta registrado.')
            time.sleep(2)

    if choice == 'h':
        print('-'*51)
        for motor, action in hist.items():
            print('| {:<13} de ID {:<2} foi {:<20} |'.format(str(motor), str(poppy.motor.id), str(action)))
        print('-'*51)
    time.sleep(1)
    clear()
