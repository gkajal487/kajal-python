import time
def case_list():
    l1=[10,20,30,40,50,60]
    sum=0
    for x in l1:
        sum=sum+x
    print("the sum of list",sum)
def case_list2():
    l2=[22,33,44,55,66,77]
    i=0
    while(i<len(l2)):
        print(l2[i])
        i+1
print()
case_list()
print()
case_list2()
print()
time.sleep(2)
print("end of an application")

