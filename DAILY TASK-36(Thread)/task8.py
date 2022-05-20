import time 
from threading import * 
class MyThread(Thread):
    def run(self):
        for x in range(7):
            time.sleep(1)
            print("Advance Python")
t1=MyThread()
t1.start()
for x1 in range(7):
    time.sleep(1)
    print("Core Python")
print()
time.sleep(1)
print("End of an application ...")
