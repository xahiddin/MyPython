# -*- coding:utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup
from threading import Thread
from time import sleep


def conn():
    host = 'http://www.anewme.cn/login/phone'
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
    head['Body'] = 'mobile=18811484144; code=%s; _csrf_token=vzTAIBb8uz5Ulrgx5Pk5Rp7kDP2PK7-GqG9cMhorCno' % 827848
    req = request.Request(host, headers=head)
    response = request.urlopen(req)
    page = response.read().decode('utf-8')
    soup = BeautifulSoup(page, 'html.parser')
    div = soup.find('title')
    print(page)


conn()
