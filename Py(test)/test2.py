import time
n=10
fact=1
sum=0
for p in range(1,n+1):
    fact=fact*p
    Num=map(int,str(fact))
for i in Num:
    sum=sum+1
print("the given number is :",n)
print("the factorial of given number:",fact)
print()
time.sleep(2)
print("end of an application")
