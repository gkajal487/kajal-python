import time
from abc import *
class k_gupta(ABC):
    @abstractclassmethod
    def m1(self):
     pass
a=k_gupta()
a.m1()
print()
time.sleep(2)
print("end of an application")