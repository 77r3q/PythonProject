import requests
import tkinter
from tkinter import *
from requests import get


root = Tk()
root.title("IpTrace")
root.geometry("600x500")
root.configure(background="black")

API = "http://ip-api.com/json/"


ip_target = StringVar()

label1 = Label(root,text="Enter Target IP:",bg="yellow").pack()
entry_1 = Entry(root,textvariable=ip_target).pack()

def ip_trace():
	reponse = requests.get(API+ip_target.get())
	reponse_json = reponse.json()
	query = reponse_json['query']
	statuts = reponse_json['status']
	country = reponse_json['country']
	region = reponse_json['region']
	city = reponse_json['city']
	zipcode = reponse_json['zip']
	latitude = reponse_json['lat']
	longitude = reponse_json['lon']
	regioname = reponse_json['regionName']
	isp = reponse_json['isp']
	label_query = Label(root,text="[IP_Address] :",bg="red").place(x=120,y=80)
	label1 = Label(root,text=query,bg="yellow").place(x=230,y=80)
	label_query = Label(root,text="[Statuts] :",bg="red").place(x=120,y=120)
	label2 = Label(root,text=statuts,bg="yellow").place(x=230,y=120)
	label_country = Label(root,text="[Country] :",bg="red").place(x=120,y=160)
	label3 = Label(root,text=country,bg="yellow").place(x=230,y=160)
	label_reg = Label(root,text="[Region] :",bg="red").place(x=120,y=200)
	label4 = Label(root,text=region,bg="yellow").place(x=230,y=200)
	label_city_name = Label(root,text="[City Name] :",bg="red").place(x=120,y=240)
	label_city = Label(root,text=city,bg="yellow").place(x=230,y=240)
	label_regname = Label(root,text="[RegionName] :",bg="red").place(x=120,y=280)
	label_regionname = Label(root,text=regioname,bg="yellow").place(x=230,y=280)
	label_zipcode = Label(root,text="[ZipCode] :",bg="red").place(x=120,y=320)
	label5 = Label(root,text=zipcode,bg="yellow").place(x=230,y=320)
	label6 = Label(root,text="Latitude + Longitude: %s;%s"%(latitude,longitude),bg="yellow").place(x=120,y=360)
	label_isp = Label(root,text="[ISP] :",bg="red").place(x=120,y=400)
	label7 = Label(root,text=isp,bg="yellow").place(x=230,y=400)

def close_app():
	root.destroy()

b1 = Button(root,text="Trace!",command=ip_trace).pack()
b2 = Button(root,text="Exit",command=close_app).place(x=270,y=460)

root.mainloop()
