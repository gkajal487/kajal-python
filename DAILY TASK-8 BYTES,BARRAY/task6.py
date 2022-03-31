import time
print()
print("...before immutable")
l1=[120,130,140,150,160]
l2=bytes(l1)
print(*l1)
print(type(l1))
print()
print("...after immutable...")
l2[1]=120
l2[2]=130
print(l2)
print()
time.sleep(2)
print('end of an application')

