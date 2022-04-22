import time
class my_type:
    @staticmethod
    def m3(a,b):
       print("the mul is:",a*b)
       print()
a=my_type
a.m3(2,3)
print()
my_type.m3(2,8)
print()
time.sleep(2)
print("end of an application")