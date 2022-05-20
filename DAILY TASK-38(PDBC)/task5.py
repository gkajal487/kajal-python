#INSERTING SINGLE ROW
import time 
import mysql.connector 
try:
    sql="insert into P1 values(1001,'Mobile',34500,'VIVO')"
    con=mysql.connector.connect(host="localhost",user="root",password="",database="I_hub_QT")
    cursor=con.cursor() 
    cursor.execute(sql)
    print("A new Database created in Mysql DB")
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

