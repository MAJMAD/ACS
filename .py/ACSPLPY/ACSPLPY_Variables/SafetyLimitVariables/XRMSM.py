from .ACSLowLevel import *

def setXRMSM(axis, newLimit):#tests well on simulator
    writeToACS(f'XRMSM({axis}) = {newLimit}')

def getXRMSM(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?XRMSM')
    else:
        writeToACS(f'?XRMSM({axis})')
    status = recvall(1024)
    print(status)

def infoXRMSM():#tests well on simulator aside from some unrecognized characters
    print('XRMSM is a real array, with one element for each axis in the system, and is used for setting the maximum allowable RMS current on the motor, as opposed to XRMSD which sets the maximum allowed RMS current for the drive. XRMSM is defined as a percentage of the maximum peak output. For products that incorporate the Drive Power Electronics (UDMnt, etc…), this value directly limits the Output Current. For products that output Voltage Signals to external Amplifiers (universal analog drive controllers such as the UDI), this value limits the Output Signal to percentage of ±10V')
