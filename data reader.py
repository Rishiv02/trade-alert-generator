import pandas as pd

df = pd.read_excel(r'/Users/rishikeshvaidya/Desktop/nifty500.xlsx', engine="openpyxl")
l=[]
val = input("give the stock name: ")
l.append(val)
a = df.Symbol[df.Symbol == l[0]].index
u = df.loc[a[0]].iat[2]
l.append(u)
url= l[1]
