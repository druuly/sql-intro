#already exectuted

import sqlite3

# connect db
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# execute
cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute('''CREATE TABLE IF NOT EXISTS authors(
            author_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS books(
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(100) NOT NULL,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors (author_id))''')

cursor.execute("INSERT INTO authors (name) VALUES ('J.R.R. Tolkien')")
tolkien_id = cursor.lastrowid

cursor.execute("INSERT INTO books (title, author_id) VALUES (? , ?)",
            ('The Hobit' , tolkien_id))

conn.commit()
conn.close()
print("Tables linked successfully.")