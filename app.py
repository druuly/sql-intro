import sqlite3

# connect db
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# execute 
with open ('setup.sql' , 'r') as sql_file:
    cursor.executescript(sql_file.read())

conn.commit()
conn.close
print('Database setup completed.')