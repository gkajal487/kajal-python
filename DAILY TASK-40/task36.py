from ast import Str
import time
import re
Str=int(input('enter the mobile number:'))
d1=re.match(int,"+918210789352")
if(d1!=None):
    print(int,"this is indian mobile number")
else:
    print("this is not indian mobile number")
print()
time.sleep(2)
print("end of an application")