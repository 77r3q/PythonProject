import os
import hashlib
import pyperclip
import tkinter
from tkinter import *

__author__ = "Made By Pyr3q" 

root = Tk()
root.geometry("300x300")
root.title("Encode MD5 APP")
root.configure(background="black")

label_md5 = Label(root,text="Entrer String: ",bg="white").pack()
entrer_md5 = StringVar()
entry_md5 = Entry(root, textvariable=entrer_md5).pack()
result = hashlib.md5(entrer_md5.get().encode())
cipher_result = result.hexdigest()

def copy():
	pyperclip.copy(cipher_result)

def encode_md5():
	button_md5_result = Button(root,text=cipher_result,bg="white",command=copy).place(x=20,y=150)

def exit():
	root.destroy()

def instagram():
	os.system("proxychains firefox https://instagram.com/pyr3q")

button_encode_md5 = Button(root,text="encode",command=encode_md5).place(x=10,y=250)
button_close_app = Button(root,text="Exit",command=exit).place(x=230,y=250)
button_author = Button(root,text=__author__,command=instagram).place(x=95,y=250)

root.mainloop()
