#identity operator, equality operator
import time
l1=[400,500,600,800]
l2=[300,700,900,100]
print()
print('..adderessing..')
print(id(l1))
print(id(l2))
print()
print('..using identity operator..')
print(l1 is l2)
print()
print('..using equality opeator..')
print(l1==l2)
print()
time.sleep(2)
print('end of an application')