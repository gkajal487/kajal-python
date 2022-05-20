import time 
from threading import * 
class I_HUB:
    def m1(self):
        for x in range(5):
            time.sleep(1)
            print("B thread ...")
i1=I_HUB()
t1=Thread(target=i1.m1())
for x1 in range(5):
    time.sleep(1)
    print("A thread ...")
print()
time.sleep(2)
print("End of an application ...")

