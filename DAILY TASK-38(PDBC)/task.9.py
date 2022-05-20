#Fetching the records from the database

import time 
import mysql.connector 
try:
    con=mysql.connector.connect(host="localhost",user="root",password="",database="I_HUB_QT")
    cursor=con.cursor() 
    cursor.execute("select * from P1")
    data=cursor.fetchall()
    print("Product Information")
    print('--------------------')
    for d in data:
        print("Pid is:",d[0])
        print("Pname is:",d[1])
        print("Price is:",d[2])
        print("Company is:",d[3])
        print()
    print("--------------------------")
    
  
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
