import time
l1=[233,133,41,22,13,14]
l2=bytearray(l1)
print()
print('before immutable')
print(*l1)
print(type(l1))
print()
print('after immutable')
print()
l2[1]=120
l2[2]=146
l2[3]=178
l2[4]=167
print()
print(*l2)
print(type(l2))
print()
time.sleep(2)
print('end of an application')
