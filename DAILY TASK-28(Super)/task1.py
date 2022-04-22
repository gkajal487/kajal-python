import time
class techer:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def m1(self):
        print("the name is:",self.name)
        print("the age is:",self.age)
class person(class techer):
    def __init__(self,name,age,sub,sal):
        super(). __init__(name,age,sub,sal)
        self.name=name
        self.age=age
        self.sub=sub
        self.sal=sal
    def m2(self):
        print("the name is:",self.name)
        print("the age is :",self.age)
        print("the sub is",self.sub)
        print("the sub is:",self.sub)
        print("the sal is:",self.sal)
class trainer:
    def __init__(self ,name,sal,id):
        super().__init__(name,sal,id)
        self.name=name
        self.sal=name
        self.id=id
    def m3(self):
        print("the name is:",self.name)
        print("the sal is:",self.sal)
        print("the id is:",self.id)
class Employee_Class:
    def __init__(self,name,age,eid,esal,design,company):
        super().__init__(name,age)
        self.eid=eid 
        self.esal=esal 
        self.design=design 
        self.company=company 
    def m2(self):
        super().m1()
        print("Eid is:",self.eid)
        print("Esal is:",self.esal)
        print("Design is:",self.design)
        print("Company is:",self.company)
        e1=Employee_Class("Mahesh",23,1001,45000,"DAD","TM")
e1=Employee_Class("Mahesh",23,1001,45000,"DAD","TM")
e1.m2()
print()
s1=trainer("Ajay",21,101,"Python",76)
s1.m3()
print()
t1= Employee_Class("John",31,85000,"Django")
t1.m4()
print()
time.sleep(2)
print("End of an application ...")

