import time 
class Car:
    print("Car Imp ....")
    class Engine:
        print("Engine imp ...")
        def m1(self):
            print("Engine first service ...")
c=Car().Engine().m1()
print()
time.sleep(2)
print("End of an application ..")
