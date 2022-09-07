from ...ACSPLPY_Tools.ACSLowLevel import *

def OUTP(channel, array=None, start_index=None, number=None):#need to validate
    cmd = "OUTP(" + str(channel)
    if array != None:
        cmd = cmd + "," + str(array)
        if start_index != None:
            cmd = cmd + "," + str(start_index)
            if number != None:
                cmd = cmd + "," + str(number)
    cmd = cmd + ")"
    writeToACS(cmd)

def infoINP():
    print("OUTP sends data values from an integer array to a specified channel. This function is useful to create an interface between the controller and special input devices such as a track-ball, mouse and various sensors. OUTP is also used when the controller acts as a master with the MODBUS protocol communication.\nBefore using OUTP, configure the relevant communication channel as a special communication channel using SETCONF function, key 302.\nEach ASCII character is represented by its numerical value and is stored in a separate element of the array.\nThe user might have to define communication parameters for the special communication channel\nwith SETCONF function keys 302, 303, 304, 309.\nSee also INP.")
