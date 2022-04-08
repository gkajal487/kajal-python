import time
p1=input('enter the password:')
p2=input ("enter the confirm password:")
if(p1==12345 and p2==3456):
    print(p1,p2,'is valid password')
else:
    print(p1,p2,'is not valid password')
print()
time.sleep(2)
print('end of an application')    