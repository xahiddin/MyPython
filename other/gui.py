from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
from tkinter import ttk

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

a = 0

def btn_click():
    global a
    global li
    a = a + 1
    li.append(a)
    print(li)
    if tkinter.messagebox.askyesno('eskertish', 'marry me'):

        print('she says yes')
    else:
        print('she says no')


tk = Tk()
tk.title('by xahidin')
tk.geometry('500x400+500+200')

li = []

label = Label(tk, text='hello world',style="BW.TLabel")
listbox = Listbox(tk)
#btn = Button(tk, command=btn_click, activeforeground='white', text='btn')

for item in li:
    listbox.insert(0, item)

#scale = Scale(tk, from_=0, to=100, orient=HORIZONTAL, activebackground='grey')
#scale.set(35)

label.pack()
listbox.pack()
# btn.pack()
# scale.pack()
tk.mainloop()
