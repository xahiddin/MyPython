import threading
import re
from bs4 import BeautifulSoup
from time import sleep
import urllib.request


def gets(soup):
    td = soup.find_all('td')

    timepat = re.compile(r'.*?>([\d-]{6,})<.*?')
    apat = re.compile(r'.*?href="(/.*?)".*?')
    titlepat = re.compile(r'.*?href="/news.*?>(.*?)<.*?')

    time = re.findall(timepat, str(td))
    a = re.findall(apat, str(td))
    title = re.findall(titlepat, str(td))

    for i in range(0, len(title)):
        print("url-->%s title-->%s time-->%s" % (a[i], title[i], time[i]))
    print("\r\n")

def get_soup(page):
    addr = 'https://sec-wiki.com/news/?ajax=yw0&News_page=' + str(page)
    response = urllib.request.urlopen(addr)
    html = response.read().decode('utf-8', 'ignore')
    soup = BeautifulSoup(html, 'html.parser')
    get_last(soup)
    gets(soup)


def get_last(soup):
    li = soup.find('li', class_="last")
    asoup = BeautifulSoup(str(li), 'html.parser')
    lasta = asoup.find('a').get('href')
    lastid = lasta.split("=")[1]
    return lastid


if __name__ == "__main__":
    for page in range(1, 5):
        print(page)
        t = threading.Thread(target=get_soup, args=(get_soup(page),))
        t.start()
