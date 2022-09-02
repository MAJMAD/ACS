from .ACSLowLevel import *

def setSLLIMIT(axis, newLimit):#tests well on simulator
    writeToACS(f'SLLIMIT({axis}) = {newLimit}')

def getSLLIMIT(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?SLLIMIT')
    else:
        writeToACS(f'?SLLIMIT({axis})')
    status = recvall(1024)
    print(status)
    
def infoSLLimit():#tests well on simulator
    print('SLLIMIT is a real array, with one element for each axis in the system, and is used for defining the minimum allowed Left position for the motor')
