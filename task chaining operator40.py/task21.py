import time 
l1=[500,500,500,500]
l2=[500,500,500,500]
print(id(l1))
print()
print(id(l2))
print()
print("---Using IO ---")
print(l1 is l2)
print()
print("---Using EO---")
print(l1==l2)
print()
time.sleep(2)
print("End of an application ...")

