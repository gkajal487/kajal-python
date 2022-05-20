import time
try:
    print("this  is the try block")
    print(100//2)
except:
    print("this is the except block")
else:
    print("this is the else block")
finally:
    print("this is the finally block")
print()
time.sleep(2)
print("end of an application")