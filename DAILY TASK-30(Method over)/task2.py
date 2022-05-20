import time
class Calculate:
   def add(self, *a):
     result = 0
     for x in a:
        result += x
        print("Result: {}".format(result))

c1 = Calculate()
c1.add(10, 20, 30)
c1.add(10,20)
print()
time.sleep(2)
print("end of an application")