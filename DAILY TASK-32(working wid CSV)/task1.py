import time
import csv
with open("data.csv","w",newline=" ")as f:
    d1=csv.reader(f)
    d1.writerow(["eid,esalry,ename,company:"])
    n=int(input("enter the value:"))
    for x in range:
        eid=int(input("enter the eid:"))
        esalry=float(input("enter the slary:"))
        ename=input("enter the ename") 
        company=input("enter the company:")
        d1.writerow(["eid,esalry,ename,company"])
        print("A csv file is created succesfully")
print()
time.sleep(2)
print("end of an application")
