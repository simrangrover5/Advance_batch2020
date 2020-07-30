
import sqlite3 as sql

db = sql.connect("customer.db")
cursor = db.cursor()
while not input("\n Press enter to continue......."):
    name = input("\n Name : ")
    id1 = int(input("\n Id : "))
    product = int(input("\n Product : "))
    cursor.execute(f"insert into customer values({id1},'{name}',{product})")
    db.commit()
    print("\n Data inserted")
