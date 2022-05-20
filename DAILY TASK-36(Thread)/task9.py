import time
def test_squar(num):
    for x1 in (num):
        print("this is the squar ",x1*x1)
def test_expo(num):
    for x2 in (num):
        print("this is the expo:",x2**x2)
def test_add(num):
    for x3 in (num):
        print("this is the add value:",4+x3)
def test_double(num):
    for x4 in (num):
        print("this is the double value:",5*x4)
print()
num=[1,2,3,4,5,6,7,8]
beginingtime=time.time()
test_squar(num)
test_expo(num)
test_add(num)
test_add(num)
endtime=time.time()
print("time is without multithreading:",beginingtime,endtime)
print()
time.sleep(2)
print("end of an application")