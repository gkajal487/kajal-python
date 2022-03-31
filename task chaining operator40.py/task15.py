#LOGICALOPERATOR #AND
import time
fname=(input('enter the name:'))
lname=(input('enter the last name:'))
p1=(input('enter the password:'))
p2=(input('enter the confirm password:'))
username=(input('enter username:'))
email=(input('enter the email adderess:'))
if ((fname=="anu" and lname=="gupta")) or (p1=="anu@100" or p2=="anu@@100" or username=="ganu" or email=="ganu487"):
   print('fname:',fname)
   print('lname:',lname)
   print('p1=:',p1)
   print('p2:',p2)
   print('username:',username)
   print('email',email)
   print()
else:
    ("dear user please inter your fname,lname,p1,p2")
    print()
time.sleep(2)
print('end of an application')