import time
class A:
    def __init__(self, a):
        self.a = a
    def __add__(self, o):
        return self.a + o.a
ob1 = A(1)
ob2 = A(2)
ob3 = A("kajal")
ob4 = A("gupta")
 
print(ob1 + ob2)
print(ob3 + ob4)
print()
time.sleep(2)
print("end of an application")