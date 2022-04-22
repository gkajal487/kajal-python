from mimetypes import init
import time
class k_gupta:
    def __init__(self):
        print("this is the contructor")
    def m1(self):
        print("this the instructor")
    @classmethod
    def m2():
        print("this isthe classmethod")
    @staticmethod
    def m3():
        print("this is the static method")
class person(k_gupta):
    def __init__(self):
        super().__init__()
        super() .m1()
        super().m2()
        super().m3()
a=person()
print()
time.sleep(2)
print("end of an application")

