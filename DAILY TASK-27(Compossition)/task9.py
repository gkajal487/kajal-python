import time 
class A:pass
class B(A):pass 
class C(A):pass 
class D(B,C):pass 
print()
print("---Mro of A class---")
print(A.mro())
print()
print("---Mro of B class----")
print(B.mro())
print()
print("---Mro of C class---")
print(C.mro())
print()
print("----Mro of D class---")
print(D.mro())
print()
time.sleep(2)
print("End of an application ...")
