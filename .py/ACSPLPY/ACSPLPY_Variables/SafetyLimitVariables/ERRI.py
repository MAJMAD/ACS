from .ACSLowLevel import *

def setERRI(axis, newLimit):#tests well on simulator
    writeToACS(f'ERRI({axis}) = {newLimit}')

def getERRI(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?ERRI')
    else:
        writeToACS(f'?ERRI({axis})')
    status = recvall(1024)
    print(status)
    
def infoERRI():#tests well on simulator
    print('ERRI is a real array, with one element for each axis in the system, and is used for defining the maximum tolerable Position Error (FAULT(axis_index).#PE) when the motor is idle.')