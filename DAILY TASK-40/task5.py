import time 
import re 
count=0
d1=re.compile("AB")
d2=re.finditer("AB","ABEEERRRRABTTTAB")
for d3 in d2:
    count+=1
    print(d3.start(),"---",d3.end(),"---",d3.group())
print("AB pattern is present in Target string is:",count)
print()
time.sleep(2)
print('End of an application ...')

