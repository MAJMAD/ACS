from ...ACSPLPY_Tools.ACSLowLevel import *

def INP(channel, array=None, start_index=None, number=None, timeout=None):#need to validate
    cmd = "INP(" + str(channel)
    if array != None:
        cmd = cmd + "," + str(array)
        if start_index != None:
            cmd = cmd + "," + str(start_index)
            if number != None:
                cmd = cmd + "," + str(number)
                if timeout != None:
                    cmd = cmd + str(timeout)
    cmd = cmd + ")"
    writeToACS(cmd)

def infoINP():
    print("INP reads data values from a specified channel and stores them to an integer array. This function is useful for creating an interface between the controller and special input devices such as a track-ball, mouse or various sensors. INP is also used when the controller acts as a master with the MODBUS protocol communication.\nBefore using INP, configure the relevant communication channel as a special communication channel using SETCONF function, key 302.\nSee also OUTP.")
