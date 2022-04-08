import time
l1=[['A','B','C'],['D','E','F'],['G','H','I']]
print(l1)
print()
print(type(l1))
print()
for l2 in l1:
    for l3 in l2:
        print(l3,end="  ")
print()
print()
time.sleep(2)
print("End of an application ...")

