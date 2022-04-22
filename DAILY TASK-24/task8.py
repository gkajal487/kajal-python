import time 
import numpy as np 
import pandas as pd 
data=[[1001,"Rahul",45000,"DAD","CG"],[1002,"Ajay",47000,"IOT","CG"],[1003,"Akil",40000,"Python developer","CG"],[1004,"Sameer",41000,"Flask developer","CG"]]
d1=pd.DataFrame(data,columns=['Eid','Ename','Esal','Design','Company'],index=['B1','B2','B3','B4'])
print()
print("------------------------------")
print(d1)
print()
print()
print('---Using count()---')
print(d1.count())
print("-----------------")
time.sleep(2)
print("End of an application ...")


