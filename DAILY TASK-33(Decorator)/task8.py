import time
from unicodedata import name
def decor(func):
    def inner(a,b):
        if (b==0):
            print(b,"dear use only allo no are [0,9]")
        else:
            func(a,b)
    return inner
@decor
def test_case1(a,b):
    print("the result is" ,a//b)
test_case1(100,10)
print()
test_case1(100,12)
print()
test_case1(100,40)
print()
test_case1(100,50)
print()
time.sleep(2)
print("end of an applicatin")




