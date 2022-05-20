import time
import re
str=input("enter the pattern")
d2=re.search(str,"software",re.IGNORECASE)
if(d1!=None):
    print(str,"pattern is matched")
else:
    (str,"pattern is not matched")
print()
time.sleep(2)
print("end of an application")