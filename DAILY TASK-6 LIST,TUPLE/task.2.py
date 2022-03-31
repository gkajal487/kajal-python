#list data type before mutable or after mutable
import time
l1=[20,30,40,50]
print(l1)
print()
print("before mutuble")
print()
print(l1)
print(type(l1))
print()
print("after mutuble")
l1[0]=100
l1[1]=500
l1[2]=1000
l1[3]=1500
print()
time.sleep(2)
print("end of an application")