import time 
class I_HUB:
    def __init__(self):
        print("This is constructor ...")
    def __del__(self):
        print("For cleanup activity for memory allocation")
t1=[I_HUB(),I_HUB(),I_HUB(),I_HUB(),I_HUB()]
del t1
print()
time.sleep(5)
print("End of an application ...")
