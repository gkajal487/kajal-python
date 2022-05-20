import time 
import pickle
class train:
    def __init__(self,tname,tno,depattime,arriveltime):
        self.tname=tname
        self.tno=tno
        self.depattime=depattime
        self.arriveltime=arriveltime
        def m1(self):
            print(self,tname,tno,depattime,arriveltime)
with open ("data1.txt","wb")as f:
     t=train("jammutavi",1234,"12:34pm ist","12:45am ist")
     pickle.dump(t,f)
     print("pickling process is done")
with open("data.txt","rb")as f:
    a=pickle.load(f)
    print("unpickling process is done")
print()
time.sleep(2)
print("end of the application")