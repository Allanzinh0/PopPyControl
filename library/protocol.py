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
    packet = {}
    res = ''
    trys = 0
    value = 0

    while True:
        test = port.read()
        if len(test) != 0:
            res += hex(ord(test)) + ' '
        else:
            trys += 1

            if trys > 3:
                break

    request = ''
    for a in req:
        request += hex(ord(a)) + ' '
    req = request

    req = req.replace('0x', '').split(' ')

    if len(res.split(' ')) < 7:
        packet = {'req': req, 'res': res, 'status': 'Response Null'}
        sleep(delaytime)
        return packet

    res = res.split(' ')

    if res[0] == '0x0':
        del(res[0])

    if res[::-1][1] == '0x0':
        del(res[len(res) - 2])

    if len(res) == 7:
        value = 'Null'

    else:
        for val in res[5:-2][::-1]:
            value *= 256
            value += int(val, 16)

    resStr = []
    for i in range(len(res)):
        resStr.append(res[i].replace('0x', ''))

    response = {
        'received': resStr,
        'id': int(res[2], 16),
        'error': int(res[4], 16),
        'value': value
    }

    packet = {'req': req, 'res': response, 'status': 'OK'}
    sleep(delaytime)
    # print(str(int(res[2], 16)), '-', str(resStr))
    return packet


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
        packet = {'req': req, 'res': res, 'status': 'Tipo Invalido'}
        sleep(delaytime)
        return packet

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
        packet = {'req': req, 'res': res, 'status': 'Tipo Invalido'}
        sleep(delaytime)
        return packet
    elif type(address) != int:
        packet = {'req': req, 'res': res, 'status': 'Tipo Invalido'}
        sleep(delaytime)
        return packet
    elif type(size) != int:
        packet = {'req': req, 'res': res, 'status': 'Tipo Invalido'}
        sleep(delaytime)
        return packet
    elif type(value) != int:
        packet = {'req': req, 'res': res, 'status': 'Tipo Invalido'}
        sleep(delaytime)
        return packet

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
