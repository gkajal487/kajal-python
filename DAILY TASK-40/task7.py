import time
import re
d1=re.compile("[A-B]","kajal123@gmail.com")
d2=re.finditer("kajal123@gmail.com")
for d3 in d2:
    print(d3.start(),"---",d3.end(),"---",d3.group())
print()
time.sleep(2)
print("end of an application")