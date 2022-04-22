import time
class kajal:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "the number of p1 is:",+str(self.name)
p1=kajal("gupta")
print(p1)
print()
time.sleep(2)
print("end of an application")