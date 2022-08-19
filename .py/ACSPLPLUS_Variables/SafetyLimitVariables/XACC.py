from ACSLowLevel import *

def setXACC(axis, newLimit):#tests well on simulator
    writeToACS(f'XACC({axis}) = {newLimit}')

def getXACC(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?XACC')
    else:
        writeToACS(f'?XACC({axis})')
    status = recvall(1024)
    print(status)

def infoXACC():#tests well on simulator
    print('XACC is a real array, with one element for each axis in the system, and is used for defining the maximum allowed acceleration for the motor.')
