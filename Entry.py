
from Tkinter import *
top = Tk()

top.title("The Main Window")
top.geometry("500x500")
top.resizable(0,0)

def print_content():
    global data
    content = data.get()
    print "Sqaure is ",content*content

data = IntVar()

Label(top,text="Input:").grid(row=0,sticky=W)
Entry (top,textvariable=data).grid(row=1,column=1)
b1 = Button(top,text="continue",command=print_content)
b1.grid(row=2,column=1)

top.mainloop()