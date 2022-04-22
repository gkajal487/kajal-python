import time 
class Product:
    def __init__(self,item):
        self.item=item
    def __str__(self):
        return str(self.item)
    def __add__(self,other):
        return self.item+other.item
p1=Product(100)
print("The number of items in p1 is:",p1)
print()
p2=Product(200)
print("The number of items in p2 is:",p2)
print()
print("The total number of items in p1 & p2 are:",p1+p2)
time.sleep(2)
print("End of an application ...")