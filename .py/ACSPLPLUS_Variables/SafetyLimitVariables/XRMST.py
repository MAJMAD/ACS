from ACSLowLevel import *
#issue in documentation moreso than a bug it seems
#actually might be a bug accidentally left a getXRMST() line when testing XRMSTM saw the 59999 and 60000 values???
def setXRMST(axis, newLimit):#issues with setting values around upper 3260 limit, seems like the real upper limit is 3230
    writeToACS(f'XRMST({axis}) = {newLimit}')

def getXRMST(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?XRMST')
    else:
        writeToACS(f'?XRMST({axis})')
    status = recvall(1024)
    print(status)

def infoXRMST():#tests well on simulator
    print('XRMST is a real array, with one element for each axis in the system, and is used for setting the time constant in milliseconds for the XRMS to activate the overcurrent protection. For calculation of XRMS activation time, see SPiiPlus Setup Guide .')
