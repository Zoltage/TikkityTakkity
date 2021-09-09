from tkinter import *
import sys

win = Tk()

class GuiController():
    def __init__(self):
        self.buttoncolor = "#F2002C"
        self.bgcolor = "#0c0c0c"

    def Main(self):
        Clear()

        Label(win, text='Tic Tac Toe', bg=self.buttoncolor )

    win.mainloop()

def Clear():
    for widget in win.winfo_children():
        widget.destroy()

def Exit():
    sys.exit()

Main()

