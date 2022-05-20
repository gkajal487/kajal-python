import time
class product_information:
    def setpid(self,pid):
        self.pid=pid
    def getpid(self):
        return self.pid 
    def pname(self):
        return self.pname 
    def setpprice(self):
        return self.pprice
    def setcompany(self):
        return self.company
p=product_information()
p.setpid(1001)
p.setpname("mobile")
p.setpprice(30000)
p.setcompany("samsung")
print()
print("----product information----")
print("pid is",p.getpid())
print("pname is:",p.getpname())
print("price is:",p.getpprice())
print("pcompany:",p.pcompany())
time.sleep(2)
print("end of am application")
