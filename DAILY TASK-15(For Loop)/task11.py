import time 
n=int(input('Enter the number of rows:'))
for x in range(n):
    pid=int(input("Enter the pid:"))
    pname=input("Enter the pname:")
    price=float(input("Enter the price:"))
    company=input("Enter the company:")
    m_date=input("Enter the m_date")
    exp_date=input("Enter the exp_date:")
print()
print("---Product Information---")
print(pid,pname,price,company,m_date,exp_date)
print('--------------------------------------')
print()
time.sleep(2)
print("End of an application ...")
