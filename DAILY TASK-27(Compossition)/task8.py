import time 
class Parent1_Class:pass
class Parent2_class:pass
class Parent3_class:
    def m1(self):
        print("Parent3 class ...")
class Parent4_class:
    def m1(self):
        print("Parent four class ...")
class Child1_class(Parent1_Class,Parent2_class,Parent3_class,Parent4_class):pass
 
c1=Child1_class()
c1.m1()

print()
time.sleep(2)
print("end of an application")
