from Tkinter import *

top = Tk()
top.title("Main Window")

lb1 = Listbox(top)
lb1.insert(1,"python")

lb1.insert(2,"c")

lb1.pack()
top.mainloop()
