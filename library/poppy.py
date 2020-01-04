from library.motor import Motor
from library.protocol import clearPort
from serial import Serial, SerialException
import json

motorsLegs = []
motorsTorso = []


class Poppy:
    def __init__(self):
        self.motors = {}

        self.serialPortLegs = Serial()
        self.serialPortTorso = Serial()

        with open("data/ports.json") as ports:
            portsData = json.load(ports)
            dataLegs = portsData['legs']
            dataTorso = portsData['torso']
            try:
                self.serialPortLegs.port = dataLegs['port']
                self.serialPortLegs.baudrate = int(dataLegs['baudrate'])
                self.serialPortLegs.timeout = int(dataLegs['timeout'])
                self.serialPortLegs.open()
            except SerialException:
                print('Porta das pernas ja esta sendo usada!')
                print('Programa abortado!')
                self.serialPortLegs.close()
                exit()

            try:
                self.serialPortTorso.port = dataTorso['port']
                self.serialPortTorso.baudrate = int(dataTorso['baudrate'])
                self.serialPortTorso.timeout = int(dataTorso['timeout'])
                self.serialPortTorso.open()
            except SerialException:
                print('Porta do torso ja esta sendo usada!')
                print('Programa abortado!')
                self.serialPortLegs.close()
                self.serialPortTorso.close()
                exit()

        with open("data/motors.json") as motors:
            motorsData = json.load(motors)

            for motorName in motorsData['motors']:
                if motorsData['motors'][motorName]['type'] == 'legs':
                    motorsLegs.append(motorsData['motors'][motorName]['name'])
                if motorsData['motors'][motorName]['type'] == 'torso':
                    motorsTorso.append(motorsData['motors'][motorName]['name'])

        for motor in motorsLegs:
            name = str(motorsData['motors'][motor]['name'])
            limits = {
                'min': motorsData['motors'][motor]['angleLimits']['min'],
                'max': motorsData['motors'][motor]['angleLimits']['max']
            }
            motorObj = Motor(
                _serialPort=self.serialPortLegs,
                _name=name,
                _limits=limits,
                _robot=self,
                motorID=int(motorsData['motors'][motor]['id']),
                typeMotor=str(motorsData['motors'][motor]['type'])
            )

            self.__dict__[name] = motorObj
            self.motors[int(motorsData['motors'][motor]['id'])] = motorObj

            name = ''
            limits = {}

        for motor in motorsTorso:
            name = str(motorsData['motors'][motor]['name'])
            limits = {
                'min': motorsData['motors'][motor]['angleLimits']['min'],
                'max': motorsData['motors'][motor]['angleLimits']['max']
            }
            motorObj = Motor(
                _serialPort=self.serialPortTorso,
                _name=name,
                _limits=limits,
                _robot=self,
                motorID=int(motorsData['motors'][motor]['id']),
                typeMotor=str(motorsData['motors'][motor]['type'])
            )

            self.__dict__[name] = motorObj
            self.motors[int(motorsData['motors'][motor]['id'])] = motorObj

            name = ''
            limits = {}

        print('\n\n')
        for id, motor in self.motors.items():
            print(str(motor))

    def open(self):
        self.serialPortLegs.open()
        self.serialPortTorso.open()

    def close(self):
        self.clear()
        self.serialPortLegs.close()
        self.serialPortTorso.close()

    def status(self):
        for id, motor in self.motors.items():
            print(str(motor))

    def balance(self, motorsID):
        while True:
            test = False

            for id in motorsID:
                load = self.motors[id].getLoad()
                position = self.motors[id].getPosition()

                if position != 0:
                    if 5 < load and load < 1024:
                        test = True
                        self.motors[id].setPosition(position - 2)
                    elif 1029 < load and load < 2048:
                        test = True
                        self.motors[id].setPosition(position + 2)

            if not test:
                break

    def clear(self):
        clearPort(self.serialPortLegs)
        clearPort(self.serialPortTorso)
