from tkinter import *


root = Tk()
def copydata():
    x=a.get()
    y=b.get()
    z=x+y
    r.set(z)
    

a=IntVar()
b=IntVar()
r=IntVar()
s1=Label(root,text="Enter first number:")
s1.pack()

s2=Label(root,text="Enter sec number:")
s2.pack()

e1=Entry(root,textvariable =a)
e1.pack()
e2=Entry(root,textvariable =b)
e2.pack()



b1=Button(root,text="Addition",command=copydata)
b1.pack()

e3=Entry(root,textvariable =r)
e3.pack()

root.mainloop()
