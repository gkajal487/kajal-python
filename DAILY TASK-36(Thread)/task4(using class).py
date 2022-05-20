import time
from threading import*
from typing_extensions import Self
class k_gupta:
    def m1(self):
        for x in range(5):
            time.sleep(1)
            print("this is django")
a=k_gupta()
a=Thread(target=k_gupta)
for x in range (9):
    time.sleep(1)
    print("this is not django")
print()
time.sleep(2)
print("end of an application")