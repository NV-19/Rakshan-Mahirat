import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="root", password="naveen@1911",database="testconn",auth_plugin='mysql_native_password')

cursor=mydb.cursor()

cursor.execute("show databases")

for db in cursor:
    print(db)

