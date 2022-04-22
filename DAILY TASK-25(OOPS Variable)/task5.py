import time
class kajal_g:
    def __init__(self):
         kajal_g.a=1002 
         kajal_g.b=1003  
    def m1(self):
        kajal_g.c=1004 
        kajal_g.d=1005
    @classmethod 
    def m2(cls):
        cls.e=1006 
        kajal_g.f=1007
    @staticmethod 
    def m3():
        kajal_g.g=1008 
        kajal_g.h=1009
i=kajal_g()
print(kajal_g.__dict__)
print()
i.m1()
print(kajal_g.__dict__)
print()
i.m2()
print(kajal_g.__dict__)
print()
i.m3()
print()
print(kajal_g.__dict__)
kajal_g.m=1011
kajal_g.n=1012
print()
print(kajal_g.__dict__)
print()
time.sleep(1)
print("End of an application ..")


