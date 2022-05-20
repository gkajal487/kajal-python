import time
import os
try:
    print("this is the try block")
    os._exite((800))
except:
    print('this is the except block')
finally:
    print("this is the finally block")
print()
time.sleep(2)
print("end of an application")