# -*- coding:utf-8 -*-

from socket import *

host = '123.57.220.107'
# host = 'anewme.cn'

port = 80

header = 'POST /login/phone HTTP/1.1\r\n' \
         'Host: anewme.cn\r\n' \
         'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0\r\n' \
         'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n' \
         'Accept-Language: en-US,en;q=0.5\r\n' \
         'Accept-Encoding: gzip, deflate\r\n' \
         'Content-Type: application/x-www-form-urlencoded\r\n' \
         'Content-Length: 85\r\n' \
         'Referer: http://anewme.cn/login?goto=/\r\n' \
         'Cookie: CNZZDATA1260082819=661439901-1504512085-%7C1506486599; UM_distinctid=15e501131e71c1-04e150cf6e0d02-12656e4a-100200-15e501131e91ce; PHPSESSID=f7fsn2t85nb5pltanuc3kt0ulm\r\n' \
         'Connection: close\r\n' \
         'Upgrade-Insecure-Requests: 1\r\n\r\n' \
         'mobile=18811484144&code=11111&_csrf_token=vzTAIBb8uz5Ulrgx5Pk5Rp7kDP2PK7-GqG9cMhorCno\r\n'

addr = (host, port)

s = socket(AF_INET, SOCK_STREAM)
s.connect(addr)

s.send(header.encode("utf8"))

data = s.recv(100)
try:
    for i in range(2):
        print(data)
        data = s.recv(1000)
except:
    pass
s.close()
