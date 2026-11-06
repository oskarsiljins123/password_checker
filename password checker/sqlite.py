import sqlite3

connection = sqlite3.connect("test.db")

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
stores(stores_id int primary key , location text)"""

cursor.execute(command1)

cursor.execute('INSERT INTO stores VALUES (1, "a")')
cursor.execute('INSERT INTO stores VALUES (2, "b")')
cursor.execute('INSERT INTO stores VALUES (3, "c")')
cursor.execute('INSERT INTO stores VALUES (4, "d")')
cursor.execute('INSERT INTO stores VALUES (5, "e")')
cursor.execute('INSERT INTO stores VALUES (6, "f")')
cursor.execute('INSERT INTO stores VALUES (7, "g")')

cursor.execute("SELECT location FROM stores")

locations =locations = [row[0] for row in cursor.fetchall()]
print(locations)

x = "g"

print(x)

if x in locations:
    print("yes")
else:
    print("no")