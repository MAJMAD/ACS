from ...ACSPLPY_Tools.ACSLowLevel import *

def SET(axis_RPOS, value_or_formula):#need to validate, direct setting of FPOS and APOS is suggested by documentation
    writeToACS("SET " + str(axis_RPOS) + "=" + str(value_or_formula))
    
def infoSET():
    print("SET defines the current value of either feedback (FPOS), reference (RPOS), or axis (APOS) position. SET can be initiated when the axis is disabled, or on-the-fly. APOS and FPOS are updated automatically when SET is specified for RPOS, If a non-default CONNECT is used, assign different values to APOS and RPOS.")
