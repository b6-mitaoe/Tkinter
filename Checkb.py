from Tkinter import *
import tkMessageBox

top = Tk()

def hello():
    tkMessageBox.showinfo("Hello Python","You Clicked Music")

def display(): 
    print "You Clicked Videos"

#Checkbox declaration
checkvar1 = IntVar()
checkvar2 = IntVar()

C1 = Checkbutton(top,text="Music",variable=checkvar1,onvalue=1,offvalue=0,height=5,width=20,command=hello)

C2 = Checkbutton(top,text="Video",variable=checkvar2,onvalue=1,offvalue=0,height=5,width=20,command=display)

print checkvar1
print checkvar2

L1 = Label(top,text="User Name",font="Times",fg="Green")
L1.pack()

E1 = Entry(top,bg="Yellow",fg="red")
E1.pack(side=RIGHT)
#Appding checkbox
C1.pack()
C2.pack()

top.mainloop()
