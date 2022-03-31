import time
l1=[10,33,30,150,180,190]
l2=bytes(l1)
print()
print(type(l1))
print()
for x in l2:
    time.sleep(2)
    print(x)
time.sleep(2)
print("end of an application")