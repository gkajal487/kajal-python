import time 
try:
    print("This outer try block ...")
    try:
        print("This is Inner try block")
    except:
        print("This is Inner except block")
    else:
        print("This is Inner esle block")
    finally:
        print("This is Inner finally block")
except:
    print("This outer except block .. .")
else:
    print("This is outer esle block")
finally:
    print("This outer finally block")
print()
time.sleep(2)
print("End of an application ...")

