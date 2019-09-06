import time

from poppy.creatures import PoppyHumanoid
from os import system, name

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

    idMotor = input('Digite o id do motor desejado: ')
    choice = raw_input('Deseja mover, verificar o encoder ou acessar o historico? (m|v|h): ')

    if choice == 'v':
        if idMotor in IDs:
            for motor in poppy.motors:
                if idMotor == int(motor.id):
                    print("Posicao atual: {0}".format(motor.present_position))
                    if str(motor.name) in hist:
                        if hist[str(motor.name)] == 'Movido':
                            hist[str(motor.name)] = 'Movido e Verificado'
                    else:
                        hist[str(motor.name)] = 'Verificado'
        else:
            print('O ID fornecido nao esta registrado.')
            time.sleep(2)

    if choice == 'm':
        if idMotor in IDs:
            angle = input('Digite o angulo desejado: ')
            if angle <= 359 and angle >= -359:
                for motor in poppy.motors:
                    if idMotor == int(motor.id):
                        motor.goto_position(angle, 0.5, wait = True)
                        if str(motor.name) in hist:
                            if hist[str(motor.name)] == 'Verificado':
                                hist[str(motor.name)] = 'Movido e Verificado'
                        else:
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
        time.sleep(5)
    time.sleep(1)
    clear()
