import time 
try:
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    res1=a//b 
    print("The result is:",res1)
except ArithmeticError as e:
    print("There is an exception:",e)
print()
time.sleep(2)
print()
print("End of an application ...")
