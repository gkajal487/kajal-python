from functools import reduce
import time
total_salary=[200,300,400,500,600]
l1=reduce(lambda x,y:x+y ,total_salary)
print("the total salary from python departent:",l1)
print()
time.sleep(2)
print("end of an application")