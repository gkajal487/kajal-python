import time
try:
    a=int(input("enter the value of a"))
    b=int(input("enter the value of b"))
    res=a//b
    print("this is the res",res)
except:
    print("this is the value error")
except ArithmeticError:
    print("this the arithmaticerrror")
except ZeroDivisionError:
    print("this is the zero division error")
print()
time.sleep(2)
print("end of an application")