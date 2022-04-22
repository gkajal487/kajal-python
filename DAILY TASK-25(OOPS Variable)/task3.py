import time
class I_HUB:
    company_name="IBM"
    def __init__(self,eid,ename,esal,design):
        self.eid=eid 
        self.ename=ename 
        self.esal=esal 
        self.design=design
    def m1(self):
        print("----Employee Details----")
        print("Employee_Id is:",self.eid)
        print("Employee_Name is:",self.ename)
        print("Employee_Salary is:",self.esal)
        print("Employee_Design is:",self.design)
i1=I_HUB(1001,"Mahesh",45000,"DAD")
i1.m1()
print("Company name is:",I_HUB.company_name)
print("------------------------------")
i2=I_HUB(1002,"Harish",54000,"Python developer")
i2.m1()
print("Company name is:",I_HUB.company_name)
print("------------------------------")
print()
i3=I_HUB(1003,"Mohan",60000,"FTPD")
i3.m1()
print("Company name is:",I_HUB.company_name)
print("------------------------------")
print()
i4=I_HUB(1004,"Ravi",50000,"Django developer")
i4.m1()
print("Company name is:",I_HUB.company_name)
print("------------------------------")
print()

time.sleep(2)
print('End of an application ...')