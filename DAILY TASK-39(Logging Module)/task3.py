import time
import logging
logging.basicConfig(filename="info5.txt",level=logging.INFO)
print("print new loggin demo")
logging.NOTSET("notset information")
logging.DEBUG("debug information")
logging.INFO("info information")
logging.WARNING("WARNING information")
logging.ERROR("error information")
logging.CRITICAL("critical information")
print()
time.sleep(2)
print("end of the application")