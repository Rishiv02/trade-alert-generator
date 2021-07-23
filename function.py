

def boom(n,stock,tar,trg,sl):
    import requests
    from bs4 import BeautifulSoup
    import threading
    import tkinter as tk
    import pandas as pd

    df = pd.read_excel (r'/Users/rishikeshvaidya/Desktop/nifty500.xlsx', engine = "openpyxl")

    def reload(stockname, url, targ, trg, sl):
        page = requests.get(url)
        threading.Timer(15.0, reload).start()
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('div', {'class':"inprice1"})['rel']

        if int(targ) > int(sl):
            if int(table) > int(trg) :
                root = tk.Tk()
                lb = tk.Label(root, text = stockname + " is ready to buy, with target of : " + targ + " and stoploss of : "+ sl)
                lb.pack()
                root.mainloop()
                exit()
        else:
            if int(table) < int(trg):
                toor = tk.Tk()
                ll = tk.Label(toor, text = stockname + " is ready to sell, with target of : " + targ + " and stoploss of : " + sl)
                ll.pack()
                toor.mainloop()
                exit()

    def row_col(val):
        l = []
        df = pd.read_excel (r'/Users/rishikeshvaidya/Desktop/nifty500.xlsx', engine = "openpyxl")
        l.append(val)
        a = df.Symbol[df.Symbol == l[0]].index
        u = df.loc[a[0]].iat[2]
        l.append(u)
        return l[1]


    for i in range(0,n):
        x = stock[i]
        ta = tar[i]
        tr = trg[i]
        stl = sl[i]
        ur = row_col(x)
        reload(x, ur, ta, tr, stl)











