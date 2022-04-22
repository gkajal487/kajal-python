
import time
from functools import*

total_money=[70,29,30,60,80]
l1=reduce(lambda x,y:x+y,total_money)
print("add the all money from the list:",l1)
print()
time.sleep(2)
print("end of an application")