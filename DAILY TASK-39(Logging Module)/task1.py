import time
import logging
logging.basicConfig("info1.txt",level=logging.DEBUG)
print("new logging demo")
logging.critical("critical information")
logging.error("error information")
logging.warning("warning information")
logging.info("info information")
logging.debug("debug information")
print()
time.sleep(2)
print("end of an applicaton")