__author__= "Made By Pyr3q"


import os
import tkinter
from tkinter import *
#import libraries


root = Tk()
root.geometry("600x300")
root.title("USB Info")
root.configure(background="black")
#define interface


a = os.popen('lsusb ').readlines()
a = list(a)
c = len(a)

for i in range(c):
	b = a[i]
	label1 = Label(root,text=b,bg="white",width=75,anchor=NW,justify=CENTER).pack(side="top")


def exit():
	root.destroy()
#function like sys.exit()

def author():
	os.system("firefox https://instagram.com/pyr3q")
#function who am i 

B1 = Button(root,text="Exit",command=exit,bg="white").place(x=360,y=260)
B2 = Button(root,text=__author__,command=author,bg="white").place(x=100,y=260)

root.mainloop()
