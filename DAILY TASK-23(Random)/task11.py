import time 
from random import *
print("---Random even numbers----")
for x in range(10):
    time.sleep(1)
    print(randrange(0,10,2))
print()
print("---Random Odd number---")
for x1 in range(10):
    time.sleep(1)
    print(randrange(1,10,2))
print()
time.sleep(2)
print("End of an application ...")


