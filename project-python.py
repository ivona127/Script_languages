import tkinter as tk
from tkinter import *
from tkinter.filedialog import *

def openFile ():
    name_file  = askopenfilename()
    f = open(name_file,"r",encoding='utf-8')
    file_content  = f.read()
    text.delete ('1.0',END)
    text.insert (END,file_content)

def saveFile ():
    save_as = asksaveasfilename ()
    file_content  = text.get('1.0',END)
    f = open(save_as,"w",encoding='utf-8')
    f.write(file_content)
    
root = tk.Tk()
root.geometry  ("1000x500")
root.title ("View,edit  and save text files")
root.configure(background='#cce5ff')

labl = Label (root, text= "Write something",background='#ffffff').grid(pady=10)

menu = Menu(root)
root.config(menu=menu)

m = Menu(menu)
menu.add_cascade(label="Files",menu = m)
m.add_command(label="Open",command = openFile)
m.add_command(label="Save as",command = saveFile)
m.add_command(label="Exit",command = root.destroy)

text = Text(root)
text.grid(sticky=N, padx=200,pady=15)

root.mainloop()



