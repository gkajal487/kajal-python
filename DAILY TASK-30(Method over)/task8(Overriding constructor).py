from os import pidfd_open
import time
class product:
    def __init__(self,pname,price):
        self.pname=pname
        self.price=price
    def __init__(self):
        print("pname is:",self.pname)
        print("price is:",self.price)
class mobile(product):
    def __init__(self,pname,price,pid,company):
        print("pid is:",self.pid)
        print("company is:",self.company)
    def __init__(self):
        super().__init__()
        self.pid=pid 
        self.company=company
    def m2(self):
        super().__init__
        print("pid is:",self.pid)
        print("company is:",self.company)
q1=mobile("samsung","AC",23000,1001,"samsung")
q1.m2()
print()
time.sleep(2)
print("end of an application")