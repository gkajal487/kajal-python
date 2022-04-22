import time
import numpy as np
d1=np.array([[[[[123,234,345,456],[678,789,890,888]]]]])
print()
print(d1)
print()
print("The daimentions are:",d1.ndim)
print()
for a in d1:
    for b in a:
        for c in b:
            for d in c:
                print(d,end="")
print()
time.sleep(1)
print("End of an application ...")
