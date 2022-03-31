import time
x1=1000
x2=2000
x3=3000
print()
print('using ternary operator')
print()
res1=x1+x2+x3
print()
print(res1)
print(type(res1))
print()
res2=x1*x2*x3
print(res2)
print(type(res2))
print()
res3=x1>x2>x3
print()
print(res3)
print(type(res3))
print()
res4=x1 if x1>x2 else x2<x3
print()
print(res4)
print(type(res4))
print()
time.sleep(2)
print('end of an application')