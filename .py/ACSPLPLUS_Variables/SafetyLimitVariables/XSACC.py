from ACSLowLevel import *

def setXSACC(axis, newLimit):#tests well on simulator
    writeToACS(f'XSACC({axis}) = {newLimit}')

def getXSACC(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?XSACC')
    else:
        writeToACS(f'?XSACC({axis})')
    status = recvall(1024)
    print(status)

def infoXSACC():#tests well on simulator
    print('XSACC is a real array, with one element for each axis in the system, and is used for defining the maximum allowed slave acceleration in MASTER - SLAVE motion.')
