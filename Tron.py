import subprocess
from tkinter import *
from subprocess import call
import os

tk = Tk()

def run():
    call(['python', 'app.py'])

def help():
    os.system("notepad.exe instructions.txt")

tk.title('Tron Launcher')
tk.geometry("150x75") #Sets Menu Dimensions
tk.eval('tk::PlaceWindow %s center' % tk.winfo_toplevel()) #Centers Window
tk.resizable(False, False) #Disables Window Adjustments

head = Label(tk, text = 'Tron Launcher')
play = Button(tk, text='Play Game', command= run )
instr = Button(tk, text='Instructions', command= help )

head.pack()
play.pack()
instr.pack()

mainloop() #Keeps code running
