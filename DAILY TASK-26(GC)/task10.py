import time 
class Robot:
    def __init__(self):
        self.name="Chitti"
        self.head=self.HEAD()
    def m1(self):
        print("Name of the robot is:",self.name)
        self.head.talk()
        self.head.microchip.think()
    class HEAD:
        def __init__(self):
            self.microchip = self.MicroChip()
        def talk(self):
            print("Chitti is talking ....")
        class MicroChip:
            def think(self):
                print("Chitti is thinking ...")
r1=Robot()
r1.m1()
print()
time.sleep(2)
print('End of an application ...')