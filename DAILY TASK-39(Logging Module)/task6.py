import time 
import logging 
logging.basicConfig(filename="info1.txt",level=10,filemode="w")
print("New logging demo")
logging.debug("Debug Iformaion")
logging.info("Info information")
logging.warning("Warning Information")
logging.error("Error information")
logging.critical("Critical information")
print()
time.sleep(2)
print('End of an application ...')
