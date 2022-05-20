#[+][9]{1}[1]{1}-[6-9]\d{9}

import time 
import re
mobile_number=input("Enter the indian mobile number:")
d1=re.fullmatch("[+][9]{1}[1]{1}-[6-9]\d{9}",mobile_number)
if(d1!=None):
    print(mobile_number,":It is valid indian mobile number")
else:
    print(mobile_number,":It is invalid indian mobile number")
print()
time.sleep(2)
print("End of an application ...")
