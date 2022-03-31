import time
from sys import argv
print(type(argv))
sum=0 
for x in argv [1:]:
    print(x)
    sum=sum+1
print("the sum of argument:",sum)
print()
time.sleep(2)
print('end of n application')