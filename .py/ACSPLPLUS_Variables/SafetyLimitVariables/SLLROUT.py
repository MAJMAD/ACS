from ACSLowLevel import *
#found a bug, SLLROUT will allow invalid values
#ACS documentation also seems to have typos and refers to SLLROUT as SLPROUT
SLLROUTARGUEMENTS = {
    '0':'According to SLLROUT',
    '001':'From channel 0',
    '101':'From channel 1',
    '201':'From channel 2',
    '301':'From channel 3'
}

def setSLLROUT(axis, newLimit):#tests well on simulator
    writeToACS(f'SLLROUT({axis}) = {newLimit}')

def getSLLROUT(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?SLLROUT')
    else:
        writeToACS(f'?SLLROUT({axis})')
    status = recvall(1024)
    print(status)
    
def infoSLLROUT():#tests well on simulator
    print('SLLROUT is an integer array, with one element for each axis in the system, and is used for setting the HW limits routing for the specified axis.')

def infoSLLROUTARGUEMENTS(ARGUEMENT =''):#tests well on simulator
    if ARGUEMENT == '':
        print(SLLROUTARGUEMENTS)
    else:
        print(SLLROUTARGUEMENTS[ARGUEMENT])