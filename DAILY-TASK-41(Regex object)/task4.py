#Regex object for different domains
#.com , .in ,co.in,.net

#\w[A-Za-z0-9._]*@(gmail|yahoo|rediff|[a-z])([.]com|in|co.in|net)
import time 
import re 
email=input("Enter the email account:")
d1=re.fullmatch("\w[A-Za-z0-9._]*@(gmail|yahoo|rediff|[a-z]*)([.]com|[.]in|[.]co[.]in|[.]net)",email)
if(d1!=None):
    print(email,":It is valid email account")
else:
    print(email,":It is invalid email account")
print()
time.sleep(2)
print("End of an application ...")

