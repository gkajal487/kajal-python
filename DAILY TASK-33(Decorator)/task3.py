import time
from unicodedata import name
def decore(func):
    def inner(name):
        if (name=="python"):
            print(name,":it is meant for data science application")
        else:
           func(name)
    return inner   
@decore
def test_kajal(name):
    print("that girl is a beautiful",name)
test_kajal("kajal")
print()
time.sleep(2)
print("end of an application")