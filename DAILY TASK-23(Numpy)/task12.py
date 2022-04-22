import time
from traceback import print_tb 
import numpy as np 
d1=np.array([200,300,400,500,100,200,300,400,700,800])
print()
d2=d1.reshape(5,2)
print()
print(d2)
print("the diamwnsion are",d1.ndim)
print()
time.sleep(2)
print("end of an application")