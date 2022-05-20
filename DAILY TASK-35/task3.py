import time
try:
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b"))
    res=a//b
    print("the res is ",res)
except(ArithmeticError,ZeroDivisionError,ValueError)as e:
    print("there is exption ",e)
print()
time.sleep(2)
print("end of an application")