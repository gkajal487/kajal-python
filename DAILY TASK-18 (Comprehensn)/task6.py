import time
t1=(x*x for x in range(8) if x%8==0)
print(t1)
print(type(t1))
for d in t1:
    print(d)
print()
time.sleep(2)
print("end of an application")