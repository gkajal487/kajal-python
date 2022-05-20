import time 
import csv 
with open("data1.csv","w",newline="") as f:
    d1=csv.writer(f)
    d1.writerow(["Eid","Ename","Esal","Design","Company"])
    n=int(input("Enter the number of rows:"))
    for x in range(n):
        eid=int(input("Enter the eid:"))
        ename=input("Enter the ename:")
        esal=float(input("Enter the esal:"))
        design=input("Enter the design:")
        company=input("Enter the company:")
        d1.writerow([eid,ename,esal,design,company])
    print("A CSV file is created successfully")
print()
time.sleep(2)
print("End of an application ...")
