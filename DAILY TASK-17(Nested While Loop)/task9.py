import time
i=1
while(i<=6):
    
    j=1
    while(j<=6):
        print(i,"X",j,"=",i*j,end="  ")
        j+=1
        print()
    i+=1
print()
time.sleep(2)
print("end of an application")