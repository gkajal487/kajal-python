import time
l1=int(input("enter the value of l1:"))
l2=int(input("enter the value of l2:"))
print('using ternary operator')
print()
res1=l1 if l2<l1 else l1
print('the minimum no is:')
print(res1)
print(type(res1))
print()
time.sleep(2)
print('end of an application')
