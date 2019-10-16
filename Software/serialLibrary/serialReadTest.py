import sys
sys.path.insert(0, "/serialCommands")

from serialCommands import *
from serial import Serial
import time

def readCommand(serialPort):
    readed = ""
    try:
        h1 = serialPort.read()
        readed = str(hex(h1))
        assert ord(h1) == 255
    except:
        e = 'Timeout on servo ' + str(id)
        raise ValueError('Timeout servo '+ str(id))

    try:
        h2 = serialPort.read()
        readed += "|" + str(hex(h2))
        origin = serialPort.read()
        readed += "|" + str(hex(origin))
        length = ord(serialPort.read()) - 1
        readed += "|" + str(hex(length + 1))
        error = ord(serialPort.read())
        readed += "|" + str(bin(error))

        for i in range(length):
            readed += '|' + str(hex(serialPort.read()))
            print(readed)

        if error != 0:
            e = 'Error from servo ' + str(id) + ' error: ' + str(hex(error))
            raise ValueError('Error ' + str(hex(error)) + ' in servo ' + str(id))
        if error == 0:
            return readed
    except:
        raise ValueError('Critical error!')

port = Serial('/dev/ttyACM0', 1000000)

goToPosition(port, 14, 2000)
port.flush()
print("Comando recebido: " + readCommand(port))

setTorque(port, 14, 0)
port.flush()
print("Comando recebido: " + readCommand(port))

port.close()
