from ...ACSPLPY_Tools.ACSLowLevel import *

def FCLEAR(axis_list):#need to validate
    cmd = "FCLEAR "
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

def infoFCLEAR():
    print("FCLEAR clears the FAULT variable and the results of the previous fault stored in MERR")
