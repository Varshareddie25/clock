from tkinter import *
from tkinter.ttk import *
from time import strftime
root =Tk()
root.title("cClock")
def time():
    string =strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)
label=Label(root,font=("ds-digital bold",80),background="white",foreground="black")
label.pack(anchor='center')
time()
mainloop()
