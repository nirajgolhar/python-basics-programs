from tkinter import *

root=Tk()

operator=""

def press(num):
    global operator
    operator=operator+str(num)
    a.set(operator)
    
def clear():
    a.set("")

def equalsInput():
    global operator
    c=str(eval(operator))
    a.set(c)
    operator=""

a=StringVar()

e1=Entry(root,textvariable=a)
e1.grid(columnspan=4)


b1=Button(root,text='1',command=lambda :press('1'))
b1.grid(row=1,column=0)
b2=Button(root,text='2',command=lambda :press('2'))
b2.grid(row=1,column=1)
b3=Button(root,text='3',command=lambda :press('3'))
b3.grid(row=1,column=2)
b4=Button(root,text='4',command=lambda :press('4'))
b4.grid(row=1,column=3)




b5=Button(root,text='5',command=lambda :press('5'))
b5.grid(row=2,column=0)
b6=Button(root,text='6',command=lambda :press('6'))
b6.grid(row=2,column=1)
b7=Button(root,text='7',command=lambda :press('7'))
b7.grid(row=2,column=2)
b8=Button(root,text='8',command=lambda :press('8'))
b8.grid(row=2,column=3)


b9=Button(root,text='9',command=lambda :press('9'))
b9.grid(row=3,column=0)
b10=Button(root,text='0',command=lambda :press('0'))
b10.grid(row=3,column=1)
b11=Button(root,text='-',command=lambda :press('-'))
b11.grid(row=3,column=2)
b12=Button(root,text='+',command=lambda :press('+'))
b12.grid(row=3,column=3)

b13=Button(root,text='*',command=lambda :press('*'))
b13.grid(row=4,column=0)
b14=Button(root,text='/',command=lambda :press('/'))
b14.grid(row=4,column=0)
b15=Button(root,text='c',command=lambda :clear)
b15.grid(row=4,column=0)
b16=Button(root,text='=',command=equalsInput)
b16.grid(row=4,column=0)
                    
