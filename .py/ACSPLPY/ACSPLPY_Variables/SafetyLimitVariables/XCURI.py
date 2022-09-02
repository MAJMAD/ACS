from .ACSLowLevel import *
#for brake applications make this 100% right?
def setXCURI(axis, newLimit):#tests well on simulator
    writeToACS(f'XCURI({axis}) = {newLimit}')

def getXCURI(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?XCURI')
    else:
        writeToACS(f'?XCURI({axis})')
    status = recvall(1024)
    print(status)

def infoXCURI():#tests well on simulator aside from some unrecognized characters 
    print('XCURI is a real array, with one element for each axis in the system, and is used for limiting the drive output when the motor is enabled but in standstill position. XCURI is defined as a percentage of the maximum peak output. For products that incorporate the Drive Power Electronics (UDMnt, etc…), this value directly limits the Output Current. For products that output Voltage Signals to external Amplifiers (universal analog drive controllers such as the UDI), this value limits the Output Signal to percentage of ±10V.')
