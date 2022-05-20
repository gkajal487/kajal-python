#Deleting complete data from the table
import time 
import mysql.connector 
try:
    sql="truncate table P1"
    con=mysql.connector.connect(host="localhost",user="root",password="",database="I_HUB_QT")
    cursor=con.cursor()
    cursor.execute(sql) 
    con.commit()
    print("Data is deleted successfully from the database ...")
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
