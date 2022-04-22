import time
class parent:
    def __init__(self,text):
        self.text=text
    def m1(self):
        print(self.text)
    def m2(self):
        print(self.text)
class child(parent):
    def __init__(self, text):
        super().__init__(text)
        super().m1()
        super().m2()
        super().m3()
a=child("hello,welcome")
print()
time.sleep(2)
print("end of an application")