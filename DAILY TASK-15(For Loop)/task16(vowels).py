import time
c=0
str1=input("enter any str")
print(str1)
for x in str1:
    if x in ('aeiouAEIOU'):
        c+=1
print()
time.sleep()
print('end of an application')
