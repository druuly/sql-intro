import _sqlite3

def setup_library():
    conn = _sqlite3.connect('library.db')
    cursor = conn.cursor()

    #clear out old data
    cursor.execute('''DROP TABLE IF EXISTS Books''')

    #create the schema
    cursor.execute('''
                CREATE TABLE Books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    author TEXT,
                    rating INTEGER,
                    cover_url TEXT
                )
                ''')

    #insert data
    library_data = [
        ('The Hobbit' , 'J.R.R. Tolkien', 4.8 , 'https://covers.openlibrary.org/b/id/6979861-L.jpg'),
        ('The Shining' , 'Stephen King', 4.5 , 'https://covers.openlibrary.org/b/id/8231856-L.jpg'),
        ('Good Omens' , 'Neil Gaiman' , 4.7 , 'https://covers.openlibrary.org/b/id/10520280-L.jpg'),
        ('Database Test Entry' , None , None , None)
    ]

    cursor.executemany('''INSERT INTO Books (title, author, rating, cover_url) VALUES (?, ?, ?, ?)''', library_data)
    conn.commit()
    conn.close()
    print("Database refreshed successfully.")

if __name__ == "__main__":
    setup_library()