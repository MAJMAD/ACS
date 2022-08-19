from ACSLowLevel import *

def setDELI(axis, newLimit):#tests well on simulator
    writeToACS(f'DELI({axis}) = {newLimit}')

def getDELI(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?DELI')
    else:
        writeToACS(f'?DELI({axis})')
    status = recvall(1024)
    print(status)
    
def infoDELI():#tests well on simulator
    print('DELI is a real array, with one element for each axis in the system, and is used for defining the delay of transition to the Idle state.')
