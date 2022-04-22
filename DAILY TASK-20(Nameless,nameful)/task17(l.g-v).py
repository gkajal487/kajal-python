import time
from tkinter import Y
Y= 5

def case_1():
    x = 10
    print("local x:", x)


case_1()
print("global x:", Y)
print()
time.sleep(2)
