import time 
def decor(func):
    def inner(name):
        if(name=="python"):
            print(name,":Meant for data science applications")
        elif(name=="java"):
            print(name,":Meant for ERP appliction ...")
        else:
            func(name)
    return inner
@decor
def Test_Case1(name):
    print("Name of the language is:",name)
Test_Case1("Python")
print()
Test_Case1("Java")
print()
time.sleep(2)
print("End of an application ...")
