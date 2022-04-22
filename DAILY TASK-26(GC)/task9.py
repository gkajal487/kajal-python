#Name of the employee is:Rahul Reddy
#Date of birth is:19/7/1995
import time 
class Employees:
    def __init__(self):
        self.name="Rahul Reddy"
        self.dob=self.DOB() 
    def m1(self):
        print("Name of the employee is:",self.name)
        self.dob.m2()
    class DOB:
        def __init__(self):
            self.day=19
            self.month=7
            self.year=1995 
        def m2(self):
            print("Date of birth is:{}/{}/{}".format(self.day,self.month,self.year))
e1=Employees()
e1.m1()
print()
time.sleep(2)
print("End of an application ...")

