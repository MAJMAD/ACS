from .ACSLowLevel import *

def setDELV(axis, newLimit):#tests well on simulator
    writeToACS(f'DELV({axis}) = {newLimit}')

def getDELV(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?DELV')
    else:
        writeToACS(f'?DELV({axis})')
    status = recvall(1024)
    print(status)
    
def infoDELV():#tests well on simulator
    print('DELV is a real array, with one element for each axis in the system, and is used for defining the delay of transition to the Constant Velocity state.')
