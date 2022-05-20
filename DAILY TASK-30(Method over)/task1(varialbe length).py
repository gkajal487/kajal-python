import time
class Qt_class:
    def m1(self,*x):
        for x1 in x:
         time.sleep(2)
         print(x1)
q1=Qt_class()
q1.m1("kajal","gupta","kajal1234","kajal@gmail.com")
q1.m1("annu","gupta","kajal1234","kajal@gmail.com")
print()
time.sleep(2)
print("end of an application")