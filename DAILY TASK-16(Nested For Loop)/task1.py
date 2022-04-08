import time 
for x in range(3):  #0,1,2
    time.sleep(1)
    print(x)
    for y in range(3):  #0,1,2
        time.sleep(1)
        print(y)
print()
time.sleep(2)
print("End of an application ...")
