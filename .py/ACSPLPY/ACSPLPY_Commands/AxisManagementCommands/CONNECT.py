from ...ACSPLPY_Tools.ACSLowLevel import *

def CONNECT(formula):#need to validate,
    writeToACS(f'CONNECT ' + str(formula))
    
def infoCONNECT():
    print("CONNECT defines a formula for calculating reference position (RPOS). This formula can include any other axes variables. DEPENDS must follow CONNECT")
