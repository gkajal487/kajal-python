import time 
import json 
with open("tool1.txt","r") as f:
    obj1=json.load(f)
    print(obj1)
    print()
    for x,y in obj1.items():
        print(x,"---",y)
print()
print("Object deserialization is done  ...")
print()
time.sleep(2)
print("End of an application ...")

 
