import time 
s1={chr(97),chr(98),chr(99),chr(100),chr(101)}
print("--Before mutable operation---")
print(s1)
print()
print(type(s1))
print()
print("---After mutable operation---")
s1[0]='A'
print(s1)
print()
time.sleep(2)
print("End of an application ...")
