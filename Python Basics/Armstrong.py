num=int(input("Enter a number:"))
sum=0
temp=num
while temp>0:
 a=temp % 10
 sum+= a**3
 temp//=10

if num==sum:
        print(num,"is not an Armstrong number")
else:
        print(num,"is an Armstrong number")
