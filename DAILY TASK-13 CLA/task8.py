import time
from sys import argv
print(type(argv))
print()
sum=0
for b in argv[4:]:
    sum=sum+b
print('the sum of argument',sum)
time.sleep(2)
print('end of an application')