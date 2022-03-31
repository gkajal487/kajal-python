import time 
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
max=a if a>b and a>c else b if b>c else c 
print("The maximum number of three of number is:",max)
print()
time.sleep(2)
print("End of an application ...")
