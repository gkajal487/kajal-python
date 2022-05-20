#adding exter column in TABLE
import time
import mysql.connector
try:
    sql="alter table add product VARCHER(20)"
    con=mysql.connector.connect(host="local host",user="root",password="",database="I_hub_QT")
    cursor=con()
    con.execute(sql)
    print("a table created succesefully")
except mysql.connector.connect.databaseeerror as e:
    print("there is a database",e)
finally:
    if cursor():
        cursor.close()
    if con():
        con.close()
print()
time.sleep(2)
print("end of an application")


