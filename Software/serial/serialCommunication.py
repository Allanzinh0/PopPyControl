from serial import Serial
import time

def writeCommand(port, id, address, size, value):
    length = hex(size + 3)
    header = chr(0xFF) + chr(0xFF) + chr(hex(id)) + chr(length) + chr(0x03) + chr(hex(address))
    if size == 1:
        req = header + chr(hex(value))
        checksum = hex(255 - ((0xFF + 0xFF + hex(id) + length + 0x03 + hex(address) + hex(value))%256))
    elif size == 2:
        value1 = value - (value%256)
        value2 = value%256
        req = header + chr(hex(value1)) + chr(hex(value2))
        checksum = hex(255 - ((0xFF + 0xFF + hex(id) + length + 0x03 + hex(address) + hex(value1) + hex(value2))%256))

    port.write(req+chr(checksum))
