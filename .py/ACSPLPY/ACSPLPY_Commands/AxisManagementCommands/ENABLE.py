from ...ACSPLPY_Tools.ACSLowLevel import *

def ENABLE(axis_list):#need to validate
    cmd = "ENABLE "
    if axis_list == "ALL":
        cmd = cmd + str(axis_list)
    elif type(axis_list) == int:
        cmd = cmd + str(axis_list)
    else:
        cmd = cmd + "("
        for axis in axis_list:
            cmd = cmd + str(axis) + ","
        cmd = cmd[:-1] + ")"
    writeToACS(cmd)

def infoENABLE():
    print("ENABLE activates one or more axes. After ENABLE, the motor starts following the reference position (RPOS) and axis faults are enabled. ENABLE ALL activates all axes.")
