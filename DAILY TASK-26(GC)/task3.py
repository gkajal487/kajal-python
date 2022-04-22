import time 
class I_HUB:
    def __init__(self):
        print("This is constructor ...")
    def __del__(self):
        print("For cleanup activity for memory allocation")
t1=I_HUB()
t2=t1 
t3=t2 
t4=t3 
t5=t4
del t1
time.sleep(2)
print("t1 ref is gone object is there")
del t2
time.sleep(2)
print("t2 ref is gone object is there")
del t3
time.sleep(2)
print("t3 ref is gone object is there")
del t4
time.sleep(2)
print("t4 ref is gone object is there")
del t5
print()
print()
time.sleep(5)
print("End of an application ...")
