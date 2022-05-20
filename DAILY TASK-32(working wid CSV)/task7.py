import time
from zipfile import*
f=ZipFile("files.zip","w",ZIP_DEFLATED)
d1=f.namelist
print(d1)
print()
time.sleep(2)
print("end of an application")