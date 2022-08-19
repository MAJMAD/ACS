from ACSLowLevel import *

def setERRA(axis, newLimit):#tests well on simulator
    writeToACS(f'ERRA({axis}) = {newLimit}')

def getERRA(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?ERRA')
    else:
        writeToACS(f'?ERRA({axis})')
    status = recvall(1024)
    print(status)
    
def infoERRA():#tests well on simulator
    print('ERRA is a real array, with one element for each axis in the system, and is used for defining the Position Error criterion for Acceleration/Deceleration states.')