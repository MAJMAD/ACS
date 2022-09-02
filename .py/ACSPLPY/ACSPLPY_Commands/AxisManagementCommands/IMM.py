from ...ACSPLPY_Tools.ACSLowLevel import *

def IMM(axis_motion_parameter, value_or_formula):#need to validate,
    writeToACS("IMM " + str(axis_motion_parameter) + "=" + str(value_or_formula))
    
def infoIMM():
    print("In single axis motion, IMM provides on-the-fly changes of the following motion parameters:\n> VEL (Velocity)\n> ACC (Acceleration)\n> DEC (Deceleration)\n> JERK (Jerk)\nIMM affects the motion in progress and all motions waiting in the corresponding motion queue.\nIn group motion, IMM provides on-the-fly changes for the motion parameters of the leading axis only.")
