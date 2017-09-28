from bs4 import BeautifulSoup
import urllib.request, urllib.error
import re
import requests
from time import sleep
import os


def download(url):
    a = str(url).split(".")
    print(a[2])
    try:
        pic = requests.get(url, timeout=10)
    except requests.exceptions.ConnectionError:
        print('error')
    string = 'E:/z_user_Image/' + str(x) + '.' + a[2]
    fp = open(string, 'wb')
    fp.write(pic.content)
    fp.close()
    print("downloaded", x)


addr = "http://anewme.cn"
for x in range(1, 4):
    url = "http://anewme.cn/user/" + str(x)
    try:
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        img = soup.find('img', class_='avatar-lg').get("src")
        fulladdr = addr + img
        print(fulladdr)
        download(fulladdr)
        sleep(0.5)
    except url.urlError as reason:
        print(reason)
