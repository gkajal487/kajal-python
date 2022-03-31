import time 
a=int(input("Enter the value  of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value  of c:"))
d=int(input("Enter the value of d:"))
e=int(input("Enter the value of e:"))
res1=a>b>c<d>e 
print("The result with chaining operator is:",res1)
print()
print(type(res1))
print()
time.sleep(2)
print("End of an application ...")