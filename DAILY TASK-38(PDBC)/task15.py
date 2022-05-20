#Deleteing the database from mysql database

import time 
import mysql.connector 
try:
    sql="drop database I_HUB_QT"
    con=mysql.connector.connect(host="localhost",user="root",password="",database="I_HUB_QT")
    cursor=con.cursor()
    cursor.execute(sql) 
    print("Database is deleted successfully ...")
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











