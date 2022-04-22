import time 
class k_gupta:
    company_name="cisco"
    def __init__(self,ename,eid,esal,design):
        self.ename=ename
        self.eid=eid
        self.esal=esal
        self.design=design
    def m1(self):
        print("...employee information...")
        print("ename is:",self.ename)
        print("eid is:",self.eid)
        print("esal is:",self.esal)
        print("design is:",self.design)
        print()
        print("...........................")
a=k_gupta("kajal",1234,35000,"python devpoloper")
a.m1()
print("company name is:",k_gupta.company_name)
time.sleep(2)
print("end of an application")
