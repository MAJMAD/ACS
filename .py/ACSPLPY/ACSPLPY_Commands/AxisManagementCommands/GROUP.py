from ...ACSPLPY_Tools.ACSLowLevel import *

def GROUP(axis_list):#need to validate
    cmd = "GROUP "
    if type(axis_list) == int:
        cmd = cmd + str(axis_list)
    else:
        cmd = cmd + "("
        for axis in axis_list:
            cmd = cmd + str(axis) + ","
        cmd = cmd[:-1] + ")"
    writeToACS(cmd)

def infoGROUP():
    print("GROUP defines an axis group for coordinate multi-axis motion. The first axis in the axes list is the leading axis. The motion parameters of the leading axis become the default motion parameters for all axes in the group. Motion on all axes in a group will start and conclude at the same time.")