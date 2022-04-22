import time
class A_class:
    def m1(self):
        print("A class implementation")
class B_class(A_class):
    def m2(self):
        print("B class implementation")
class C_class(B_class):
    def m3(self):
        print("this is the implementation")
class D_class(C_class):
    def m4(self):
        print("this is the implemention")
    def m1(self):
        A_class.m1(self)
        print()
        super(B_class,self).m1()
d=D_class()
d.m1()
print()
time.sleep(2)
print("end of an application")

