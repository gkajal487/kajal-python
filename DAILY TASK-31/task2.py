import time
from abc import*
class test1(ABC):
    def m1(self):
        pass
    def m2(self):
        pass
    def m3(self):
        pass
class test2(test1):
    def m1(self):
        print("this is the m1 service")
    def m2(self):
        print("this is m2 service")
class test3(test2):
    def m3(self):
        print("this is the m3 service")
t1=test3()
t1.m1()
t1.m2()
t1.m3()
print()
time.sleep(2)
print("end of an application")

