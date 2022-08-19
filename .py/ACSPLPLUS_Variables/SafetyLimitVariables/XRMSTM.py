from ACSLowLevel import *

def setXRMSTM(axis, newLimit):#tests well on simulator
    writeToACS(f'XRMSTM({axis}) = {newLimit}')

def getXRMSTM(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?XRMSTM')
    else:
        writeToACS(f'?XRMSTM({axis})')
    status = recvall(1024)
    print(status)

def infoXRMSTM():#tests well on simulator
    print('XRMSTM is a real array, with one element for each axis in the system, and is used for setting the time constant in milliseconds for XRMSM to activate the overcurrent protection for the motor. For calculation of XRMSM activation time, see SPiiPlus Setup Guide.')
