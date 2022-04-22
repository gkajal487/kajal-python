import time 
class I_HUB:
    def __init__(self):
        I_HUB.a=1002 
        I_HUB.b=1003  
        print(I_HUB.a,I_HUB.b)
    def m1(self):
        I_HUB.c=1003 
        I_HUB.d=1004 
        print(I_HUB.c,I_HUB.d)    
    @classmethod 
    def m2(cls):
        I_HUB.e=1005
        cls.f=1008
        print(I_HUB.e,cls.f)
       
    @staticmethod 
    def m3():
        I_HUB.g=1010
        I_HUB.i=1015 
        print(I_HUB.g,I_HUB.i) 
i=I_HUB()
print()
i.m1()
print()
i.m2()
print()
i.m3()
print()
I_HUB.k=1019
print(I_HUB.k)
print()
time.sleep(1)
print("End of an application ...")
