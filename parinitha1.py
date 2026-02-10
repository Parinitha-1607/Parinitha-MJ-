import mysql.connector
host="localhost"
user="root"
password="root"
db="parinitha1"
conn=mysql.connector.connect(host=host,user=user,password=password,db=db)
cur=conn.cursor()
cur.execute("select * from Customers")
res=cur.fetchone()
print(res)
