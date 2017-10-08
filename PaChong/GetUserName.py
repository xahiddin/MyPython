from bs4 import BeautifulSoup
import urllib.request
import re
from time import sleep
from threading import Thread
import urllib.error


def uname(n):
    url = "http://anewme.cn/user/" + str(n)
    try:
        response = urllib.request.urlopen(url)
        html = response.read().decode("utf-8", 'ignore')
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div', class_='name')
        sp = re.split('\\n', str(div))
        print(n, sp[1])
    except urllib.error.HTTPError as reason:
        print(reason)


if __name__ == "__main__":
    for i in range(1, 1000):
        t = Thread(target=uname, args=(i,))
        sleep(0.01)
        t.start()
        t.join()
