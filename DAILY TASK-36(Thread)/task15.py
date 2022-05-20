import time 
def Test_Game(num):
    print("You time start now")
    while(num>1):
        num=num-1 
        yield num 
    print("Your time is over")
x=Test_Game(11)
for x1 in x:
    time.sleep(1)
    print(x1)
print()
time.sleep(2)
print("End of an application ...")