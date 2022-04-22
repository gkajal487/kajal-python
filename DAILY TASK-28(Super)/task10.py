import time 
class Product:
    def __init__(self,item):
        self.item=item
    def __str__(self):
        return "The number of items in p1 is:"+str(self.item)
p1=Product(100)
print(p1)
print()
time.sleep(2)
print("End of an application ...")
