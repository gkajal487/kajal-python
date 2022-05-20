import time
import os
try:
    print("this is the try block")
    100//20
    os._exite((0))
except:
    print("this is the except block")
finally:
    print("this is the finally block")
print()
time.sleep(2)
print("end of an application")