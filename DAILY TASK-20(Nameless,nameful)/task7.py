import time
a=(1,3,4,5,6)
def filter_case(a):
        if (a%2==1):
             return True
        else:
           return False
b=list(filter(filter_case,a))
print("odd number from the list:",b)
print()
time.sleep(2)
print("end of an application")