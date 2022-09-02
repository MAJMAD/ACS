from ...ACSPLPY_Tools.ACSLowLevel import *

def DISABLE(axis_list, reason=0):#need to validate
    cmd = "DISABLE "
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

def infoDISABLE():
    print("DISABLE deactivates one, several, or using DISABLEALL, all drives. After DISABLE, RPOS = FPOS which means that no position error exists, or PE<axis> = 0.")
