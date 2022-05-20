import time
from abc import *
class Vehicle:
    @abstractmethod
    def m1(Self):
        pass
q1=Vehicle()
q1.m1()
print()
time.sleep(2)
print("end of an application")