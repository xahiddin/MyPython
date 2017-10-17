# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image
import pymysql.cursors
import random

con = pymysql.Connect(host='localhost', port=3306, user='root', passwd='xm', db='forpy', charset='utf8', )
cursor = con.cursor()

app = Tk()
app.title("Welcome")
app.resizable(width=False, height=False)
image = Image.open('bg.jpg')
background_image = ImageTk.PhotoImage(image)
w = background_image.width()
h = background_image.height()
app.geometry('%dx%d+0+0' % (w, h))

l = StringVar()
b1 = StringVar()
b2 = StringVar()
b3 = StringVar()
b4 = StringVar()
b5 = StringVar()

background_label = Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def get_en_by_id(id):
    sql_en = "select `en` from vocabulary where id=%d" % id
    cursor.execute(sql_en)
    result_en = cursor.fetchone()
    return result_en[0]


def get_en_by_uy(cn):
    sql_en_by_cn = "select `en` from vocabulary where uy='%s'" % cn
    cursor.execute(sql_en_by_cn)
    result_en_by_cn = cursor.fetchone()
    return result_en_by_cn[0]


def get_uy():
    sql_uy = "select `uy` from vocabulary"
    cursor.execute(sql_uy)
    result_uy = cursor.fetchall()
    return result_uy


def random_getuy():
    n = random.randint(0, len(get_uy()) - 1)
    return get_uy()[n][0]


def settext():
    b1.set(random_getuy())
    b2.set(random_getuy())
    if b1.get() == b2.get():
        b2.set(random_getuy())
    b3.set(random_getuy())
    if b2.get() == b3.get() or b1.get() == b3.get():
        b3.set(random_getuy())
    b4.set(random_getuy())
    if b2.get() == b4.get() or b3.get() == b4.get() or b1.get() == b4.get():
        b4.set(random_getuy())
    b5.set(random_getuy())
    if b4.get() == b5.get() or b3.get() == b5.get() or b2.get() == b5.get() or b1.get() == b5.get():
        b5.set(random_getuy())

    btns = [b1, b2, b3, b4, b5]
    ltext = get_en_by_uy(random.choice(btns).get())
    l.set(ltext)


settext()


def click(b, btn):
    sql_id = "select `id` from vocabulary where uy='%s'" % b.get()
    cursor.execute(sql_id)
    result_id = cursor.fetchone()
    result = get_en_by_id(result_id)
    if result == l.get():
        btn['bg'] = 'blue'
    else:
        btn['bg'] = 'red'


def refresh():
    settext()


ft = tkFont.Font(family='alkatip kofi', size=15, weight=tkFont.BOLD)

label = Label(app, text=l.get(), font=ft, compound='center', bg='white').grid(row=1, column=3)

btn1 = Button(app, text=b1.get(), width=6, height=2, font=ft, compound='center', command=lambda: click(b1, btn1),
              bg='white', padx=3)
btn2 = Button(app, text=b2.get(), width=6, height=2, font=ft, compound='center', image=None,
              command=lambda: click(b2, btn2),
              bg='white', padx=3)

btn3 = Button(app, text=b3.get(), width=6, height=2, font=ft, compound='center', image=None,
              command=lambda: click(b3, btn3),
              bg='white', padx=3)

btn4 = Button(app, text=b4.get(), width=6, height=2, font=ft, compound='center', command=lambda: click(b4, btn4),
              bg='white', padx=3)

btn5 = Button(app, text=b5.get(), width=6, height=2, font=ft, compound='center', command=lambda: click(b4, btn5),
              bg='white', padx=3)

btn1.grid(row=5, column=1)
btn2.grid(row=5, column=2)
btn3.grid(row=5, column=3)
btn4.grid(row=5, column=4)
btn5.grid(row=5, column=5)

app.mainloop()
