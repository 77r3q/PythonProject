#__author__ : PyR3q
#IG: pyr3q

import tkinter
import random
import pyperclip
from tkinter import *
from random import sample

root = Tk()
root.title("Password Generator ")
root.geometry("300x300")
root.configure(background="black")
#interface tkinter 

label_app = Label(root,text="Password Generator",bg="white",font=("Helvetica",16)).place(x=50,y=20)

alphabet = "@!#$^&?()*abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key_password = 12
#we create an aplabet and a password size to define it

password = "".join(random.sample(alphabet,key_password))

def copy():
	pyperclip.copy(password)
	#copy char
def password_generator():
	button_password = Button(root,text=password,command=copy,bg="white").place(x=80,y=120)
	#print password
def close_app():
	root.destroy()
	#function like sys.exit()
button_close_app = Button(root,text="Exit",command=close_app,bg="white").place(x=20,y=240)
button_generator = Button(root,text="Generate !",command=password_generator,bg="white").place(x=180,y=240)

root.mainloop()
