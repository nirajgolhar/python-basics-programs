class Reactangle :
    def get(self):
        self.length=int(input('enter length'))
        self.breath=int(input('enter breath'))
    def disp(self):
        print("length:",self.length)
        print("breath:",self.breath)

class Square:
    def get1(self):
        self.side=int(input('enter side of square:'))

    def disp1(self):
        print("side:",self.side)
class Shape(Reactangle,Square):
    def display(self):
        
        self.a=self.length*self.breath
        print(self.a)
        self.b=self.side*self.side
        print(self.b)
s1=Shape()
s1.get()
s1.get1()
s1.disp()
s1.disp1()
s1.display()
