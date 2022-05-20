import time
n=5
fact=1
sum=0
for i in range(1,n+1):
    fact=fact*i
    num=map(int, str(fact))
for i in num:
    sum=sum+i
print("Sum of digits of ",n," factorial is:",sum)
print()
time.sleep(2)
print("end of an application")