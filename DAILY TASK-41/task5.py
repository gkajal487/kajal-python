import time 
import re 
import urllib 
import urllib.request 
d1=["https://www.qualitythought.in/contact-us/"]
for x1 in d1:
    print("Searching for:",x1)
    u=urllib.request.urlopen(x1)
    data=u.read()
    number=re.findall("[a-z]{4}@[a-z]*[.]in",str(data),re.I)
    for obj1 in number:
        time.sleep(1)
        print(obj1)
print()
time.sleep(2)
print("End of an application ...")
