from re import A
import time
A=(input('enter the value of k:'))
b=(input('enter the value of r:'))
c=(input('enter the value of r2:'))
print()
print('using ternary operator')
res1=A if b>c else b 
print('the maximum two no,is:',res1)
print(type(res1))
print()
time.sleep(2)
print('end of an application')