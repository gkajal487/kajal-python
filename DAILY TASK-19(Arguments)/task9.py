import time
def my_function(**arguments):
    print(arguments)
    print("key","value")
    print("[0],[1]".format("key,value"))
my_function(name="kajal",roll=1,sub="maths")
print()
time.sleep(2)
print("end of an application")
