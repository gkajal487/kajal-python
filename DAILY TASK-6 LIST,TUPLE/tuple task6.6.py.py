#list is mutable
import time
t5=[10,50,60,70,80]
print()
print('before mutuble')
print(type(t5))
print()
print('after mutable')
t5[0]=100
t5[1]=200
t5[2]=300
t5[3]=400
t5[4]=500
print(t5)
print(type(t5))
print()
time.sleep(2)
print("end of an applicatinon")

#before mutuble
#<class 'list'>

#after mutable
#[100, 200, 300, 400, 500]
#<class 'list'>

#end of an applicatinon

