import time
class myclass:
   def __init__(self,age):
           self.age=age
   def __add__(self,other):
           return self.age+other
   def __radd__(self,other):
           return self.age+other
a=myclass(1)
a+2
print()
print("end of an application")