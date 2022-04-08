import time 
number=int(input("Enter the number here:"))
for x in range(1,11):
    time.sleep(1)
    print("%dX%d=%d\n"%(number,x,number*x))
print()
time.sleep(2)
print("End of an application ...")
