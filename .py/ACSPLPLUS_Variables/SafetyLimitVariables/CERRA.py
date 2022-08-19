from ACSLowLevel import *

def setCERRA(axis, newLimit):#tests well on simulator
    writeToACS(f'CERRA({axis}) = {newLimit}')

def getCERRA(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?CERRA')
    else:
        writeToACS(f'?CERRA({axis})')
    status = recvall(1024)
    print(status)
    
def infoCERRA():#tests well on simulator
    print('CERRA is a real array, with one element for each axis in the system, and is used for defining the Position Error criterion for acceleration/deceleration states.')
