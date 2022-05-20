import time 
import csv 
f=open("data1.csv","r")
d1=csv.reader(f)
d2=list(d1)
for a in d2:
    for b in a:
        print(b,end=" ")
    print()
print()
time.sleep(2)
print("End of an application ...")

