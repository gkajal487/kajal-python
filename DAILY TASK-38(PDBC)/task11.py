#Updating a column as per the applicaton requirement
import time 
import mysql.connector 
try:
    sql="update P1 set price=price+15000 where pid=1004"
    con=mysql.connector.connect(host="localhost",user="root",password="",database="I_HUB_QT")
    cursor=con.cursor()
    cursor.execute(sql) 
    con.commit()
    print("Apple mobile price is updated ...")
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

