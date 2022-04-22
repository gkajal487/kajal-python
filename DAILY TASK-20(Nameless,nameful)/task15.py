import time 
def Test_list1():
    l1=[10,20,30,40,50,60]
    sum=0 
    for x in l1:
        sum=sum+x 
    print("The sum of list is:",sum)
def  Test_tuple1():
    s1=(10,20,30,40,50,60)
    i=0
    while(i<len(s1)):
        print(s1[i])
        i+=1 
Test_list1()
print()
Test_tuple1()
print()
time.sleep(2)
print("End of an application ...")
