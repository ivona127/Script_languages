import os
import tkinter as tk
from tkinter import *

def printFile(event):
    sel = lb.get(lb.curselection()[0])
    f = open(sel, 'r')
    t.delete('1.0', END)
    for line in f:
        t.insert(INSERT, line)
    f.close()

def fillList():
    files=os.listdir()
    lb.delete(0, END)
    for file_ in files:
        lb.insert(END, file_)   

root = tk.Tk()
root.geometry("1000x500")
Label(root, text='Buttons:').grid(row=0, column=0)
Label(root, text='File List:').grid(row=0, column=1, padx=10)
Label(root, text='File content:').grid(row=0, column=2, padx=10)
b = Button(root,text="Get files:", command=fillList).grid(row=1, column=0, sticky=N)
lb = Listbox(root)
lb.grid(row=1, column=1, sticky=N, padx=10)
lb.bind("<Double-Button-1>", printFile)
t = Text(root)
t.grid(row=1, column=2, sticky=N, padx=10)
root.mainloop()
