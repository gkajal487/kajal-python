import time 
import re 
str1=input("Enter the pattern:")
d1=re.search('^a',str1)
if(d1!=None):
    print(str1,":Our pattern is starts with a")
else:
    print(str1,":Our pattern not starts with a")
print()
time.sleep(2)
print("End of an application ...")

