a=input("Enter your  name")
b=int(input("Enter your  age"))
c=input("Enter your  address")
d=input("Enter your  city")
sub1=int(input("Enter sub1 marks:"))
sub2=int(input("Enter sub2 marks:"))
sub3=int(input("Enter sub3 marks:"))

f=open("kajal.txt","w")

f.write(a)
f.write(str(b))
f.write(c)
f.write(d)
f.write(str(sub1))
f.write(str(sub2))
f.write(str(sub3))

f.close()




