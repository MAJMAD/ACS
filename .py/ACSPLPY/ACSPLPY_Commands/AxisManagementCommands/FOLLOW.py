from ...ACSPLPY_Tools.ACSLowLevel import *

def FOLLOW(axis):#need to validate
    writeToACS(f'FOLLOW({axis})')

def infoFOLLOW():
    print("FOLLOW switches an axis into slave mode. The specified axis will follow the profile generated by the RTC6.")
