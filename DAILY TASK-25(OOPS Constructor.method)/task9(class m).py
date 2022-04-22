import time
class person:
    @classmethod
    def m2(self):
        print("this is the class method")
        print()
p1=person
p1.m2()
person.m2()
print()
time.sleep(2)
print("end of an application")
