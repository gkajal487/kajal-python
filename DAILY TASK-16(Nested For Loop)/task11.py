import time
coloum= 5
for i in range(1, coloum + 1):   
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')
print()
time.sleep(2)
print("end of an application")