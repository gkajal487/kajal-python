from distutils.log import error
import time
try:
    a=int(input("enter a value of a:"))
    b=int(input("enter a value of b:"))
    res=100//5
    print("the res is:",res)
except:
    print("this is value error")
except ArithmeticError:
    print("this is the arimatic error")
except ZeroDivisionError:
    print("this is the zero division error")
print()
time.sleep(2)
print("end of an application")

