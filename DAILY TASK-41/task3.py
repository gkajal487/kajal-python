import time 
import re 
import urllib 
import urllib.request 
d1=["https://www.rediff.com"]
for x1 in d1:
    print("Searching for:",x1)
    u=urllib.request.urlopen(x1)
    data=u.read()
    print(data)
    print()
    print(type(data))
    #title=re.findall("<title>.*</title>",str(data),re.I)
    #print(title[0])
print()
time.sleep(2)
print("End of an application ...")