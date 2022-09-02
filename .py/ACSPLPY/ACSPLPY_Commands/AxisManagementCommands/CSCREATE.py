from ...ACSPLPY_Tools.ACSLowLevel import *

def CSCREATE(axis_list, x_trans, y_trans, z_trans=None, switch=None, rot_axis=None, rot_angle=None):#need to validate,
    cmd = "CSREATE"
    if switch != None:
        cmd = cmd + "/r"
    cmd = cmd + " ("
    for axis in axis_list:
        cmd = cmd + str(axis) + ","
    cmd = cmd[:-1] + ")"
    cmd = cmd + ", " + str(x_trans) + ", " + str(y_trans)
    if z_trans != None:
        cmd = cmd + ", " + str(z_trans)
    if rot_axis != None and rot_angle != None:
        cmd = cmd + ", " + str(rot_axis) + ", " + str(rot_angle)
    writeToACS(cmd)

def infoCSCREATE():
    print("The CSCREATE command creates the new Local Coordinate System (LCS) relative to the Machine Coordinate System or the previous LCS, depending on the applied switches.")
