class liabrary :
    def get(self):
        self.Lid=int(input('enter id'))
        self.Lname=input('enter name')
    def display(self):
        print("liabrary id",self.Lid)
        print("Liabrary name",self.Lname)

class Book(liabrary) :
    def get1(self):
        self.bid=int(input('enter book id'))
        self.bname=input('enter book name')
        self.author=input('enter book author')
    def display1(self):
        print("Book id:",self.bid)
        print("book name:",self.bname)
        print("book author:",self.author)
        
  
class Reader(Book):
    def get2(self):
        self.rid=int(input('enter reader id'))
        self.rname=input('enter reader name')
        self.address=input('enter your address')
    def display2(self):
        print("reader id:",self.rid)
        print("reader name:",self.rname)
        print("reader address:",self.address)

r=Reader()
r.get()
r.get1()
r.get2()
r.display()
r.display1()
r.display2()

    
