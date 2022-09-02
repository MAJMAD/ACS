from ...ACSPLPY_Tools.ACSLowLevel import *

def GO(axis_list):#need to validate
    cmd = "GO "
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

def infoGO():
    print("GO starts a motion that has been created using the /w (wait) switch.")
