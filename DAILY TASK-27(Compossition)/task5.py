import time 
class QT_Class:
    def m1(self):
        print("This is parent company ...")
class I_HUB1(QT_Class):
    def m2(self):
        print("This is I_HUB1 one class")
class I_HUB2(I_HUB1):
    def m3(self):
        print("This is I_HUB two class")
class I_HUB3(I_HUB2):
    def m4(self):
        print("This is I_HUB three class")
i1=I_HUB3()
i1.m1()
i1.m2()
i1.m3()
print()
time.sleep(2)
print("End of an application ...")

