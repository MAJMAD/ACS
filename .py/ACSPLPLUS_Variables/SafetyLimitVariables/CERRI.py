from ACSLowLevel import *

def setCERRI(axis, newLimit):#tests well on simulator
    writeToACS(f'CERRI({axis}) = {newLimit}')

def getCERRI(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?CERRI')
    else:
        writeToACS(f'?CERRI({axis})')
    status = recvall(1024)
    print(status)
    
def infoCERRI():#tests well on simulator
    print('CERRI is a real array, with one element for each axis in the system, and is used for defining the critical Position Error when the motor is idle.')
