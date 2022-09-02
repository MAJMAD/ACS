from ...ACSPLPY_Tools.ACSLowLevel import *

def KILL(axis_list, reason=0, switch=None):#need to validate
    cmd = "KILL"
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

def infoKILL():
    print("Use KILL after a safety event to decelerate and stop an axis faster than during normal deceleration and stop. KILLALL stops all axes.\nIn single axis motion, KILL terminates currently executed motion and clears all other motions waiting in the axis motion queue. The deceleration profile uses a second-order deceleration profile and the KDEC (kill deceleration) value.\nIn group motion, KILL terminates currently executed motion only for the specified axes, and clears all other motions waiting in the axis/axes motion queue.The deceleration profile uses a secondorder deceleration profile and the KDEC (kill deceleration) variable of each axis.")
