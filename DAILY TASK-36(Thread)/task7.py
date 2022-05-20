import time
from threading import *
class k_gupta(Thread):
    def m1(self):
        for x in range(7):
            time.sleep(1)
            print("this is thread using inheritance approach ")
a=k_gupta()
a.start()
for y in range(7):
    time.sleep(1)
    print("this is the iheritance 2")
print()
time.sleep(2)
print("end of an application")