import time 
l1=[]
print(l1)
print("---Adding the elements---")
l1.append(1001)
l1.append("Rahul")
l1.append(56000.0)
l1.append("TM")
print(l1)
print()
l2=[10,20,30]
print()
print("....removing element")
l2.remove(10)
time.sleep(2)
print(l2)
print("end of an application")



#example2
import time 
l1=eval(input('Enter the list data type:'))
print(l1)
print()
print(type(l1))
print('---Fetching the data from the list---')
for abc in l1:
    time.sleep(1)
    print(abc)
print()
time.sleep(2)
print('End of an application ...')





