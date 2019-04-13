from Tkinter import *
import tkMessageBox
#Top is object of window
top = Tk()

#Code to add widgets will go here
def hellocallback():
    tkMessageBox.showinfo("Hello Python","Hello World")

#Button object is created
b = Button(top,text="Hello",command=hellocallback)

c = Canvas(top,bg="Orange",height=500,width=500)#Object created to create canvas

#Tuple data of coord
coord = 10,50,250,210 #Co-ordinates are passed
arc = c.create_arc(coord,start=0,extent=150,fill="red")#Arc created 
C = c.create_line(10,50,110,180)#Line created

p = c.create_polygon(100,100,100,250,400,250,400,100)#Polygon created
o = c.create_oval(150,150,200,200,fill="white")

filename = PhotoImage(file="mic.png")
image = c.create_image(50,50,ANCHOR=NE,image=filename)

b.pack()#Used to add on the window
c.pack()#Canvas to add on the window

top.mainloop() #