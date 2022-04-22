import time
class my_cast:
    def __init__(self):
        print("this is constructor")
    def m1():
        print("this is the instance")
    @classmethod
    def m2():
        print("this is classmethod")
    @staticmethod
    def m3():
        print("this is staticmethod")
    print()
a=my_cast()
a.m1()
print()
a.m2()
print()
a.m3()
print()
print()
time.sleep()
print("end of an application")