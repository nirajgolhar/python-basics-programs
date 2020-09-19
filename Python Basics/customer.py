class customer:
    def get(self):
        self.custid=int(input('enter customer id'))
        self.custname=input('Enter name')
        self.proname=input('Enter product name')
        self.proprice=int(input('Enter product price'))
    def display(self):
        print("customer id:",self.custid)
        print("customer name:",self.custname)
        print("product name:",self.proname)
        print("product price:",self.proprice)
c1=customer()
c1.get()
c1.display()

        
        
