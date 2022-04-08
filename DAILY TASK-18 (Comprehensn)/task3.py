import time
l1=[x*x for x in range (8) if x%4==0]
print(l1)
print(type(l1))
print()
for x in l1:
    print(x)
print()
time.sleep()
print("end of an application")