import socket, time
from ACSLowLevel import *
#from ACSPLPLUS_Variables.AxisStateVariables import AST
#from ACSPLPLUS_Variables.SafetyLimitVariables import SLLIMIT, SRLIMIT

address = '192.168.0.198' #if running simulator this should be your ip address
port = 701
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)



'''def ACSConnectWithServoLicense():
    #print(dir(soc))
    soc.connect((address, 701)) # ((IP address, port number))
    soc.settimeout(0.25)
    SendGoodServoLicense()

def ReadSystemInfo():
    writeToACS('#SI')
    SI = recvall(1024)
    print((SI))

def SendGoodServoLicense():
    writeToACS('#SDO GPNLGOJJILNEDGLLOMHPPJAJHHACHPJJNKALELMAKGENCJMOGKPMPCOBMKPIEKLJAJFHEEMPAIMOMM')
    ErrorCheck()

def SendBadServoLicense():
    writeToACS('#SDO GPNLGOJDGLLOMHPPJAJHHACHPJJNKALELMAKGENCJMOGKPMPCOBMKPIEKLJAJFHEEMPAIMOMM')
    ReturnCheck()'''

def CheckPosition(axis):
    writeToACS(f'?FPOS({axis})')
    FPOS = recvall(1024)
    print(f'Axis {axis} Position is')
    print(FPOS)

'''# home axis
def Home(axis):
    writeToACS(f'START 8, home{axis}')
    ReturnCheck()
    # writeToACS('disable 0')

# START X-SCAN with Default Values
def XScan():
    writeToACS('START 2, 1')
    soc.close()



'''
if __name__ == '__main__':
    ACSConnect(address, port)
    #getSLLIMIT()

    #print(qAST(0))
    #ReadSystemInfo()
    CheckPosition(0)
    # CheckPosition(1)
    # Home(0)
    # Home(1)
    # CheckPosition(0)
    # CheckPosition(1)
    # time.sleep(5)
    # CheckPosition(0)
    # CheckPosition(1)
    #CheckPosition(0)
    #SendBadServoLicense()
    #SendGoodServoLicense()
