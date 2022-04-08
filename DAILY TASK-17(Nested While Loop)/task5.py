import time
l1=[[1,2,3],[4,5,6],[7,8,9]]
print(l1)
print()
i=0
while(i<len(l1)):
    j=0
    while(j<len(l1)):
        print(l1[i][j])
        j+=1
    i+=1
print()
time.sleep(2)
print("end of an application")
