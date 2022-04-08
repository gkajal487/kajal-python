import time
t1=(x*x for x in range (20))
print(*t1)
print()
print(type(t1))
for c in t1:
    print(t1)
print()
time.sleep(2)
print("end of an application")



