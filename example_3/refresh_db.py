import sqlite3

def refresh_db():
    conn = sqlite3.connect('library_system.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # rm old tables

    cursor.execute("DROP TABLE IF EXISTS Book_Authors;")
    cursor.execute("DROP TABLE IF EXISTS Books;")
    cursor.execute("DROP TABLE IF EXISTS Authors;")

    # rebuild new tables

    # Authors table
    cursor.execute("(CREATE TABLE Authors (author_id INTEGER PRIMARY KEY, name TEXT);")

    # Books table
    cursor.execute("CREATE TABLE Books (book_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT);")

    # Book_Authors table (junction)
    cursor.execute("CREATE TABLE Book_Authors (book_id INTEGER, author_id INTEGER,"
                   "FOREIGN KEY(book_id) REFERENCES Books(book_id)," 
                   "FOREIGN KEY(author_id) REFERENCES Authors(author_id));")
    
    # insert authors with a tuple of tuples

    authors = [('Neil Gaiman',),
                ('Terry Pratchett',),
                ('N.K. Jemisin',),
                ('Stephen King',),
                ('Peter Straub',),
                ('Octavia Butler',)
                ]
    
    cursor.executemany("INSERT INTO Authors (name) VALUES (?);" , authors)

    # insert books with a tuple of tuples
    
    books = [('Good Omens',),
             ('The Talisman',),
             ('The Fifth Season',),
             ('American Gods',),
             ('Kindred',),
             ('Sandman',),
             ]
    
    cursor.executemany("INSERT INTO Books (title) VALUES(?);" , books)

    # insert relationships

    relationships = [
        (1,1) , (1,2),
        (2,4) , (2,5),
        (3,3) ,
        (4,1) , 
        (5,6) , 
        (6,1) ,
    ]

    cursor.executemany("INSERT INTO Book_Authors (book_id, author_id) VALUES (?, ?);" , relationships)

    conn.commit()
    conn.close()
    print("Database refreshed and updated.")

    if __name__ == "__main__":
        refresh_db()