from serial import Serial
import json
import time

def writeCommand(port, id, address, size, value): # Simplifies the hexadecimal command
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
#    return readCommand(port, id, address, size)

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

        for i in range(length):
            readed.append(ord(port.read()))
            length -= 1

	    if error != 0:
	        e = 'Error from servo ' + str(id) + ' error: ' + str(hex(error))
	        raise ValueError('Error ' + str(hex(error)) + ' in servo ' + str(id))

        return readed
    except:
	    raise ValueError('Critical error!')
	

def setTorque(serialPort, ID, finalState):           #Defines the Torque to a motor
    writeCommand(serialPort, ID, 24, 1, finalState)  #Serial port = legs/torso | ID = Motor ID | finalState -> 0 to deactivate -> 1 to activate

def setTorquesByName(serialPort, name, finalState):
    writeCommand(serialPort, getIDByMotorName(str(name)), 24, 1, finalState)  #Serial port = legs/torso | ID = Motor ID | finalState -> 0 to deactivate -> 1 to activate

def setTorques(serialPort, IDlist, finalState):
    for ID in IDlist:
        setTorque(serialPort, ID, finalState)

def setTorquePower(serialPort, ID, torquePower):
    writeCommand(serialPort, ID, 34, 2, torquePower)

def setTorquePowerByName(serialPort, name, torquePower):
    writeCommand(serialPort, getIDByMotorName(str(name)), 34, 2, torquePower)

def setTorquesPower(serialPort, IDlist, torquePower):
    for ID in IDlist:
        writeCommand(serialPort, ID, 34, 2, torquePower)

def goToPosition(serialPort, ID, goalPosition):
    with open("data/motors.json") as motors:
        motorObj = getMotorObject(str(getMotorNameByID(int(ID))))

        if goalPosition <= motorObj["angleLimits"]["max"] and goalPosition >= motorObj["angleLimits"]["min"]:
            writeCommand(serialPort, ID, 30, 2, goalPosition)
        else:
            print("Goal position out of bounds for {0}! Code not executed.".format(motorObj["name"]))
            print("Limits for this motor: {0} --> {1}".format(motorObj["angleLimits"]["min"], motorObj["angleLimits"]["max"]))

def goToPositionByMotorName(serialPort, name, goalPosition):
    with open("data/motors.json") as motors:
        motorObj = getMotorObject(str(name))

        if goalPosition <= motorObj["angleLimits"]["max"] and goalPosition >= motorObj["angleLimits"]["min"]:
            writeCommand(serialPort, getIDByMotorName(str(name)), 30, 2, goalPosition)
        else:
            print("Goal position out of bounds for {0}! Code not executed.".format(motorObj["name"]))
            print("Limits for this motor: {0} --> {1}".format(motorObj["angleLimits"]["min"], motorObj["angleLimits"]["max"]))

def getMotorNameByID(ID):
    with open("data/motors.json") as motors:
        motorsData = json.load(motors)
    
    if str(ID) in motorsData["motorsName"]['legs']:
        return motorsData["motorsName"]['legs'][str(ID)]
    elif str(ID) in motorsData["motorsName"]['torso']:
        return motorsData["motorsName"]['torso'][str(ID)]
    else:
        print("Servomotor id not found!")

def getIDByMotorName(name):
    with open("data/motors.json") as motors:
        motorsData = json.load(motors)

        for motor in motorsData["motors"]:
            if motor["name"] == str(name):
                return motor["id"]
        
        print("No motor with that name in JSON file!")
    

def getMotorObject(motorName):
    with open("data/motors.json") as motors:
        motorsData = json.load(motors)

    if motorName in motorsData["motors"]:
        return motorsData["motors"][motorName]

def defineAngleLimitsFromJSON(serialPortLegs, serialPortTorso):
    with open("data/motors.json") as motors:
        motorsData = json.load(motors)
    
    idsLegs = []
    idsTorso = []

    for i in motorsData['motorsName']['legs']:
        idsLegs.append(str(motorsData['motorsName']['legs'][i]))
    for j in motorsData['motorsName']['torso']:
        idsTorso.append(str(motorsData['motorsName']['torso'][j]))

    for motorLegs in idsLegs:
        idMotor = int(motorsData['motors'][motorLegs]['id'])
        angleMin = int(motorsData['motors'][motorLegs]['angleLimits']['min'])
        angleMax = int(motorsData['motors'][motorLegs]['angleLimits']['max'])

        setTorque(serialPortLegs, idMotor, 0)
        print("Torque desativated for motor {}".format(str(motorsData['motors'][motorLegs]['name'])))
        time.sleep(0.1)
        writeCommand(serialPortLegs, idMotor, 6, 2, angleMin)
        print("Angle Limit Min defined for motor {}".format(str(motorsData['motors'][motorLegs]['name'])))
        time.sleep(0.1)
        writeCommand(serialPortLegs, idMotor, 8, 2, angleMax)
        print("Angle Limit Max defined for motor {}".format(str(motorsData['motors'][motorLegs]['name'])))
        time.sleep(0.1)

    for motorTorso in idsTorso:
        idMotor = int(motorsData['motors'][motorTorso]['id'])
        angleMin = int(motorsData['motors'][motorTorso]['angleLimits']['min'])
        angleMax = int(motorsData['motors'][motorTorso]['angleLimits']['max'])

        setTorque(serialPortTorso, idMotor, 0)
        print("Torque desativated for motor {}".format(str(motorsData['motors'][motorTorso]['name'])))
        time.sleep(0.1)
        writeCommand(serialPortTorso, idMotor, 6, 2, angleMin)
        print("Angle Limit Min defined for motor {}".format(str(motorsData['motors'][motorTorso]['name'])))
        time.sleep(0.1)
        writeCommand(serialPortTorso, idMotor, 8, 2, angleMax)
        print("Angle Limit Max defined for motor {}".format(str(motorsData['motors'][motorTorso]['name'])))
        time.sleep(0.1)

def setPositionPredefined(serialPortLegs, serialPortTorso, positionName):
    with open("data/motors.json") as motors:
        motorsData = json.load(motors)

    defineAngleLimitsFromJSON(serialPortLegs, serialPortTorso)

    motorLegs = []
    motorTorso = []

    for i in motorsData['motors']:
        motorLegs.append(str(motorsData['motors'][i]["name"]))
    for j in motorsData['motors']:
        motorTorso.append(str(motorsData['motors'][j]["name"]))

    for legs in motorLegs:
        motor = getMotorObject(legs)

        goToPosition(serialPortLegs, int(motor["id"]), int(motor["prefabPositions"][positionName]))
        time.sleep(0.5)

    for Torso in motorTorso:
        motor = getMotorObject(Torso)

        goToPosition(serialPortTorso, int(motor["id"]), int(motor["prefabPositions"][positionName]))
        time.sleep(0.5)
        
