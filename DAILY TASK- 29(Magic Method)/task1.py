import time
class myfloat:           
      def __init__(self,whole,fraction):        
                self.whole=whole         
                self.fraction=fraction      
      def shownumber(self):       
                print(f"I am {self.whole}.{self.fraction}")
M=myfloat(3,7)
M.shownumber()
print()
time.sleep(2)
print("end of an application")