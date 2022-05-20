import time
from threading import*
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
t1=Thread(target=test_squar(num))
t2=Thread(target=test_expo(num))
t3=Thread(target=test_add(num))
t4=Thread(target=test_add(num))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
endtime=time.time()
print("time is without multithreading:",beginingtime,endtime)
print()
time.sleep(2)
print("end of an application")