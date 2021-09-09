# Jacob Mathews
# TicTacToe
# 9 / 9 / 21

from tkinter import *
import sys

win = Tk()
win.option_add("*font", "roboto 20")
win.configure(bg="#000000")


def Main():
    Clear()

    Label(win, text= "DGS LLC Database", fg='#64ffff', bg='#646464').grid(row=1, column=1)
    Label(win, text='', bg='#000000').grid(row=2, column=0)

    Button(win, text="Reports", command=reportMenu, padx=16, bd=2, relief=SOLID).grid(row=3, column=0,sticky='nesw')
    Button(win, text="Exit", command=endWin, bg="#646464", fg="#64ffff", bd=2, relief=SOLID).grid(row=3, column=2,sticky='nesw')
    Button(win, text="Enter / Edit\nCustomers", command=customerMenu, bd=2, relief=SOLID).grid(row=4, column=0)
    Button(win, text="Enter / Edit\nProducts", command=productMenu, bd=2, relief=SOLID).grid(row=4, column=1)
    Button(win, text="Enter / Edit\nSales", command=salesMenu, bd=2, relief=SOLID).grid(row=4, column=2)

def Clear():
    for widget in win.winfo_children():
        widget.destroy()

def Exit():
    sys.exit()

Main()
win.mainloop()
