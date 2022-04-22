import time
class k_gupta:
    def __init__(self,eid,ename,esal,design,company):
        self.eid=eid
        self.ename=ename
        self.esal=esal
        self.design=design
        self.company=company
    def m1(self):
            print("eid is:",self.eid)
            print("ename is:",self.ename)
            print("esal is:",self.esal)
            print("design is:",self.design)
            print("company is:",self.company)
            print()
k1=k_gupta(1001,"kajal","45000","jr.developer","tech mahindra")
k1.m1()
print()
time.sleep(2)
print("end of an application")
