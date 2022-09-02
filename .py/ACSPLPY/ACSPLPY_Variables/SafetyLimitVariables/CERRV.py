from .ACSLowLevel import *

def setCERRV(axis, newLimit):#tests well on simulator
    writeToACS(f'CERRV({axis}) = {newLimit}')

def getCERRV(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?CERRV')
    else:
        writeToACS(f'?CERRV({axis})')
    status = recvall(1024)
    print(status)
    
def infoCERRV():#tests well on simulator
    print('CERRV is a real array, with one element for each axis in the system, and is used for defining the critical Position Error when the motor is moving with constant velocity.')
