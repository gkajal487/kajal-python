#Inserating two rows data or informat
import time 
import mysql.connector 
try:
    sql="insert into P1 values(%s,%s,%s,%s)"
    con=mysql.connector.connect(host="localhost",user="root",password="",database="I_HUB_QT")
    cursor=con.cursor() 
    record=([1002,"Tab",17000,"Samsung"],[1003,"LCD TV",56000,'Sony'])
    cursor.executemany(sql,record)
    con.commit()
    print("Two records successfully inserterd ...")
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