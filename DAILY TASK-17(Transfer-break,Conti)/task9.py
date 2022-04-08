import time
for i in range(4):
    for j in range(4):          
        if j==2:    
            continue
        print("The number is ",i,j)
print()
time.sleep(2)
print("end of an application")
