import time 
import numpy as np 
d1=np.array([['A','B','C'],['a','b','c']],ndmin=7)
print()
print(d1)
print()
print("The daimentions are:",d1.ndim)
print()
for  a in d1:
    for b in a:
        for c in b:
            for d in c:
                for e in d:
                    for f in e:
                        for g in f:
                            print(g,end=" ")
                        print()
print()
time.sleep(1)
print("End of an application ...")
