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
        value2 = (value - (value%256))/256
        value1 = value%256
        req = header + chr(int(value1)) + chr(int(value2))
        checksum = int(253 - ((0xFF + 0xFF + int(id) + length + 0x03 + int(address) + int(value1) + int(value2))%256))

    port.write(req+chr(checksum))

def setTorque(serialPort, ID, finalState):           #Defines the Torque to a motor
    writeCommand(serialPort, ID, 24, 1, finalState)  #Serial port = legs/torso | ID = Motor ID | finalState -> 0 to deactivate -> 1 to activate
    
def setTorques(serialPort, IDlist, finalState):
    for ID in IDlist:
        setTorque(serialPort, ID, finalState)

def goToPosition(serialPort, ID, goalPosition):
    writeCommand(serialPort, ID, 30, 2, goalPosition)

