from .ACSLowLevel import *

def setXRMSTD(axis, newLimit):#tests well on simulator
    writeToACS(f'XRMSTD({axis}) = {newLimit}')

def getXRMSTD(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?XRMSTD')
    else:
        writeToACS(f'?XRMSTD({axis})')
    status = recvall(1024)
    print(status)

def infoXRMSTD():#tests well on simulator
    print('XRMSTD is a real array, with one element for each axis in the system, and is used for setting the time constant in milliseconds for XRMSD to activate the overcurrent protection for the drive. For calculation of XRMSD activation time, see SPiiPlus Setup Guide .')
