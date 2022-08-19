import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

def writeToACS(acsCommand):
    soc.send(str.encode(acsCommand + '\r'))

def recvall(buffSize):
    fragments = []
    while True:
        try:
            chunk = soc.recv(buffSize).decode("utf-8").replace('\r','\r\n')
            fragments.append(chunk)
        except:
            break
    message = ''.join(fragments)
    return message

def ACSConnect(address='10.0.0.100', port=701):
    soc.connect((address, port))
    soc.settimeout(0.5)

def ReturnCheck():
    check = recvall(1024)
    print(check)
