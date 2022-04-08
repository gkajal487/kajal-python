import time
eid=[]
ename=[]
esal=[]
company=[]
design=[]
print()
while(True):
    a=input("enter the eid:")
    eid.append(a)
    b=input("enter the ename:")
    ename.append(b)
    c=float(input("enter the esal:"))
    esal.append(c)
    d=("enter the design:")
    design.append(d)
    e=("enter the company:")
    company.append(e)
    option=("dear user do you want to insert another record ")
    if(option=="no"):
        break
        print("eid","ename","esal","company","design")
for y1,y2,y3,y4,y5 in zip(eid,ename,esal,design,company):
  print(y1,y2,y3,y4,y5)
print()
time.sleep()
print("end of an application")