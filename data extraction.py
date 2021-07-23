import requests
import sys
from bs4 import BeautifulSoup
import threading
import tkinter as tk
price = []
stock = input("Enter the stock to trade")
url = "https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI"
def reload():
    page = requests.get(url)
    threading.Timer(15.0, reload).start()
    soup = BeautifulSoup(page.content, 'html.parser')
    table1 = soup.find('div', {'class':"inprice1"})['rel']
    price.append(table1)
    if table1 > "410" :
        root = tk.Tk()
        tk.Label(root, text = "Your Trade is ready").place(x = 5, y = 0)
        root.mainloop()
        sys.exit()


    else : print("00")

reload()








