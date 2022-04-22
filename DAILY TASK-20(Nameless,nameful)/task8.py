import time
print("using nameless function")
number=[109,108,107,106,345,234,678]
l=list(filter(lambda x:x%2==1,number))
print(" odd no is after filtering data  are",l)
print()
time.sleep(2)
print("end of an application")