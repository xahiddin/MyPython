from socket import *

host = '192.168.20.54'
port = 7777

bufsize = 1024
addr = (host, port)
clisock = socket(AF_INET, SOCK_DGRAM)
clisock.connect(addr)

while True:
    data = input('>>>')
    if not data:
        break
    clisock.sendto(data, addr)
    data = clisock.recvfrom(bufsize)
    print(data)
clisock.close()
