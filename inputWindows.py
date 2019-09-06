import time

from poppy.creatures import PoppyHumanoid
from os import system

poppy = PoppyHumanoid(simulator = 'vrep')

for motor in poppy.motors:
    motor.complient = False

system('cls')

while True:
    print('-'*24)
    for motor in poppy.motors:
        print('| {:<13} id: {:<2} |'.format(str(motor.name), str(motor.id)))
    
    print('-'*24)
    idMotor = input('Digite o id do motor desejado: ')
    choice = raw_input('Deseja mover ou ver o angulo? (m|v): ')

    for motor in poppy.motors:
        if str(choice) == 'v':
            if str(motor.id) == str(idMotor):
                print("Posicao atual: " + str(motor.present_position))

        if str(choice) == 'm':
            if str(motor.id) == str(idMotor):
                angulo = input('Digite o angulo desejado: ')
                motor.goto_position(angulo, 0.5, wait = True)
    
    time.sleep(1)
    system('cls')
