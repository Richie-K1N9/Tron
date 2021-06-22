import subprocess
from subprocess import call
import os
import sys

if sys.version_info[0] < 3: #Checks if the User is running an older version of Python
    import Tkinter
    import tkMessageBox
    tkMessageBox.showerror('Python Error', 'Must be running Python 3.x')

from tkinter import *

tk = Tk()
var = IntVar()

def ed():
    call(['pythonw', 'easy.file'])

def md():
    call(['pythonw', 'medium.file'])

def hd():
    call(['pythonw', 'hard.file'])

def help():
    os.system('notepad.exe README.txt')

tk.title('Tron Launcher')
tk.geometry('175x125') #Sets Menu Dimensions
tk.eval('tk::PlaceWindow %s center' % tk.winfo_toplevel()) #Centers Window
tk.resizable(False, False) #Disables Window Adjustments

head = Label(tk, text='Chose Difficulty')
easy = Button(tk, text='Easy', command= ed )
medium = Button(tk, text='Medium', command= md )
hard = Button(tk, text='Hard', command= hd )
instr = Button(tk, text='How to use', command= help )

easy.pack()
medium.pack()
hard.pack()
instr.pack()

mainloop() #Keeps code running