from ...ACSPLPY_Tools.ACSLowLevel import *

def COMMUT(axis, excitation_current=98, settletime=500, slope=-1, gantry_commut_delay=500):#need to validate
    cmd = "COMMUT " + str(axis) + "," + str(excitation_current) + "," + str(settletime)
    if slope != -1:
        cmd = cmd + "," + str(slope)
        if gantry_commut_delay != 500:
            cmd = cmd + "," + str(gantry_commut_delay)
    writeToACS(cmd)

def infoCOMMUT():
    print("COMMUT performs auto commutation and may be used when the following conditions hold true:\n> The motor is DC brushless (AC servo)\n> The motor is enabled\n> The motor is idle\n> The axis is already configured and properly tuned")
