from ...ACSPLPY_Tools.ACSLowLevel import *

def CSDESTROY(axis_list, restoreflag=0):#need to validate, documentation suggests an inconsistency with CSCREATE
    cmd = "CSDESTROY ("
    for axis in axis_list:
        cmd = cmd + str(axis) + ","
    cmd = cmd[:-1] + ")"
    if restoreflag != 0:
        cmd = cmd + ", " + str(restoreflag)
    writeToACS(cmd)
    
def infoCSDESTROY():
    print("The CSDESTROY command cancels the active Local Coordinate System and sets the Machine Coordinate System or previous Local Coordinate System.")
