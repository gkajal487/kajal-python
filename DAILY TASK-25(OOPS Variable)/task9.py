import time 
class I_HUB:
    def __init__(self):
        emp_id=1001
        print("Employee_Id is:",emp_id)
    def m1(self):
        emp_name="Harish Kumar"
        print("Employee_Name is:",emp_name)
    @classmethod 
    def m2(self):
        emp_sal=42500 
        print("Employee_Salary is:",emp_sal)
    @staticmethod
    def m3():
        emp_design="Django Developer"
        emp_company="TCS"
        print("Employee_Designation is:",emp_design)
        print("Employee_Company is:",emp_company)
i=I_HUB()
i.m1()
i.m2()
i.m3()
print()
time.sleep(2)
print("End of an application ...")

    

