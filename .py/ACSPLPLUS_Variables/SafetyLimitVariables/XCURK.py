from ACSLowLevel import *

def setXCURK(axis, newLimit):#tests well on simulator
    writeToACS(f'XCURK({axis}) = {newLimit}')

def getXCURK(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?XCURK')
    else:
        writeToACS(f'?XCURK({axis})')
    status = recvall(1024)
    print(status)

def infoXCURK():#tests well on simulator
    print('XCURK is a double array with one element for each axis in the system. It sets the current limit (in percentage) for the axis to be applied during a KILL MOTION operation.')
