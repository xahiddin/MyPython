# -*- coding: utf-8 -*-

from tkinter import *
import tkinter
from PIL import ImageTk, Image
import pymysql.cursors
import random

con = pymysql.Connect(host='localhost', port=3306, user='root', passwd='xm', db='forpy', charset='utf8', )
cursor = con.cursor()

app = Tk()
app.title("Welcome")
image = Image.open('back.jpg')
background_image = ImageTk.PhotoImage(image)
w = background_image.width()
h = background_image.height()
app.geometry('%dx%d+0+0' % (w, h))

l = StringVar()
b1 = StringVar()
b2 = StringVar()
b3 = StringVar()
b4 = StringVar()

background_label = Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def get_en(id):
    sql_en = "select `en` from vocabulary where id=%d" % id
    cursor.execute(sql_en)
    result_en = cursor.fetchone()
    return result_en[0]


def get_uy():
    sql_uy = "select `uy` from vocabulary"
    cursor.execute(sql_uy)
    result_uy = cursor.fetchall()
    return result_uy


panes = PanedWindow(app, orient=HORIZONTAL)

b1.set(get_uy()[random.randint(0, len(get_uy()) - 1)][0])
b2.set(get_uy()[random.randint(0, len(get_uy()) - 1)][0])
b3.set(get_uy()[random.randint(0, len(get_uy()) - 1)][0])
b4.set(get_uy()[random.randint(0, len(get_uy()) - 1)][0])
l.set(get_en(random.randint(1, 4), ))


def click(b):
    sql_id = "select `id` from vocabulary where uy='%s'" % b.get()
    cursor.execute(sql_id)
    result_id = cursor.fetchone()
    result = get_en(result_id)
    if result == l.get():
        print("right")

photo = tkinter.PhotoImage(file='wrong.png')
frm1 = Frame(panes)
frm2 = Frame(panes)
label = Label(frm1, text=l.get(), compound='center', bg='white').pack()

btn1 = Button(frm2, text=b1.get(), compound='center', command=lambda: click(b1), bg='white', image=photo).grid(row=1,
                                                                                                               column=1)
btn2 = Button(frm2, text=b2.get(), compound='center', command=lambda: click(b2), bg='white', image=photo).grid(row=1,
                                                                                                               column=2)
btn3 = Button(frm2, text=b3.get(), compound='center', command=lambda: click(b3), bg='white', image=photo).grid(row=1,
                                                                                                               column=3)
btn4 = Button(frm2, text=b4.get(), compound='center', command=lambda: click(b4), bg='white', image=photo).grid(row=1,
                                                                                                               column=4)

frm1.pack()
frm2.pack()
panes.pack()
app.mainloop()
