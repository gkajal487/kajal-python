import time 
class I_HUB:
    company_name="Wiprotechnology"
    def __init__(self,eid,ename,esal,design):
        self.eid=eid 
        self.ename=ename 
        self.esal=esal 
        self.design=design 
    def m1(self):
        print("----Employee Information----")
        print("Eid is:",self.eid)
        print("Ename is:",self.ename)
        print("Esal is:",self.esal)
        print('Design is:',self.design)
i1=I_HUB(1001,"Rahul Reddy",36000,"DAD")
i1.m1()
print("Company name is:",I_HUB.company_name)
print()
time.sleep(2)
print('End of an application ...')

  