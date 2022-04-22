from distutils.log import info
import time
class k_gupta:
    def __init__(self):
        print("this is the constructor")
    def m1(self):
        print('this is the instance')
    @classmethod
    def m2():
        print("this the class method")
    @staticmethod
    def m3():
        print("this is the staticmethod")
class person(k_gupta):
    def __init__(self):
        super(). __init__()
        super().m1()
        super().m2()
        super().m3()
a=person
a=info()
print()
time.sleep(2)
print("end of an application")