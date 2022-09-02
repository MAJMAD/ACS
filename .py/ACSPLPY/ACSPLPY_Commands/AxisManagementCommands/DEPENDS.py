from ...ACSPLPY_Tools.ACSLowLevel import *

def DEPENDS(physical_axis, axis_list,):#need to validate, actual implementation is unclear
    cmd = "DEPENDS " + physical_axis
    if type(axis_list) == int:
        cmd = cmd + "," + str(axis_list)
        writeToACS(cmd)
    else:
        for axis in axis_list:
            cmd = cmd + str(axis) + ","
        cmd = cmd[:-1]
        writeToACS(cmd)
    
def infoDEPENDS():
    print("DEPENDS is used only following CONNECT. DEPENDS specifies a logical dependence between a physical axis (motor) and the same or other logical axes. By default, the physical axis (motor) is assigned to its axis. DEPENDS is necessary because the controller is generally not capable of deriving dependence information from the CONNECT formula.")
