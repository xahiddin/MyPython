import urllib.error
import requests
from time import sleep

def down(url):
    ftype = url.split(".")
    try:
        pic = requests.get(url, timeout=10)
    except requests.exceptions.ConnectionError:
        print("404")
    fp = open('E:/z_user_Image/' + str(i) + "." + ftype[2], 'wb')
    fp.write(pic.content)
    fp.close()


addr = "http://anewme.cn/api/anewme/user?id="
t = 0
for i in range(1, 50):
    url = addr + str(i)
    res = urllib.request.urlopen(url).read().decode('utf8')
    value = eval(res)  # str to dict
    if value['largeAvatar'] == "":
        continue
    down(value['largeAvatar'].replace("\\", ""))
    sleep(0.5)
    if value['role'] == 'teacher':
        t = t + 1
        print("%s is teacher" %value['nickname'])
