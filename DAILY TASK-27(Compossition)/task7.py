import time
class Parent1_Class:
    def m1(self):
        print("Parent one class ...")
class Parent2_class:
    def m2(self):
        print("Parent two class ...")
class Parent3_class:
    def m3(self):
        print("Parent3 class ...")
class Parent4_class:
    def m4(self):
        print("Parent four class ...")
class Child1_class(Parent1_Class,Parent2_class,Parent3_class,Parent4_class):
    def m5(self):
        print("Child one class ...")
c1=Child1_class()
c1.m1()
c1.m2()
c1.m3()
c1.m4()
c1.m5()
print()
time.sleep(2)
print("end of an application")