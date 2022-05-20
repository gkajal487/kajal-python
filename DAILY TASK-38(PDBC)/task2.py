#CREATING THE PRODUCT TABLE
import time 
import mysql.connector 
try:
    sql="create table products(pid INT, pname VARCHER(20),price INT)"
    con=mysql.connector.connect(host="localhost",user="root",password="",database="I_hub_QT")
    cursor=con.cursor()
    cursor.execute(sql)
    print("a new table created in mysql DB")
except mysql.connector.connect.databaseerror as e:
    print("there is a exption",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
print()
time.sleep(2)
print("end of an application")

