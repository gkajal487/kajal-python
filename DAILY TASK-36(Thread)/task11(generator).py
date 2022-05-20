import time
def tast_case():
    yield "core python"
    yield "advance python"
    yield "django"
x=tast_case()
print(next(x))
print(next(x))
print(next(x))
print()
time.sleep(2)
print("end of an application")