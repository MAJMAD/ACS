from ...ACSPLPY_Tools.ACSLowLevel import *

def SPLIT(axis_list):#need to validate
    cmd = "SPLIT "
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

def infoSPLIT():
    print("SPLIT breaks down a group created using GROUP by designating any axis in the axis list. SPLIT ALL breaks down all groups.")
