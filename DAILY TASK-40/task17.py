import time 
import re 
d2=re.finditer("[.]","ABCabc_12345  @gmail.com")
for d3 in d2:
    print(d3.start(),"---",d3.end(),"---",d3.group())
print()
time.sleep(2)
print('End of an application ...')
