from PopPyControl.packet import Packet
from time import sleep

# Variavel de tempo
delaytime = 0.002


def write(port, req):
    clearPort(port)
    sleep(delaytime)
    port.write(req)
    port.flush()
    sleep(delaytime)


def read(port, req):
    res = ''
    trys = 0

    while True:
        test = port.read()
        if len(test) != 0:
            res += test
        else:
            trys += 1

            if trys > 3:
                break

    sleep(delaytime)
    return Packet(req, res)


def pingCommand(port, id):
    req = ''
    res = ''

    if type(id) != int:
        packet = {'req': req, 'res': res, 'status': 'Tipo Invalido!'}
        sleep(delaytime)
        return packet

    checksum = int(255 - ((int(id) + 0x03) % 256))

    req += chr(int(0xff))
    req += chr(int(0xff))
    req += chr(int(id))
    req += chr(int(0x02))
    req += chr(int(0x01))
    req += chr(checksum)

    write(port, req)
    return read(port, req)


def readCommand(port, id, address, size):
    req = ''
    res = ''

    if type(id) != int or type(address) != int or type(size) != int:
        sleep(delaytime)
        return Packet(req, res)

    checksum = int(255 - ((int(id) + 0x06 + int(address) + int(size)) % 256))

    req += chr(int(0xff))
    req += chr(int(0xff))
    req += chr(int(id))
    req += chr(int(0x04))
    req += chr(int(0x02))
    req += chr(int(address))
    req += chr(int(size))
    req += chr(checksum)

    write(port, req)
    return read(port, req)


def writeCommand(port, id, address, size, value):
    req = ''
    res = ''

    if type(id) != int:
        sleep(delaytime)
        return Packet(req, res)
    elif type(address) != int:
        sleep(delaytime)
        return Packet(req, res)
    elif type(size) != int:
        sleep(delaytime)
        return Packet(req, res)
    elif type(value) != int:
        sleep(delaytime)
        return Packet(req, res)

    value1 = 0
    value2 = 0
    length = size + 3

    req += chr(int(0xff))
    req += chr(int(0xff))
    req += chr(id)
    req += chr(length)
    req += chr(int(0x03))
    req += chr(address)

    if size == 1:
        req += chr(value)
        checksum = 255 - ((id + length + 3 + address + value) % 256)
    elif size == 2:
        value1 = value % 256
        value2 = (value - (value % 256))/256
        req += chr(value1)
        req += chr(value2)
        checksum = 255 - ((id + length + 3 + address + value1 + value2) % 256)

    req += chr(checksum)

    write(port, req)
    return read(port, req)


def clearPort(serialPort):
    while True:
        trash = serialPort.read()
        if trash == '':
            break
