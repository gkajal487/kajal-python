#common differences b/w list, tuple, set
import time
l1=[2,4,6,8]
l2=(1,2,3,4)
l3={5,6,7,8}
print()
print(l1)
print(l2)
print(l3)
print()
print(type(l1))
print(type(l2))
print(type(l3))
print()
print(l1[2])
print(l1[3])
print(l1[4])
print()
for b in l1:
    print(b)
    time.sleep(2)
    print()
time.sleep(2)
print("end of an application")