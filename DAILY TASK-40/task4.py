import time 
import re
c=0
d1=re.compile("CD")
d2=d1.finditer("AAeeqquurrjbhdbhbdn")
for d3 in d2:
    c+=1
    print(d3.start(),"---",d3.end(),"---",d3.group())
    print("AB pattern is the target string is:",c)
print()
time.sleep(2)
print("end of an application")