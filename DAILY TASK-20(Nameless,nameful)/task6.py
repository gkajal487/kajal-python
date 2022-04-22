import time
kajal= {10,20,30,40,50,60}
def my_case1(y):
    if y<30:
       return False
    else:
        return True
annu=(filter(my_case1,kajal))
for x in annu:
    print(x)
print()
time.sleep(2)
print("end of an apliction")