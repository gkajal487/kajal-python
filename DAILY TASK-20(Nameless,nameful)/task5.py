import time
age=[30,40,50,60]
def my_fun(x):
    if x>50:
        return True
    else:
        return False
age2=(filter(my_fun,age))
for x in age2:
  print(x)
print()
time.sleep(2)
print("end of an application")