import time
import numpy as np 
import pandas as pd 
data=[[1001,"Mahesh",34500,"DAD","TM"],[1002,"Satish",54500,"Sr DAD","Infosys"],[1003,"Kajal",32500,"DS","D-MAC"],[1004,"Rahul",30500,"DAD","CG"],[1005,"Atul ",75500,"Sr DAD","IBM"]]
d1=pd.DataFrame(data,column=["eid","ame","sal","design","company"])
print()
print(d1)
print()
time.sleep(2)
print("end of an application")