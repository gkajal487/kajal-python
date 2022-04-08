import time
p1=input('enter the password')
p2=input('enter the confirm password')
if (p1==p2):
    print(p1,p2,'password is valid :')
else:
    print(p1,p2,'password is not valid:')
print()
time.sleep(2)
print('end of an application')