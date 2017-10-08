# -*- coding:utf-8 -*-

from urllib import request

if __name__ == "__main__":
    host = 'http://www.anewme.cn/login/phone'

    port = 80
    head = {}

    head['POST'] = '/login/phone HTTP/1.1'
    head['Host'] = 'anewme.cn'
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'
    head['Content-Type'] = 'application/x-www-form-urlencoded'
    head['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    head[
        'Cookie'] = 'CNZZDATA1260082819=661439901-1504512085-%7C1506486599; UM_distinctid=15e501131e71c1-04e150cf6e0d02-12656e4a-100200-15e501131e91ce; PHPSESSID=f7fsn2t85nb5pltanuc3kt0ulm'
    head['Referer'] = ' http://anewme.cn/login?goto=/'
    head['Connection'] = 'close'
    head['Upgrade-Insecure-Requests'] = 1
    head['Body'] = 'mobile=18811484144&code=%s&_csrf_token=vzTAIBb8uz5Ulrgx5Pk5Rp7kDP2PK7-GqG9cMhorCno' % "222222"

    print(head['Body'])
    req = request.Request(host, headers=head)
    response = request.urlopen(req)
    page = response.read().decode('utf-8')
    print(page)
