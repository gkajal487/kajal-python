#using while loop in palindrom
import time
num = int(input("Enter a value:")) 
temp = num  
Rev = 0  
while(num > 0):  
    dig = num % 10  
    revrev = revrev * 10 + dig  
    numnum = num // 10  
if(temp == revrev):  
    print("This value is a palindrome number!")  
else:  
    print("This value is not a palindrome number!")
print()
time.sleep(2) 
print("end of an application") 
