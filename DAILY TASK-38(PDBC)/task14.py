#Deleteing the table from I_HUB_QT database

import time 
import mysql.connector 
try:
    sql="drop table P1"
    con=mysql.connector.connect(host="localhost",user="root",password="",database="I_HUB_QT")
    cursor=con.cursor()
    cursor.execute(sql) 
    print("Table is deleted successfully ...")
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("There is an exception:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
print()
time.sleep(2)
print("End of an application ...")

