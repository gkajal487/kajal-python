import time
c=0
str1=input("enter the any str1")
for x in str1: 
   if x in("aeiouAEIOU"):
       c+=1
       print(x)
       print("number are vowels are:",c)
print()
time.sleep(2)
print("end of an application")