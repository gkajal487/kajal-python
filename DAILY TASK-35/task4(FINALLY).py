import time
try:
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))
    res=10//2
    print("the result is",res)
finally:
    print("this is the finally")
print()
time.sleep(2)
print("end of an application")