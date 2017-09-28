# coding=utf-8
import pymysql.cursors
from tkinter import *

tk = Tk()
tk.title("for xahidin")
tk.geometry("300x300+400+200")
tk.resizable(width=False, height=False)
e1 = StringVar()
e2 = StringVar()
e1.set("مەن")
e2.set("2008-8-9")
En = Entry(tk, textvariable=e1, bd=5, relief=RIDGE, font=40, justify=RIGHT)
Ed = Entry(tk, textvariable=e2, bd=5, relief=RIDGE, font=40, justify=RIGHT)

con = pymysql.Connect(host='localhost', port=3306, user='root', passwd='xm', db='forpy', charset='utf8', )
cursor = con.cursor()


def save():
    sta = cursor.execute("insert into social (name,brithday) values('" + e1.get() + "','" + e2.get() + "')")
    if sta == 1:
        print("shoh")
    else:
        print("poh")
    con.commit()
    sel()


def dele():
    lbs = lb.selection_get()
    id = lbs.split("---->")
    sta = cursor.execute("delete from social where id='" + id[0] + "'")
    if sta == 1:
        print("shoh")
    else:
        print("poh")
    sel()


sql = """create table `social`
 (
	`id` int(10) NOT NULL AUTO_INCREMENT,
	`name` varchar(20) NOT NULL,
	`brithday` date DEFAULT NULL,
	PRIMARY KEY (`id`)
	)CHARSET=UTF8;"""

select = "select * from social"

insert = "insert into social (name,brithday) values (%s,%s)"

btn_insert = Button(tk, text="ساقلاش", command=save, width=6, height=2, bg='gray', relief=RIDGE)
btn_delete = Button(tk, text="يۇيۇش", command=dele, width=6, height=2, bg='gray')
En.grid(row=1, column=1)
Ed.grid(row=2, column=1)
btn_insert.grid(row=3, column=1)
lb = Listbox(tk, width=50)


def sel():
    lb.delete(0, lb.size())
    cursor.execute(select)
    result = cursor.fetchall()
    for i in result:
        lbstr = i[0], "---->", i[1], "---->", i[2]
        lb.insert(END, lbstr)
    lb.selection_set(lb.size() - 1)


lb.grid(row=4, column=1)
btn_delete.grid(row=5, column=1)

sel()
tk.mainloop()
