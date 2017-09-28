import re
import urllib2
from bs4 import BeautifulSoup
import requests
addr="http://www.ulinix.com"
request=urllib2.Request(addr)
response=urllib2.urlopen(request)
html=response.read()
soup=BeautifulSoup(html,'html.parser')
img=soup.findAll('img')
for i in range(len(img)):
	print img[i].get('src')