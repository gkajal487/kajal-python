import time 
import logging 
logging.basicConfig(format="%(message)s:%(levelname)s:%(asctime)s",datefmt="%d/%m/%Y %H:%M:%S %p",level=logging.DEBUG)
print("New logging demo")
print()
logging.debug("Debug Iformaion")
logging.info("Info information")
logging.warning("Warning Information")
logging.error("Error information")
logging.critical("Critical information")
print()
time.sleep(2)
print('End of an application ...')
