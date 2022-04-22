import time
print("using nameful function")
def my_function(num):
    return num*num
l=(2,3,4,5,6,7)
l2=list(map(my_function,l))
print("sqare the no from given list",l2)
print()
time.sleep(2)
print("end of an application")