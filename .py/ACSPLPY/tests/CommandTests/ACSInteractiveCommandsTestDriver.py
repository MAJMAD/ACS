import socket
from ACSPLPY.ACSPLPY_Tools.ACSLowLevel import *
from ACSPLPY.ACSPLPY_Commands.InteractiveCommands import *

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
    infoINP()
    