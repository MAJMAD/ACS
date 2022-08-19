import socket, time
from ACSLowLevel import *
from SLLIMIT import *
from SRLIMIT import *
from CERRA import *
from CERRI import *
from CERRV import *
from DELV import *
from DELI import *
from E_ERR import *
from ERRA import *
from ERRI import *
from ERRV import *
from SLLROUT import*


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

'''def CheckPosition(axis):
    writeToACS(f'?FPOS({axis})')
    FPOS = recvall(1024)
    print(f'Axis {axis} Position is')
    print(FPOS)'''

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
    #CERRA TESTS
    '''infoCERRA()
    getCERRA()
    getCERRA(1)
    getCERRA(0)
    setCERRA(0, 1)
    setCERRA(1, 2)
    setCERRA(2, 3)
    getCERRA()
    getCERRA(1)
    getCERRA(0)'''
    #CERRI TESTS
    '''infoCERRI()
    getCERRI()
    getCERRI(1)
    getCERRI(0)
    setCERRI(0, 1)
    setCERRI(1, 2)
    setCERRI(2, 3)
    getCERRI()
    getCERRI(1)
    getCERRI(0)'''
    #CERRV TESTS
    '''infoCERRV()
    getCERRV()
    getCERRV(1)
    getCERRV(0)
    setCERRV(0, 1)
    setCERRV(1, 2)
    setCERRV(2, 3)
    getCERRV()
    getCERRV(1)
    getCERRV(0)'''
    #DELV TESTS
    '''infoDELV()
    getDELV()
    getDELV(1)
    getDELV(0)
    setDELV(0, 1)
    setDELV(1, 2)
    setDELV(2, 3)
    getDELV()
    getDELV(1)
    getDELV(0)'''
    #DELI TESTS
    '''infoDELI()
    getDELI()
    getDELI(1)
    getDELI(0)
    setDELI(0, 1)
    setDELI(1, 2)
    setDELI(2, 3)
    getDELI()
    getDELI(1)
    getDELI(0)'''
    #E_ERR TESTS
    '''infoE_ERR()
    getE_ERR()
    getE_ERR(1)
    getE_ERR(0)
    infoE_ERRCODES()
    infoE_ERRCODES('5121')
    infoE_ERRCODES('5122')
    infoE_ERRCODES('5123')
    infoE_ERRCODES('5124')
    infoE_ERRCODES('5125')
    infoE_ERRCODES('5126')
    infoE_ERRCODES('5127')
    infoE_ERRCODES('5128')'''
    #ERRA TESTS
    '''infoERRA()
    getERRA()
    getERRA(1)
    getERRA(0)
    setERRA(0, 1)
    setERRA(1, 2)
    setERRA(2, 3)
    getERRA()
    getERRA(1)
    getERRA(0)'''
    #ERRI TESTS
    '''infoERRI()
    getERRI()
    getERRI(1)
    getERRI(0)
    setERRI(0, 1)
    setERRI(1, 2)
    setERRI(2, 3)
    getERRI()
    getERRI(1)
    getERRI(0)'''
    #ERRV TESTS
    '''infoERRV()
    getERRV()
    getERRV(1)
    getERRV(0)
    setERRV(0, 1)
    setERRV(1, 2)
    setERRV(2, 3)
    getERRV()
    getERRV(1)
    getERRV(0)'''
    #SLLROUT TESTS
    infoSLLROUT()
    getSLLROUT()
    getSLLROUT(1)
    getSLLROUT(0)
    setSLLROUT(0, 1)
    setSLLROUT(1, 2)
    setSLLROUT(2, 3)
    getSLLROUT()
    getSLLROUT(1)
    getSLLROUT(0)
    infoSLLROUTARGUEMENTS()
    infoSLLROUTARGUEMENTS('0')
    infoSLLROUTARGUEMENTS('001')
    infoSLLROUTARGUEMENTS('101')
    infoSLLROUTARGUEMENTS('201')
    infoSLLROUTARGUEMENTS('301')
    #SLLIMIT TESTS
    '''getSLLIMIT()
    getSLLIMIT(1)
    getSLLIMIT(0)
    infoSLLimit()
    setSLLIMIT(0, 1)
    setSLLIMIT(1, 2)
    setSLLIMIT(2, 3)
    getSLLIMIT()
    getSLLIMIT(1)
    getSLLIMIT(0)'''
    #SRLIMIT TESTS
    '''getSRLIMIT()
    getSRLIMIT(1)
    getSRLIMIT(0)
    infoSRLIMIT()
    setSRLIMIT(0, 1)
    setSRLIMIT(1, 2)
    setSRLIMIT(2, 3)
    getSRLIMIT()
    getSRLIMIT(1)
    getSRLIMIT(0)'''
















    #print(qAST(0))
    #ReadSystemInfo()
    #CheckPosition(0)
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
