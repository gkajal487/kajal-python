import time 
import re 
str1=input("Enter the pattern:")
d1=re.match(str1,"Django")
if(d1!=None):
    print(str1,":Pattern is matched")
else:
    print(str1,":Pattern is not matched")
print()
time.sleep(2)
print("End of an application ...")
