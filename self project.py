import tkinter as tk
from function import *

def run():
    y = int(entry0.get())
    boom(y,stocks,target, trigger ,stoploss)

def add():
    stocks.append(s1.get())
    trigger.append(s2.get())
    target.append(s3.get())
    stoploss.append(s4.get())
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")

input = tk.Tk()

stocks = []
trigger = []
target = []
stoploss = []

s1 = tk.StringVar()
s2 = tk.IntVar()
s3 = tk.IntVar()
s4 = tk.IntVar()
tk.Label(input, text = "enter the no. of stocks").place(x = 5, y = 0)
entry0 = tk.Entry(input)
entry0.place(x = 250, y = 0)
tk.Label(input, text = "enter the name of the stock").place(x =5 , y =50 )
entry1 = tk.Entry(input, textvariable = s1)
entry1.place(x = 250, y = 50)
tk.Label(input, text = "enter the trigger ").place(x = 5, y = 85)
entry2 = tk.Entry(input, textvariable = s2)
entry2.place(x = 250, y = 85)
tk.Label(input, text = "enter the target ").place(x = 5, y = 115 )
entry3 = tk.Entry(input,textvariable = s3)
entry3.place(x = 250, y = 115)
tk.Label(input, text = "enter the stoploss ").place(x = 5, y = 145 )
entry4 = tk.Entry(input, textvariable = s4)
entry4.place( x=250, y = 145)
tk.Button(input, text='Quit', command=input.quit).place(x = 5, y = 200)
tk.Button(input, text='enter next stock', command=add).place ( x = 50, y = 200)
tk.Button(input, text='run the alerts', command=run).place( x= 200, y = 200)


input.mainloop()


