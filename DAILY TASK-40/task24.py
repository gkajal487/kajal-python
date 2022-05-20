import time 
import re 
d2=re.finditer("a{2,4}","abcdaarrrttttuuuqqaaahhaaaa")
for d3 in d2:
    print(d3.start(),"---",d3.end(),"---",d3.group())
print()
time.sleep(2)
print('End of an application ...')
