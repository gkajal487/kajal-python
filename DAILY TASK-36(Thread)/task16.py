import time
def test_game(num):
    print("your time start now")
    while (num<10):
        num=num+1
        yield (num)
        print("your time is over")
x=test_game()
for y in x:
    time.sleep(1)
print(y)
print(type(y))
print()
time.sleep(2)
print("end of an application")