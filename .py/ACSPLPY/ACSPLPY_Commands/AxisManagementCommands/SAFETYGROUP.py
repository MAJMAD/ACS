from ...ACSPLPY_Tools.ACSLowLevel import *

def SAFETYGROUP(axis_list):#need to validate
    cmd = "SAFETYGROUP "
    if type(axis_list) == int:
        cmd = cmd + str(axis_list)
    else:
        cmd = cmd + "("
        for axis in axis_list:
            cmd = cmd + str(axis) + ","
        cmd = cmd[:-1] + ")"
    writeToACS(cmd)

def infoSAFETYGROUP():
    print("SAFETYGROUP activates the fault response for all axes in the axis_list when any axis triggers the fault, and manages the axes as a block in response to KILL/KILLALL and DISABLE/DISABLEALL. To cancel the defined SAFETYGROUP, send the command again with only the first axis as the axis_list")
