import sqlite3 as sql

db = sql.connect("customer.db")
cursor = db.cursor()

cmd = "select * from customer"
cursor.execute(cmd)

data = cursor.fetchall()
print(data)
