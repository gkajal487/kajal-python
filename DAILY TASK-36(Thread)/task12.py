import time 
def Test_Case1():
    yield "Core Python"
    yield "Advance Python"
    yield "Django with REST API's"
    yield "Flask"
x=Test_Case1()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print()
time.sleep(2)
print("End of an application ")
