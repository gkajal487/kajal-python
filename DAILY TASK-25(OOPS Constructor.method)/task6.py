import time
class k_gupta:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def m1(self):
        print("Name is:",self.name)
        print("Age is:",self.age)
        
k1=k_gupta("kajal",25)
k1.m1()
print()
time.sleep(2)
print("end of an application")