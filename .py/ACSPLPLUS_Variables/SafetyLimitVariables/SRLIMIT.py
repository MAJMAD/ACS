from ACSLowLevel import *

def setSRLIMIT(axis, newLimit):#tests well on simulator
    writeToACS(f'SRLIMIT({axis}) = {newLimit}')

def getSRLIMIT(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?SRLIMIT')
    else:
        writeToACS(f'?SRLIMIT({axis})')
    status = recvall(1024)
    print(status)

def infoSRLIMIT():#tests well on simulator
    print('SRLIMIT is a real array, with one element for each axis in the system, and is used for defining the minimum allowed Right position for the motor')
