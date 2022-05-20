import time
def test_case():
    yield "kajal"
    yield "annu"
    yield "varsha"
    yield "banti"
    yield "khushboo"
    yield "ranu"
    yield "gunu"
y=test_case()
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print()
time.sleep(2)
print("end of an application")