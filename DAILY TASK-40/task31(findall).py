import time 
import re 
d1=re.findall("\d","Rahul45678@gmail.com")
print(d1)
print()
print(type(d1))
for obj1 in d1:
    time.sleep(1)
    print(obj1)
print()
time.sleep(2)
print("End of an application ..")