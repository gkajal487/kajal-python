import time 
try:
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    res1=a//b 
    print("The result is:",res1)
except ArithmeticError:
    print("This is Arithmetic error")
except ZeroDivisionError:
    print("This is zero division error")
except ValueError:
    print("This is value error ")
print()
time.sleep(2)
print("End of an application ...")
