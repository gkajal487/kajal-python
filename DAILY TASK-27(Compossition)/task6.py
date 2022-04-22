import time
class father_class:
    def m1(Self):
        print("this is the father class")
class child_class1(father_class):
    def m2(self):
        print("this is the child one class")
class child_class2(father_class):
    def m3(self):
        print("this is the child two class")
class child_class3(father_class):
    def m3(self):
        print("this is the child three class")

a1=child_class1()
a1.m1()
a1.m2()
print()
a2=child_class2
a2.m1
a2.m3()
print()
a3=child_class3
a3.m1()
a3.m4()
print()
time.sleep(2)
print("end of the application")