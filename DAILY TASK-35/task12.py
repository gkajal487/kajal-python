import time 
import os
try:
    print("This is try block ...")
    os._exit("Fast API's")
    print(1200//0)
except:
    print("This is except block ...")
finally:
    print("This is finally block ...")
print()
time.sleep(2)
print("End of an application ...")

