from ACSLowLevel import *

def setXRMSD(axis, newLimit):#tests well on simulator
    writeToACS(f'XRMSD({axis}) = {newLimit}')

def getXRMSD(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?XRMSD')
    else:
        writeToACS(f'?XRMSD({axis})')
    status = recvall(1024)
    print(status)

def infoXRMSD():#tests well on simulator aside from some unrecognized characters
    print('XRMSD is a real array, with one element for each axis in the system, and is used for setting the maximum allowable RMS current on the drive, as opposed to XRMSM which sets the maximum allowed RMS current for the motor. XRMSD is defined as a percentage of the maximum peak output. For products that incorporate the Drive Power Electronics (UDMnt, etc…), this value directly limits the Output Current. For products that output Voltage Signals to external Amplifiers (universal analog drive controllers such as the UDI), this value limits the Output Signal to percentage of ±10V.')
