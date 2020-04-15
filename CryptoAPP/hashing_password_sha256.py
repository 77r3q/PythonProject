import os
import hashlib
import pyperclip
import tkinter
from tkinter import *

__author__ = "Made By Pyr3q" 

root = Tk()
root.geometry("500x300")
root.title("Encode SHA256 APP")
root.configure(background="black")

label_sha256 = Label(root,text="Entrer String: ",bg="white").pack()
entrer_sha256 = StringVar()
entry_sha256 = Entry(root, textvariable=entrer_sha256).pack()
result = hashlib.sha256(entrer_sha256.get().encode())
cipher_result = result.hexdigest()

def copy():
	pyperclip.copy(cipher_result)

def encode_sha256():
	button_sha256_result = Button(root,text=cipher_result,bg="white",command=copy).place(x=1,y=150)

def exit():
	root.destroy()

def instagram():
	os.system("proxychains firefox https://instagram.com/pyr3q")

button_encode_sha256 = Button(root,text="encode",command=encode_sha256).place(x=10,y=250)
button_close_app = Button(root,text="Exit",command=exit).place(x=430,y=250)
button_author = Button(root,text=__author__,command=instagram).place(x=185,y=250)

root.mainloop()
