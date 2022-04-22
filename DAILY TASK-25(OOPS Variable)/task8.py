import time 
class I_HUB:
    emp_id=1001
    def __init__(self):
        I_HUB.emp_id=1002 
    def m1(self):
        I_HUB.emp_id=1003
    @classmethod 
    def m2(cls):
        I_HUB.emp_id=1004 
    @staticmethod 
    def m3():
        I_HUB.emp_id=1005 
i=I_HUB()
I_HUB.emp_id=1006 
print("The final employee id is:",I_HUB.emp_id)
print()
time.sleep(2)
print('End of an application ...')
