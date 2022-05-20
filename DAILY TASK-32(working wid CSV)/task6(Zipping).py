import time 
from zipfile import * 
f=ZipFile("files.zip","w",ZIP_DEFLATED)
f.write("number.txt")
f.write("otp.txt")
f.write("email.txt")
print()
print("A zip file is created successfully ...")
f.close()
print()
time.sleep(2)
print("End of an application ...")
