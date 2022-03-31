import time
print('i am a smart worker') 
username=(input("Enter the username :"))
password=(input("Enter the password :"))
print()
if(username=="kajal" and password=="kajal@100"):
    print(username, password, "logging succesfully:")
else:
    print(username ,password,":username and password is invalid")
    print()
time.sleep(2)
print("end of an application")      

