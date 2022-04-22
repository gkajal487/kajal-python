import time
class person:
    def m1(self):
        print("this is the parent class")
class student1(person):
    def m2(self):
        print("this is the python class one claas")
class student2(student1):
    def m3(self):
        print("this is the python class two class")
class student3(student2):
    def m4(self):
        print("this is the python class three class")
a=student3()
a.m1()
a.m2()
a.m3()
print()
time.sleep(2)
print("end of an application")
