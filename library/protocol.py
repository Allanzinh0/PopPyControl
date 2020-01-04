from time import sleep

# Variavel de tempo
delaytime = 10 / (10 ** 6)


def pingCommand(port, id):
    req = ''
    res = ''

    if type(id) != int:
        packet = {'req': req, 'res': res, 'status': 'Tipo Invalido!'}
        return packet

    checksum = int(255 - ((int(id) + 0x03) % 256))

    req += chr(int(0xff))
    req += chr(int(0xff))
    req += chr(int(id))
    req += chr(int(0x02))
    req += chr(int(0x01))
    req += chr(checksum)

    port.write(req)
    sleep(delaytime)

    request = ''
    for a in req:
        request += hex(ord(a)) + ' '
    req = request

    while True:
        test = port.read()
        if test != '':
            res += hex(ord(test)) + ' '
        else:
            break
    
    req = req.replace('0x', '').split(' ')

    if len(res.split(' ')) < 7:
        packet = {'req': req, 'res': res, 'status': 'Response Null'}
        return packet

    response = {
        'received': res.replace('0x', '').split(' '),
        'id': int(res.split(' ')[2], 16),
        'error': int(res.split(' ')[4], 16),
        'value': 'Null'
    }

    packet = {'req': req, 'res': response, 'status': 'OK'}
    return packet


def readCommand(port, id, address, size):
    req = ''
    res = ''
    value = 0

    if type(id) != int:
        packet = {'req': req, 'res': res, 'status': 'Tipo Invalido'}
        return packet
    elif type(address) != int:
        packet = {'req': req, 'res': res, 'status': 'Tipo Invalido'}
        return packet
    elif type(size) != int:
        packet = {'req': req, 'res': res, 'status': 'Tipo Invalido'}
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
    
    port.write(req)
    sleep(delaytime)

    request = ''
    for a in req:
        request += hex(ord(a)) + ' '
    req = request

    while True:
        test = port.read()
        if test != '':
            res += hex(ord(test)) + ' '
        else:
            break

    req = req.replace('0x', '').split(' ')

    if len(res.split(' ')) < 7:
        packet = {'req': req, 'res': res, 'status': 'Response Null'}
        return packet
    
    elif len(res.split(' ')) == 7:
        value = -1

    else:
        for val in res.split(' ')[5:-2][::-1]:
            value *= 256
            value += int(val, 16)

    response = {
        'received': res.replace('0x', '').split(' '),
        'id': int(res.split(' ')[2], 16),
        'error': int(res.split(' ')[4], 16),
        'value': value
    }

    packet = {'req': req, 'res': response, 'status': 'OK'}
    return packet


def writeCommand(port, id, address, size, value):
    req = ''
    res = ''

    if type(id) != int:
        packet = {'req': req, 'res': res, 'status': 'Tipo Invalido'}
        return packet
    elif type(address) != int:
        packet = {'req': req, 'res': res, 'status': 'Tipo Invalido'}
        return packet
    elif type(size) != int:
        packet = {'req': req, 'res': res, 'status': 'Tipo Invalido'}
        return packet
    elif type(value) != int:
        packet = {'req': req, 'res': res, 'status': 'Tipo Invalido'}
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

    port.write(req)
    sleep(delaytime)

    request = ''
    for a in req:
        request += hex(ord(a)) + ' '
    req = request

    while True:
        test = port.read()
        if test != '':
            res += hex(ord(test)) + ' '
        else:
            break

    req = req.replace('0x', '').split(' ')

    if len(res.split(' ')) < 7:
        packet = {'req': req, 'res': res, 'status': 'Response Null'}
        return packet

    response = {
        'received': res.replace('0x', '').split(' '),
        'id': int(res.split(' ')[2], 16),
        'error': int(res.split(' ')[4], 16),
        'value': 'Null'
    }

    packet = {'req': req, 'res': response, 'status': 'OK'}
    return packet


def clearPort(serialPort):
    while True:
        trash = serialPort.read()
        if trash == '':
            break
