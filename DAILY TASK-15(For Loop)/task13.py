import time 
l1=[10,20,30,40,50,60,10,20,30]
print("Before removing the duplicate objects:",l1)
res=[] 
for i in l1:
    if i not in res:
        res.append(i)
print("Our list is after removing duplicate objects:",res)
print()
time.sleep(2)
print("End of an application ...")