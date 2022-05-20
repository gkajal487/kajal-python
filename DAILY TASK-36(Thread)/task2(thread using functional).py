import time
from threading import*
def k_gupta():
    for x in range (10):
        time.sleep(2)
        print("this is thred using functional aproach")
t=Thread(target=k_gupta)
t.start()
for x in range(7):
    print("this is the anather thread")
print()
time.sleep(2)
print("end of an application")
