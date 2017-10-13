import re
import urllib.request
from bs4 import BeautifulSoup
import re

addr = "http://www.ulinix.com"
request = urllib.request.urlopen(addr)
html = request.read().decode("utf8")
reg = re.compile(r'.*?<a href="(.*?)".*?')
a = reg.match(html)
if a:
    a1 = reg.findall(html)
    print(a1)
else:
    print("yoq ")
