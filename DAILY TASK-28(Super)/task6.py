import time 
class QT_class:
    company_name="IBM"
    def __init__(self):
        self.company_name1="Dell"
class I_HUB_class(QT_class):
    def m1(self):
        print("Parent company name is:",super().company_name)
        print("Child company name is:",self.company_name1)
i=I_HUB_class()
i.m1()
print()
time.sleep(2)
print("end of an application")