from Tkinter import *

top = Tk()
def hellocallback():
    messagebox.showinfo("Say Hello", "Hello World")

def display():
    print "clicked video"


checkVar1 = IntVar()
checkVar2 = IntVar()

C1 = Checkbutton(top,text="Button",variable=checkVar1,onvalue=1,offvalue=0,height=5,width=20,command=hellocallback)

C2 = Checkbutton(top,text="Video",variable=checkVar2,onvalue=1,offvalue=0,height=5,width=20,command=display)

print checkVar1
print checkVar2

C1.pack()
C2.pack()
top.mainloop()