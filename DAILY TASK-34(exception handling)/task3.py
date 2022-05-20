import time
try:
    a=int(input("enter the value a:"))
    b=int(input("enter the value b:"))
    res=a//b
    print('the res is', res)
except BaseException as e:
    print("the exception is",e)
print()
time.sleep(2)
print("end of an application")
    



