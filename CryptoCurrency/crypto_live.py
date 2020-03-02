import tkinter
from tkinter import *
import requests
from requests import get
#import libraries 

API = "https://api.coinmarketcap.com/v1/ticker/"
#API for CryptoCurrency

root = Tk()

root.title(" CryptoCurrency PriceLive ")
root.geometry("500x450")
root.configure(background='black')

label2 = Label(root,text="Enter Crypto Currency: ",bg="yellow").pack()


name_currency = StringVar()
entry_1 = Entry(root, textvariable=name_currency).pack()


def jsonapi():
	reponse = get(API+name_currency.get())
	reponse_json = reponse.json()
	a2 = float(reponse_json[0]['price_usd'])
	label3 = Label(root, text=a2, bg="yellow").pack()
	label4 = Label(root,text="$",bg="red").pack()
#function to get the price of cryptocurrency

b1 = Button(root, text="Go Watch Price !",bg="yellow",command=jsonapi).place(x=180,y=330)
label5 = Label(root, text="API: https://api.coinmarketcap.com/v1/ticker/",bg="purple").place(x=107,y=380)

liste = Listbox(root,bg="red",width="32")
liste.insert(1, "Bitcoin")
liste.insert(2, "Ethereum")
liste.insert(3, "XRP")
liste.insert(4, "Bitcoin Cash [id: bitcoin-cash]")
liste.insert(5, "Litecoin")
liste.insert(6, "Crypto.com Coin [id: crypto-com-coin]")
liste.insert(7, "Cosmos [id: cosmos]")
liste.insert(8, "HedgeTrade [id: hedgetrade]")

#List of Crypto Currency

liste.pack()

root.mainloop()

#Made By 77_r3q
