import time
class product:
    def  __init__(self,pname,price,company):
        self.pname="laptop"
        self.price=20000
        self.price="samsung"
    def m1(self):
        print("....product information....")
        print("product name is:",self.pname)
        print("product price is:",self.price)
        print("product company is",self.company)
        print()
a=product()
a.m1()
print()
time.sleep(2)
print("end of an application")
