from ...ACSPLPY_Tools.ACSLowLevel import *

def BREAK(axis_list):#need to validate
    if type(axis_list) == int:
        writeToACS("BREAK " + str(axis_list))
    else:
        cmd = "BREAK ("
        for axis in axis_list:
            cmd = cmd + str(axis) + ","
        fcmd = cmd[:-1] + ")"
        writeToACS(fcmd)

def infoBREAK():
    print("BREAK immediately terminates the currently executed motion of the specified axis without building a deceleration profile, and initiates the next motion in the axis motion queue, if it exists.")
