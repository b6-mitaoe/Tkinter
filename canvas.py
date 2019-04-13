
from Tkinter import *

top = Tk()
C = Canvas(top,height=500,width=800)
filename = PhotoImage(file = "y.png")
image = C.create_image(50,50,anchor=NW,image=filename)

C.pack()

top.mainloop()
