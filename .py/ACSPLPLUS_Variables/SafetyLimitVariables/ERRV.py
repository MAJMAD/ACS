from ACSLowLevel import *

def setERRV(axis, newLimit):#tests well on simulator
    writeToACS(f'ERRV({axis}) = {newLimit}')

def getERRV(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?ERRV')
    else:
        writeToACS(f'?ERRV({axis})')
    status = recvall(1024)
    print(status)
    
def infoERRV():#tests well on simulator
    print('ERRV is a real array, with one element for each axis in the system, and is used for defining the maximum tolerable Position Error (FAULT(axis_index).#PE) when the axis is moving with constant velocity.')