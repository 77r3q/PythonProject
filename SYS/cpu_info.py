import os
from tkinter import *

cpuinfo = []
a = os.popen('lscpu ').readlines()
a = list(a)

for x,recs in enumerate(a):
	b = recs.replace(" ","")
	b = recs.split(':')
	b[1] = b[1].strip(" ")
	b[1] = b[1].replace('\n','')
	cpuinfo.insert(x,b)

root = Tk()
root.title("MyCPU Information")

for i in range(19):
	e = str(cpuinfo[i][0])
	d = str(cpuinfo[i][1])
	print(e,d)
	button1 = Button(root,text=e)
	button1.grid(row = i, column = 0, sticky = W, pady = 2)
	entry1 = Entry(root,width=40)
	entry1.insert(INSERT,d)
	entry1.grid(row = i, column = 0, sticky = W, pady = 2)
	button2 = Button(root, text="Close", command=root.quit, width=10)

root.mainloop()


#Only For Linux Users 
