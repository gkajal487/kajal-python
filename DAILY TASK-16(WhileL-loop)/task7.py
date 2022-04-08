import time
l1=[10,20,30,40]
print(l1)
print()
i=0
sum=0
while(i<len(l1)):
    sum=sum+l1[i]
    i+=1
print("sum of the list",sum)
time.sleep(2)
print("end of an application")