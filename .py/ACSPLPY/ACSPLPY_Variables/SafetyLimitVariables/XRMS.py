from .ACSLowLevel import *

def setXRMS(axis, newLimit):#tests well on simulator
    writeToACS(f'XRMS({axis}) = {newLimit}')

def getXRMS(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?XRMS')
    else:
        writeToACS(f'?XRMS({axis})')
    status = recvall(1024)
    print(status)

def infoXRMS():#tests well on simulator aside from some unrecognized characters
    print('XRMS is a real array, with one element for each axis in the system, and is used for setting the maximum allowable rms current for the motor. XRMS is defined as a percentage of the maximum peak output. For products that incorporate the Drive Power Electronics (UDMnt, etc…), this value directly limits the Output Current. For products that output Voltage Signals to external Amplifiers (universal analog drive controllers such as the UDI), this value limits the Output Signal to percentage of ±10V')
