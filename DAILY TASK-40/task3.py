import time
import re
d1=re.compile("BC")
d2=d1.finditer("AAABBBCCTTYY")
for d3 in d2:
    print(d3.start(),"---",d3.end(),"---",d3.group())
print()
time.sleep(2)
print('end of an application')