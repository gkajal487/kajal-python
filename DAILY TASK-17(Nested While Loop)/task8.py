import time
i=1
while(i<=9):
    print(i)
    j=0
    while(j<=9):
        print(i*j,end=" ")
        j+=1
        print()
    i+=1
print()
time.sleep(2)
print("end of an application")