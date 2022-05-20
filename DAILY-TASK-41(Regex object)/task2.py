#abc@gmail.com

#\w[A-Za-z0-9._]*@gmail[.]com

import time 
import re 
gmail=input("Enter the gmail account:")
d1=re.fullmatch("\w[A-Za-z0-9._]*@gmail[.]com",gmail)
if(d1!=None):
    print(gmail,":It is valid gmail account")
else:
    print(gmail,":It is invalid gmail account")
print()
time.sleep(2)
print("End of an application ...")
