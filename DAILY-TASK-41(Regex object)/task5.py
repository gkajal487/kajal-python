#TS 123 EA4343 ---->Bike from TS

#[T]{1}[S]{1}[1-9]{3}[E]{1}[A]{1}[0-9]{4}

import time 
import re 
email=input("Enter the email account:")
d1=re.fullmatch([T]{1}[S]{1}[1-9]{3}[E]{1}[A]{1}[0-9]{4})
if(d1!=None):
    print(email,":It is valid email account")
else:
    print(email,":It is invalid email account")
print()
time.sleep(2)
print("End of an application ...")

