from ...ACSPLPY_Tools.ACSLowLevel import *

def ENCREAD(Axis, E_type, ParamType, Primary=None):#need to validate, dcoumentation suggest an acs buffer is required for this
    cmd = "encread("
    cmd = cmd + str(Axis) + "," + str(E_type) + "," + str(ParamType)
    if Primary != None:
        cmd = cmd + "," + str(Primary) + ")"
    else:
        cmd = cmd + ")"
    writeToACS(cmd)

def infoENCREAD():
    print("The ENCREAD function is used for reading encoder parameters. The function should be executed in a buffer, and it will wait till the execution is completed.")
