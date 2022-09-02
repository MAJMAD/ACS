from ...ACSPLPY_Tools.ACSLowLevel import *

def HALT(axis_list, reason=0, switch=None):#need to validate
    cmd = "HALT"
    if switch != None:
        cmd = cmd + "/e"
    cmd = cmd + " "
    if axis_list == "ALL":
        cmd = cmd + str(axis_list)
    elif type(axis_list) == int:
        cmd = cmd + str(axis_list)
    else:
        cmd = cmd + "("
        for axis in axis_list:
            cmd = cmd + str(axis) + ","
        cmd = cmd[:-1] + ")"
    if reason != 0:
        cmd = cmd + ", " + str(reason)
    writeToACS(cmd)

def infoHALT():
    print("In single axis motion, HALT terminates currently executed motion and clears all other motions waiting in the axis motion queue. The deceleration profile is defined by DEC (deceleration variable).\nIn group motion, HALT terminates currently executed motion of all group axes, and clears all other motions waiting in the axes motion queues. The deceleration profile is defined by the DEC (deceleration) variable of the leading axis.")
