#CREATING THE DATABASE AS I_hub_QT
import time
import mysql.connector
try:
    sql="creat a data base I_hub_QT"
    con=mysql.connector.connect(host="localhost",user="root",password="")
    cursor=con.cursor()
    cursor.execute(sql) 
    print("a new sql database created in mysql DB")
except mysql.connector. DatabaseError as e:
    if con:
        con.rollback()
        print("there is a exception",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close
print()
time.sleep(2)
print("end of an application")
