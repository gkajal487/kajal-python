import time
from zipfile import *
import zipfile
f=ZipFile("files.zip","w",ZIP_DEFLATED)
d1=f.namelist
for d2 in d1:
    print("---the file name is d2")
    f1=(d2,"r")
    d4=f1.read()
    print(d4)
    print()
print("---------------------")
f.close()
time.sleep(2)
print("End of an application ...")




