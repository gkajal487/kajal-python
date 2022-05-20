#Display the database information into a tabular
#format from database to console or application console
import time 
import mysql.connector 
try:
    con=mysql.connector.connect(host="localhost",user="root",password="",database="I_HUB_QT")
    cursor=con.cursor() 
    cursor.execute("select * from P1")
    data=cursor.fetchall()
    for x in data:
        for y in x:
            print(y,end=" ")
        print()
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