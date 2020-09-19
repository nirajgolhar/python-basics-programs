from tkinter import *
from tkinter import messagebox

import pymysql

con=pymysql.connect("localhost",'root','root','college')
cur=con.cursor()
root=Tk()
def save():
    sql="insert into student values(%d,'%s','%s','%d')" %(a.get(),b.get(),c.get(),d.get())
    cur.execute(sql)
    con.commit()
    messagebox.showinfo('student Data','data saved!!!!!!!!')

def edit():
    sql="select * from student where sid=%d"%(a.get())
    cur.execute(sql)
    row=cur.fetchall()
    for t in row:
        b.set(t[1])
        c.set(t[2])
        d.set(t[3])
        

def update():
    sql="update student set name ='%s' , course='%s', fees=%d where sid=%d"%(b.get(),c.get(),d.get(),a.get())
    cur.execute(sql)
    con.commit()
    messagebox.showinfo('student Data','updated !!!!!!!!')

def delete():
    sql="delete from student where sid=%d "%(a.get())
    cur.execute(sql)
    con.commit()
    messagebox.showinfo('student Data','delete !!!!!!!!')

def clear():
    a.set("")
    b.set("")
    c.set("")
    d.set("")
        

a=IntVar()
b=StringVar()
c=StringVar()
d=IntVar()


s1=Label(root,text="ID:")
s1.grid(row=0,column=0)

e1=Entry(root,textvariable=a)
e1.grid(row=0,column=1)

s2=Label(root,text="Name:")
s2.grid(row=1,column=0)

e2=Entry(root,textvariable=b)
e2.grid(row=1,column=1)

s3=Label(root,text="course:")
s3.grid(row=2,column=0)

e3=Entry(root,textvariable=c)









































e3.grid(row=2,column=1)

s4=Label(root,text="Fees:")
s4.grid(row=3,column=0)

e4=Entry(root,textvariable=d)
e4.grid(row=3,column=1)

b1=Button(root,text='Save',command=save)
b1.grid(row=4,column=0)

b2=Button(root,text='edit',command=edit)
b2.grid(row=0,column=2)

b3=Button(root,text='update',command=update)
b3.grid(row=4,column=1)

b4=Button(root,text='delete',command=delete)
b4.grid(row=4,column=2)

b5=Button(root,text='clear',command=clear)
b5.grid(row=4,column=3)


root.mainloop()
