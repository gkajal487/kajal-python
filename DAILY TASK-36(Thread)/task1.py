import time 
from threading import * 
print("Current thread name is:",current_thread().getName())
current_thread().setName("I-HUB")
print("Current thread name is:",current_thread().getName())
print()
time.sleep(2)
print("End of an application ...")

