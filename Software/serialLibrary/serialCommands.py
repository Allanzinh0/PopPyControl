from serial import Serial
import time

def writeCommand(port, id, address, size, value): #Simplifies the hexadecimal command
    value1 = 0
    value2 = 0
    
    length = int(size + 3)
    header = chr(int(0xFF)) + chr(int(0xFF)) + chr(int(id)) + chr(length) + chr(int(0x03)) + chr(int(address))
    
    if size == 1:
        req = header + chr(int(value))
        checksum = int(253 - ((0xFF + 0xFF + int(id) + length + 0x03 + int(address) + int(value))%256))
    elif size == 2:
        value1 = value%256
        value2 = (value - (value%256))/256
        req = header + chr(int(value1)) + chr(int(value2))
        checksum = int(253 - ((0xFF + 0xFF + int(id) + length + 0x03 + int(address) + int(value1) + int(value2))%256))

    port.write(req+chr(checksum))
    return readCommand(port, id, address, size)

def readCommand(port, id, address, size):
    readed = list()
    try:
        h1 = port.read()
	assert ord(h1) == 255
    except:
	e = 'Timeout on servo ' + str(id)
        raise ValueError('Timeout servo '+ str(id))
    
    try:
        h2 = port.read()
        origin = port.read()
        length = ord(port.read()) - 1
        error = ord(port.read())

	while length > 0:
            readed.append(ord(port.read()))
            length -= 1

	if error != 0:
	    e = 'Error from servo ' + str(id) + ' error: ' + str(hex(error))
	    raise ValueError('Error ' + str(hex(error)) + ' in servo ' + str(id)

        return readed

    except Exception, detail:
	raise ValueError(detail)
	

def setTorque(serialPort, ID, finalState):           #Defines the Torque to a motor
    writeCommand(serialPort, ID, 24, 1, finalState)  #Serial port = legs/torso | ID = Motor ID | finalState -> 0 to deactivate -> 1 to activate
    
def setTorques(serialPort, IDlist, finalState):
    for ID in IDlist:
        setTorque(serialPort, ID, finalState)

def goToPosition(serialPort, ID, goalPosition):
    writeCommand(serialPort, ID, 30, 2, goalPosition)

