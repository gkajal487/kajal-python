import time
try:
    a=int(input("enter the value a:"))
    b=int(input("enter the value b:"))
    res=a//b
    print("the res is",res)
except ZeroDivisionError:
    print("this is zero division error ")
except ArithmeticError:
    print("This is Arithmetic error")
except ValueError:
    print("This is value error ")
print()
time.sleep(2)
print("End of an application ...")


