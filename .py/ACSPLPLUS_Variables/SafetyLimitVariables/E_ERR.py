from ACSLowLevel import *

E_ERRCODES = {
    '5121':'CRC Error: Result of CRC check of the received value',
    '5122':'BUSY: Indicates that encoder is busy - specifics depend on encoder brand',
    '5123':'Encoder Not Ready: The status register is not completely updated. Not All checks have been performed. Data transmission is not yet completed.',
    '5124':'TIMEOUT',
    '5125':'FPGA File not found: FPGA file is missing, therefore, the Absolute Encoder for the required axis cannot be operated.',
    '5126':'Error Flag: Error',
    '5127':'Encoder Error: An internal incompatibility was detected. Full system upgrade is required.',
    '5128':'Encoder Error: Watchdog'
}

def getE_ERR(axis = ''):#tests well on simulator
    if axis == '':
        writeToACS('?E_ERR')
    else:
        writeToACS(f'?E_ERR({axis})')
    status = recvall(1024)
    print(status)
    
def infoE_ERR():#tests well on simulator
    print('E_ERR is an integer array for each axis. It contains the encoder error code that was identified during the encoder initialization process. The encoder errors range from 5121 to 5126 and are latched in the E_ERR variable. The error codes are can be specified by calling getE_ERRCODES()')

def infoE_ERRCODES(errorcode =''):#tests well on simulator
    if errorcode == '':
        print(E_ERRCODES)
    else:
        print(E_ERRCODES[errorcode])
