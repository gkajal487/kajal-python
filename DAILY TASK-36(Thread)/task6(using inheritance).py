import time
from threading import*
class kajal_gupta(Thread):
   def m1(self):
     for x in range (4):
        time.sleep(2)
        print("this kajal")
t=kajal_gupta()
t.start()
for y in range(4):
    time.sleep(1)
    print("this is annu")
print()
time.sleep(2)
print("end of an application")
