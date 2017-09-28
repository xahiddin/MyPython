from bs4 import BeautifulSoup
import urllib.request
import re
from time import sleep

for x in range(1, 5):
    url = "http://anewme.cn/user/" + str(x)
    try:
        response = urllib.request.urlopen(url)
        html = response.read().decode("utf-8", 'ignore')
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div', class_='name')
        sp = re.split('\\n', str(div))
        print(x, sp[1])
        sleep(0.5)
    except url.urlError as reason:
        print(reason)
