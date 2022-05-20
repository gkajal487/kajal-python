import time
with open("task1.py:","w")as f:
    print("--file information--")
    print("file name is:",f.name)
    print("file name is:",f.mode)
    print("file is closed or not:",f.closed)
    print("file is writable or not:",f.writable)
    print("file is readable or not:",f.readable)
print()
print("file closed or not:",f.closed)
time.sleep(2)
print("end of an application")