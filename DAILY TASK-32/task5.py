import time 
import task1 
import pickle 
f=open("info1.txt","rb")
while(True):
    try:
        obj1=pickle.load(f)
        obj1.m1()
        print()
    except EOFError as e:
        print("There is excpetion:",e)
        break 
print()
time.sleep(2)
print("End of an application")


