import time 
def decor( Test_Case1):
    def inner(name):
        if(name=="Python"):
            print(name,":Meant for data science applications")
        elif(name=="Java"):
            print(name,":Meant for ERP appliction ...")
        else:
             Test_Case1(name)
    return inner

def Test_Case1(name):
    print("Name of the language is:",name)
decorfunction=decor(Test_Case1)
Test_Case1("Python")
print()
decorfunction("Python")
print()
Test_Case1("Java")
print()
decorfunction("Java")
print()
time.sleep(2)
print("End of an application ...")
