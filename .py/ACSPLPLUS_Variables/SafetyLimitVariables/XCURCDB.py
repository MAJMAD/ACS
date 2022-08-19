from ACSLowLevel import *

def setXCURCDB(axis, newLimit):#tests well on simulator
    writeToACS(f'XCURCDB({axis}) = {newLimit}')

def getXCURCDB(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?XCURCDB')
    else:
        writeToACS(f'?XCURCDB({axis})')
    status = recvall(1024)
    print(status)

def infoXCURCDB():#tests well on simulator
    print('XCURCDB is a real array, the size of which is determined by the total number of axes in the system. It is used for defining the threshold of the current vector peak.')
