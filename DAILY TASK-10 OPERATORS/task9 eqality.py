import time 
l1=[12500,14500,16500,18500]
l2=[12500,14500,16500,18500]
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

