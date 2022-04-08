import time 
def Test_Case3(*a):
    sum=0 
    for x in a:
        sum=sum+x 
    print("The sum of arguments is:",sum)
Test_Case3()
Test_Case3(10)
Test_Case3(10,20)
Test_Case3(10,20,30)
Test_Case3(10,20,30,40)
print()
time.sleep(1)
print("End of an application ...")
