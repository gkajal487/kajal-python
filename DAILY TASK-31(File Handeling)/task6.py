import time 
f=open("info1.txt","w")
emp_info=["1001\n","Rahul Reddy\n","45000\n","DAD\n","CG\n"]
f.writelines(emp_info)
print("A new file is created ...")
f.close()
print()
time.sleep(2)
print("End of an applcation ..")

