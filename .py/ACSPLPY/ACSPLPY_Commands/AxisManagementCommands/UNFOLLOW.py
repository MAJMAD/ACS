from ...ACSPLPY_Tools.ACSLowLevel import *

def UNFOLLOW(axis):#need to validate
    writeToACS(f'UNFOLLOW({axis})')

def infoUNFOLLOW():
    print("UNFOLLOW switches an axis into regular mode. The specified axis will follow the profile generated by the ACS controller.")
