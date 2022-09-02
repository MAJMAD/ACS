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
from SLLROUT import *
from XACC import *
from XCURCDB import *
from XCURI import *
from XCURK import *
from XCURV import *
from XRMS import *
from XRMSD import *
from XRMSM import *
from XRMST import *
from XRMSTD import *
from XRMSTM import *
from XSACC import *
from XVEL import *


address = '172.31.0.146' #if running simulator this should be your ip address
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
    '''infoSLLROUT()
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
    infoSLLROUTARGUEMENTS('301')'''
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
    #XACC TESTS
    '''infoXACC()
    getXACC()
    getXACC(1)
    getXACC(0)
    setXACC(0, 1)
    setXACC(1, 2)
    setXACC(2, 3)
    setXACC(3, -1)# error code return expected
    getXACC()
    getXACC(1)
    getXACC(0)'''
    #XCURCDB TESTS
    '''infoXCURCDB()
    getXCURCDB()
    getXCURCDB(1)
    getXCURCDB(0)
    setXCURCDB(0, 1)
    setXCURCDB(1, 2)
    setXCURCDB(2, 3)
    setXCURCDB(3, -1)# error code return expected
    getXCURCDB()
    getXCURCDB(1)
    getXCURCDB(0)'''
    #XCURI TESTS
    '''infoXCURI()
    getXCURI()
    getXCURI(1)
    getXCURI(0)
    setXCURI(0, 1)
    setXCURI(1, 2)
    setXCURI(2, 3)
    setXCURI(3, -1)# error code return expected
    getXCURI()
    getXCURI(1)
    getXCURI(0)'''
    #XCURK TESTS
    '''infoXCURK()
    getXCURK()
    getXCURK(1)
    getXCURK(0)
    setXCURK(0, 1)
    setXCURK(1, 2)
    setXCURK(2, 3)
    setXCURK(3, -1)# error code return expected
    getXCURK()
    getXCURK(1)
    getXCURK(0)'''
    #XCURV TESTS
    '''infoXCURV()
    getXCURV()
    getXCURV(1)
    getXCURV(0)
    setXCURV(0, 1)
    setXCURV(1, 2)
    setXCURV(2, 3)
    setXCURV(3, -1)# error code return expected
    getXCURV()
    getXCURV(1)
    getXCURV(0)'''
    #XRMS TESTS
    '''infoXRMS()
    getXRMS()
    getXRMS(1)
    getXRMS(0)
    setXRMS(0, 1)
    setXRMS(1, 2)
    setXRMS(2, 3)
    setXRMS(3, -1)# error code return expected
    getXRMS()
    getXRMS(1)
    getXRMS(0)'''
    #XRMSD TESTS
    '''infoXRMSD()
    getXRMSD()
    getXRMSD(1)
    getXRMSD(0)
    setXRMSD(0, 1)
    setXRMSD(1, 2)
    setXRMSD(2, 3)
    setXRMSD(3, -1)# error code return expected
    getXRMSD()
    getXRMSD(1)
    getXRMSD(0)'''
    #XRMSM TESTS
    '''infoXRMSM()
    getXRMSM()
    getXRMSM(1)
    getXRMSM(0)
    setXRMSM(0, 1)
    setXRMSM(1, 2)
    setXRMSM(2, 3)
    setXRMSM(3, -1)# error code return expected
    getXRMSM()
    getXRMSM(1)
    getXRMSM(0)'''
    #XRMST TESTS
    '''infoXRMST()
    getXRMST()
    getXRMST(1)
    getXRMST(0)
    setXRMST(0, 1)# error code return expected
    setXRMST(1, 2)# error code return expected
    setXRMST(2, 3)# error code return expected
    setXRMST(3, -1)# error code return expected
    setXRMST(4,199)# error code return expected
    setXRMST(5,200)
    setXRMST(6,201)
    setXRMST(1,3259)# unexpected error code observed
    setXRMST(2,3260)# unexpected error code observed
    setXRMST(3,3261)# error code return expected
    setXRMST(1,3229)
    setXRMST(2,3230)
    setXRMST(3,3231)# error code return expected but not seen???
    getXRMST()
    getXRMST(1)
    getXRMST(0)'''
    #XRMSTD TESTS
    '''infoXRMSTD()
    getXRMSTD()
    getXRMSTD(1)
    getXRMSTD(0)
    setXRMSTD(0, 1)# error code return expected
    setXRMSTD(1, 2)# error code return expected
    setXRMSTD(2, 3)# error code return expected
    setXRMSTD(3, -1)# error code return expected
    setXRMSTD(4,199)# error code return expected
    setXRMSTD(5,200)
    setXRMSTD(6,201)
    setXRMSTD(7,3259)
    setXRMSTD(8,3260)
    setXRMSTD(9,3261)
    setXRMSTD(10,59999)
    setXRMSTD(11,60000)
    setXRMSTD(12,60001)# error code return expected
    getXRMSTD()
    getXRMSTD(1)
    getXRMSTD(0)
    getXRMST()#unexplained 20000 values observed along axis 10 and 11, based on the following XRMSTM default values of 20,000 maybe a bug or issue with memory leak?'''
    #XRMSTM TESTS
    '''infoXRMSTM()
    getXRMSTM()
    getXRMSTM(1)
    getXRMSTM(0)
    setXRMSTM(0, 1)# error code return expected
    setXRMSTM(1, 2)# error code return expected
    setXRMSTM(2, 3)# error code return expected
    setXRMSTM(3, -1)# error code return expected
    setXRMSTM(4,199)# error code return expected
    setXRMSTM(5,200)
    setXRMSTM(6,201)
    setXRMSTM(7,3259)
    setXRMSTM(8,3260)
    setXRMSTM(9,3261)
    setXRMSTM(10,59999)
    setXRMSTM(11,60000)
    setXRMSTM(12,60001)
    setXRMSTM(13,599999)
    setXRMSTM(14,600000)
    setXRMSTM(15,600001)# error code return expected
    getXRMSTM()
    getXRMSTM(1)
    getXRMSTM(0)'''
    #XSACC TESTS
    '''infoXSACC()
    getXSACC()
    getXSACC(1)
    getXSACC(0)
    setXSACC(0, 1)
    setXSACC(1, 2)
    setXSACC(2, 3)
    setXSACC(3, -1)# error code return expected
    setXSACC(4,199)
    setXSACC(5,200)
    setXSACC(6,201)
    setXSACC(7,3259)
    setXSACC(8,3260)
    setXSACC(9,3261)
    setXSACC(10,59999)
    setXSACC(11,60000)
    setXSACC(12,60001)
    setXSACC(13,599999)
    setXSACC(14,600000)
    setXSACC(15,600001)
    getXSACC()
    getXSACC(1)
    getXSACC(0)'''
    #XVEL TESTS
    infoXVEL()
    getXVEL()
    getXVEL(1)
    getXVEL(0)
    setXVEL(0, 1)
    setXVEL(1, 2)
    setXVEL(2, 3)
    setXVEL(3, -1)# error code return expected
    setXVEL(4,199)
    setXVEL(5,200)
    setXVEL(6,201)
    setXVEL(7,3259)
    setXVEL(8,3260)
    setXVEL(9,3261)
    setXVEL(10,59999)
    setXVEL(11,60000)
    setXVEL(12,60001)
    setXVEL(13,599999)
    setXVEL(14,600000)
    setXVEL(15,600001)
    getXVEL()
    getXVEL(1)
    getXVEL(0)















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
