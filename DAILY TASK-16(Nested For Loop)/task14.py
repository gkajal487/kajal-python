import time
l1=[[[[['A','B','C'],['D','E','F'],['G','H','I']]]]]
print()
print(l1)
print()
#print("The daimentions are:",l1.ndim)
print()
for a in l1:
    for b in a:
        for c in b:
            for d in c:
                for e in d:#
                    print(e,end=" ")
                print() 
print()
time.sleep(2)
print("End of an application ...")

