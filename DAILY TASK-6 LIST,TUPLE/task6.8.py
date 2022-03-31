#Indexing and slice operator is applicable for list:
import time
rohit_info=[10001,'rohit',1050.50,'cisco',10-11-2018,10-11-2020]
print(rohit_info)
print()
print("...rohit_info...")
print("Pid is:",rohit_info[0])
print("Pname is:",rohit_info[1])
print("Price is:",rohit_info[2])
print("Company is:",rohit_info[3])
print("M_date is:",rohit_info[4])
print("Exp_date is:",rohit_info[5])
print("-------------------------")
print()
print("---Using slice operator---")
print(rohit_info[0:])
print(rohit_info[::-1])
print(rohit_info[1:6])
print(rohit_info[1:6:2])
print("-------------------")
print()
time.sleep(2)
print("End of an application ...")





