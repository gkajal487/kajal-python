import time
from threading import*
def test_case():
    for x in range (9):
        time.sleep(1)
        print("this is advance python")
t=Thread(target=test_case)
t.start()
for x in range (9):
    time.sleep(2)
    print("this is core python")
print()
time.sleep(2)
print("end of an application")