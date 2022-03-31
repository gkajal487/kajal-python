#dublicats allowed object
import time
l6=eval(input("enter list data type: "))
print(l6)
print()
print(type(l6))
print()
print("fetching the data from the list")
print()
for y in l6:
    time.sleep(1)
    print(y)
    time.sleep(2)
print("end of an application")

#example2
import time
l6=eval(input("enter list data type: "))
print(l6)
print()
print(type(l6))
print()
print("fetching the data from the list")
print()
for y in l6:
    time.sleep(1)
    print(y)
    time.sleep(2)
print("end of an application")

#example3
#list is immutable
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
l1[4]=1000
l1[4]=1500
print()
time.sleep(2)
print("end of an application")