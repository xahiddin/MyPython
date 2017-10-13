# -*- coding:utf-8 -*-
import re
from time import sleep
from bs4 import BeautifulSoup
import urllib.request, urllib.error
from tkinter import *
import tkinter.messagebox
import requests

tk = Tk()
tk.title('Get Img')
tk.geometry('500x150+500+200')
tk.resizable(width=False, height=False)


def saveImg(url, x):
    a = str(url).split(".")
    try:
        pic = requests.get(url, timeout=10)
    except requests.exceptions.ConnectionError:
        print('error')
    string = path.get() + str(x) + '.' + a[2]
    print(string)
    fp = open(string, 'wb+')
    fp.write(pic.content)
    fp.close()
    print("downloaded", x)


def saveTxt():
    for x in range(varFrom.get(), varTo.get()):
        url = addr.get() + str(x)
        try:
            response = urllib.request.urlopen(url)
            html = response.read().decode("utf-8", 'ignore')
            soup = BeautifulSoup(html, 'html.parser')
            div = soup.find('div', class_=varClass1.get())
            sp = re.split('\\n', str(div))
            print(x, sp[1])
            with open(filePath.get(), "a", encoding='utf-8') as fp:
                fp.write(str(x) + "-->" + sp[1] + "\r\n")
            fp.close()
            sleep(0.5)
        except urllib.error.URLError as reason:
            tkinter.messagebox.showerror("eroor", reason)


def down():
    for x in range(varFrom.get(), varTo.get()):
        url = addr.get() + str(x)
        try:
            response = urllib.request.urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            img = soup.find('img', class_=varClass.get()).get("src")
            fulladdr = indexAddr.get() + img
            saveImg(fulladdr, x)
            sleep(0.5)
        except urllib.error.URLError as reason:
            tkinter.messagebox.showerror("eroor", reason)


indexAddr = StringVar()
indexAddr.set("http://anewme.cn")
addr = StringVar()
path = StringVar()
filePath = StringVar()
addr.set("http://anewme.cn/user/")
path.set("E:/")
filePath.set("E:/a.txt")
RadioText = IntVar()
RadioText.set(1)
varFrom = IntVar()
varTo = IntVar()
varFrom.set(1)
varTo.set(700)
varClass = StringVar()
varClass.set("avatar-lg")
varClass1 = StringVar()
varClass1.set("name")
varlabel = StringVar()
varlabel.set("div")

panes = PanedWindow(tk, orient=VERTICAL)

frm = Frame(panes)
l_uri = Label(frm, height=2, text='ئادرىس').grid(row=1, column=1)
e_uri = Entry(frm, width=40, textvariable=addr).grid(row=1, column=2)
l_from = Label(frm, height=2, text='قانچىدىن').grid(row=1, column=3)
e_from = Entry(frm, width=3, textvariable=varFrom).grid(row=1, column=4)
l_to = Label(frm, height=2, text='قانچىگىچە').grid(row=1, column=5)
e_to = Entry(frm, width=3, textvariable=varTo).grid(row=1, column=6)

frm1 = Frame(panes)
l_url = Label(frm1, height=2, text='ئادرىس').grid(row=1, column=1)
e_url = Entry(frm1, width=40, textvariable=path).grid(row=1, column=2)
l_class = Label(frm1, height=2, text='class=').grid(row=1, column=3)
e_class = Entry(frm1, width=10, textvariable=varClass).grid(row=1, column=4)
btn_start = Button(frm1, text="چۈشۈرۈش", command=down).grid(row=1, column=5)

frm2 = Frame(panes)
l_url1 = Label(frm2, height=2, text='ئادرىس').grid(row=1, column=1)
e_url1 = Entry(frm2, width=20, textvariable=filePath).grid(row=1, column=2)
l_label = Label(frm2, height=2, text='خەتكۈچ').grid(row=1, column=3)
e_label = Entry(frm2, width=10, textvariable=varlabel).grid(row=1, column=4)
l_class1 = Label(frm2, height=2, text='class=').grid(row=1, column=5)
e_class1 = Entry(frm2, width=10, textvariable=varClass1).grid(row=1, column=6)
btn_start = Button(frm2, text="ساقلاش", command=saveTxt).grid(row=1, column=7)


def sel():
    if (RadioText.get() == 1):
        panes.add(frm2)
        panes.remove(frm1)
    if (RadioText.get() == 0):
        panes.add(frm1)
        panes.remove(frm2)


frm_R = Frame(tk)
r1 = Radiobutton(frm_R, text="تېكىست", variable=RadioText, value=1, command=sel).grid(row=1, column=1)
r2 = Radiobutton(frm_R, text="رەسىم", variable=RadioText, value=0, command=sel).grid(row=1, column=2)
frm_R.pack()
frm.pack()

panes.add(frm)
panes.add(frm1)
panes.add(frm2)
panes.pack()

sel()
tk.mainloop()
