import time 
import logging 
logging.basicConfig(filename="info_error.txt",level=logging.DEBUG ,format="%(message)s:%(levelname)s:%(asctime)s",datefmt="%d/%m/%Y %H:%M:%S %p",filemode="w")
print("A new request came on desk ....")
try:
    obj1=int(input("Enter the value for obj1:"))
    obj2=int(input("Enter the value for obj2:"))
    res1=obj1//obj2 
    print("The result is:",res1)
except ZeroDivisionError as e:
    print("There is an exception:",e)
    logging.exception(e)
except ValueError as e:
    print("There is an exception:",e)
    logging.exception(e)
print("A request processed successfully ...")
print()
time.sleep(2)
print("End of an application ...")
