from .ACSLowLevel import *

def setXVEL(axis, newLimit):#tests well on simulator
    writeToACS(f'XVEL({axis}) = {newLimit}')

def getXVEL(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?XVEL')
    else:
        writeToACS(f'?XVEL({axis})')
    status = recvall(1024)
    print(status)

def infoXVEL():#tests well on simulator
    print('XVEL is a real array, with one element for each axis in the system, and is used for defining the maximum allowed velocity for the axis.')
