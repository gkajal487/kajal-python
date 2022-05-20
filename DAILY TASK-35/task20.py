import time 
try:
    print("This outer try block ...")
    try:
        print("This is Inner try block")
        print(1800//0)
    except:
        print("This is Inner except block")
        print(120//4)
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
