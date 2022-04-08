import time
from tkinter import Y
s1={y*y for y in range(4) if y%4==0}
print(s1)
print()
print(type(s1))
print()
for a in s1:
    print(a)
print()
time.sleep(2)
print("end of an application")