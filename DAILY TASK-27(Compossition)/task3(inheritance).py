import time
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def m1(self):
        print(self.name,self.age)
a=person('kajal',25)
a.m1()
print()
time.sleep(2)
print("end of an an application")


