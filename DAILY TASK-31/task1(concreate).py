import time
from abc import*
class test1(ABC):
    @abstractmethod
    def m1(self):
        pass
    @classmethod
    def m2(self):
        pass
    @abstractmethod
    def m3(self):
        pass
class test2(test1):
    def m1 (self):
        print("this is m1 service")
    def m2(self):
        print("this is m2 serviece")
print()
time.sleep(2)
print("end of an application")
