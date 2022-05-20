import time 
import task2
import pickle 
f=open("info1.txt","wb")
n=int(input("Enter the number of row:"))
for x in range(n):
    tno=int(input("Enter the tno:"))
    tname=input("Enter the tname:")
    arrtime=input("Enter the arrtime:")
    depttime=input("Enter the dettime:")
    date=input("Enter the date:")
    t1=task2.Train(tno,tname,arrtime,depttime,date)
    pickle.dump(t1,f)
print("Picklingis done ...")
print()
f.close()
time.sleep(2)
print("End of an application ...")

