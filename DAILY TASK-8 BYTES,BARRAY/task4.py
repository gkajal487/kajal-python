import time
l1=[100,200,250,78,67,56,90,123]
l2=bytes(l1)
print()
print(*l2)
print(type(l2))
print()
for x in l2:
   time.sleep(2)
   print(l2)
print('end of an application')
