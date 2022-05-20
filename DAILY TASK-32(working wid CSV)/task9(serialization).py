import time 
import json 
d1={}
d1['eid']=1001
d1['ename']="Rahul Redddy"
d1['esal']=37000 
d1['design']="JavaScript Developer"
d1['visa_status']=True 
d1['status']=None
print()
with open("tool1.txt","w") as f:
    json.dump(d1,f)
print("Object serilization is done ...")
print()
time.sleep(2)
print("End of an application ...")


