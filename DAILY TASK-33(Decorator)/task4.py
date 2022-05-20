import time
def decor(func):
    def inner(name):
        if(name=="Python"):
            print(name,":Meant for data science applications")
        elif(name=="Java"):
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
time.sleep(2)
print("End of an application ...")

