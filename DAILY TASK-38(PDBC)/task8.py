#Inserting the records using while loop from the keyboard
import time 
import mysql.connector 
try:
    con=mysql.connector.connect(host="localhost",user="root",password="",database="I_HUB_QT")
    cursor=con.cursor() 
    while(True):
        pid=int(input("Enter the pid:"))
        pname=input("Enter the pname:")
        price=float(input("Enter the price:"))
        company=input("Enter the company:")
        sql="insert into P1 values(%s,'%s',%s,'%s')"
        cursor.execute(sql%(pid,pname,price,company))
        option=input("Do you want to insert another record[YES|NO]:")
        if(option=="NO"):
            con.commit()
            break 
    print("Okay ...")
 
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