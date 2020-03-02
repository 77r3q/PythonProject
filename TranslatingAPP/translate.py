import tkinter
import googletrans
import os
from tkinter import *
from googletrans import Translator
from os import system

#import libraries

translator = Translator(service_urls=['translate.google.com'])
#translator service

root = Tk()

root.title("Translate APP")
root.geometry("500x400")
root.configure(background='black')

message = StringVar()
source = StringVar()
destination = StringVar()

label1 = Label(root,text="Enter Sentence: ",bg="red").place(x=60,y=5)
entry_1 = Entry(root, textvariable=message).place(x=175,y=5)
label2 = Label(root,text="Enter Source Langage: ",bg="red").place(x=60,y=50)
entry_2 = Entry(root, textvariable=source).place(x=218,y=50)
label3 = Label(root,text="Enter Destination Langage: ",bg="red").place(x=60,y=80)
entry_3 = Entry(root, textvariable=destination).place(x=250,y=80)
#input data

def translate_this():
	translations = translator.translate([message.get()],dest=destination.get(),src=source.get())
	for translation in translations:
		origin_translation = translation.origin
		text_translation = translation.text
	label4 = Label(root,text=origin_translation,bg="red").place(x=200,y=170)
	label5 = Label(root,text=text_translation,bg="green").place(x=200,y=210)

#function to translate the data
def exit():
	root.destroy()

#function like sys.exit()

def my_instagram():
	my_insta = " firefox https://instagram.com/77_r3q "
	os.system(my_insta)

#function for follow me in Instagram ! :D 

b1 = Button(root,text="Translate !",command=translate_this).place(x=12,y=356)
buttonname = Button(root,text="Made By 77_r3q",command=my_instagram).place(x=200,y=356)
b2 = Button(root,text="Exit",command=exit).place(x=435,y=356)


root.mainloop()
