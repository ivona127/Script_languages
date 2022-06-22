from tkinter import *
import random
import string
import pyperclip

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.config(bg= "pink")

root.title("DataFlair-PASSWORD GENERATOR")
Label(root, text = "PASSWORD GENERATOR APPLICATION", font = "arial 10 bold").pack()

pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 8 ').pack()
pass_len = IntVar()
length = Spinbox(root,from_ = 8, to_ = 32, textvariable = pass_len,  width = 15).pack()

pass_str = StringVar()
def Generator ():
    password = ''

    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)

    for y in range(pass_len.get() - 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


but1 = Button(root, text = "GENERATE PASSWORD", command = Generator).pack(pady = 5)
ent1 = Entry(root, textvariable = pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())

but2 = Button(root, text = "COPY TO CLIPBOARD", command = Copy_password ).pack(pady = 10)

Label(root, text ='DataFlair - Password generator', font ='arial 9 bold').pack(side = BOTTOM)
root.mainloop()