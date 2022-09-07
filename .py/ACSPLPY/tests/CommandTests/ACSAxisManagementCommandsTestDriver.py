import socket, time
from ...ACSPLPY_Tools.ACSLowLevel import *
from ...ACSPLPY_Variables.SafetyLimitVariables import *
from ...ACSPLPY_Commands.AxisManagementCommands import *

address = '172.31.0.146' #if running simulator this should be your ip address
port = 701
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)



def CheckPosition(axis):
    writeToACS(f'?FPOS({axis})')
    FPOS = recvall(1024)
    print(f'Axis {axis} Position is')
    print(FPOS)


if __name__ == '__main__':
    ACSConnect(address, port)
    CheckPosition(0)
    #getCERRA()
    BREAK([0]) # expected success
    BREAK([0,1]) #expected success
    BREAK(1) # expected success
    #BREAK(1, 2) #expected type error 
    infoBREAK()
    infoCOMMUT()
    #COMMUT(0) - validation todo
    #CONNECT() - unclear validation procedure
    #CSCREATE() - validation todo
    #CSDESTROY() - validation todo
    DISABLE(1)
    DISABLE([1,2])
    DISABLE("ALL")
    DISABLE(1,6100)
    DISABLE([1,2,3],6100)
    ENABLE(1)
    ENABLE([1,2])
    ENABLE("ALL")
    #ENABLE(1,2) #expected type error
    #ENCINIT() - implementation todo
    #ENCREAD() - validation todo
    FCLEAR(1)
    FCLEAR([1,2])
    FCLEAR("ALL")
    #FOLLOW(1) validation todo
    #GO() validation todo
    #GROUP() validation todo
    HALT(1)
    HALT([1,2])
    HALT("ALL")
    infoHALT()
    infoIMM()



    











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
