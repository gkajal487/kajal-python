import time
class my_fun:
    @staticmethod
    def m3(a,b):
      print("the sum of:",a+b)
    print()
a=my_fun()
a.m3(100,300)
print()
my_fun.m3(200,300)
print()
time.sleep(2)
print("end of an application")