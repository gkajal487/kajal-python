import time 
from random import *
print('----Random string object----')
l1_items=['Apple','Orange','Water millan','Banana','Graps']
for x in range(10):
    time.sleep(1)
    print(choice(l1_items))
print()
time.sleep(2)
print("End of an application ...")