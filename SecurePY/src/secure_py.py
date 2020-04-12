__author__ = "PyR3Q"
#https://pyr3q.github.io/
#instagram: @pyr3q

import tkinter
import os
from os import system as shell
from tkinter import *

root = Tk()
root.title("SecurePy")
root.geometry("400x250")
root.configure(background="black")

background_image = PhotoImage(file="/IMG/linux.png")
background = Label(root,image=background_image,bd=0).pack()
website = StringVar()

title = Label(root,text="SecurePy",fg="black",font=("Helvitica",16)).place(x=160,y=10)
website_label = Label(root,text="Website:",fg="black",font=("Times New Roman",14)).place(x=10,y=80)
website_entry = Entry(root,textvariable=website).place(x=85,y=82)

    
ip1 = shell("curl -X GET https://api.ipify.org > output.txt && clear")
with open("output.txt","r") as f:
    my_ip = f.readlines()
    f.close()
ip_label = Label(root,text=my_ip,fg="black").place(x=110,y=50)

def proxy_connexion():
    shell("proxychains firefox %s"%(website.get()))

def vpn_connexion_on():
    shell("anonsurf start")
    ip2 = shell("curl -X GET https://api.ipify.org > output.txt && clear")
    with open("output.txt","r") as p:
        my_ip2 = p.readlines()
        p.close()
    ip_label2 = Label(root,text=my_ip2,fg="black").place(x=110,y=50)

def vpn_connexion_off():
    shell("anonsurf stop")
    ip3 = shell("curl -X GET https://api.ipify.org > output.txt && clear")
    with open("output.txt","r") as r:
        my_ip3 = r.readlines()
        r.close()
    ip_label3 = Label(root,text=my_ip3,fg="black").place(x=110,y=50)

proxy_button = Button(root,text="Proxy Connexion",fg="black",command=proxy_connexion).place(x=10,y=115)
vpn_button_on = Button(root,text="VPN Connexion",fg="black",command=vpn_connexion_on).place(x=60,y=200)
vpn_button_off = Button(root,text="Stop VPN",fg="black",command=vpn_connexion_off).place(x=210,y=200)

root.mainloop()
