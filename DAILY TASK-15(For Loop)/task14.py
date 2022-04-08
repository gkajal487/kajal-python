import time
c=0 
str1=input('Enter any string:')
print(str1)
for x in str1:
    if x in ('aeiouAEIOU'):
        c+=1 
        print(x)
print("Number of vowels are:",c)
print()
time.sleep(1)
print("End of an application ...")