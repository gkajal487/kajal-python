import time
print("...using namful function....")
def odd_number(number):
    if(number%2==1):
        return True
    else:
        return False
number=[2,4,5,6,8]
l1=(filter("odd_number is:",number))
print("odd number from list after filter operation",l1)
print()
time.sleep(2)
print("end of an application")