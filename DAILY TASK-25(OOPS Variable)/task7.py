
import time 
class I_HUB:
    def __init__(self):
        I_HUB.a=1002 
        I_HUB.b=1003  
        del I_HUB.b
    
    def m1(self):
        I_HUB.c=1003 
        I_HUB.d=1004 
        del I_HUB.c
        
    @classmethod 
    def m2(cls):
        I_HUB.e=1005
        cls.f=1008
        del cls.f
    
       
    @staticmethod 
    def m3():
        I_HUB.g=1010
        I_HUB.i=1015 
        del I_HUB.i
      
i=I_HUB()
print(I_HUB.__dict__)
print()
i.m1()
print(I_HUB.__dict__)
print()
i.m2()
print(I_HUB.__dict__)
print()
i.m3()
print(I_HUB.__dict__)
I_HUB.s1=12000
I_HUB.s2=23000
del I_HUB.s2 
print(I_HUB.__dict__)
print()
time.sleep(2)
print("End of an application ...")