from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def init_db():
    #db setup
    conn = sqlite3.connect('library_system.db')
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreign_keys = ON;')

    #authors table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Authors
                    (author_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')
    #books table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Books
                    (book_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT)''')
    #junction table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Book_Authors
                   (book_id INTEGER, author_id INTEGER,
                    PRIMARY KEY (book_id, author_id),
                   FOREIGN KEY (book_id) REFERENCES Books(book_id),
                   FOREIGN KEY (author_id) REFERENCES Authors(author_id))''')
    
    cursor.execute("SELECT count(*) FROM Authors")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO Authors (name) VALUES ('Toni Morrison')")
        cursor.execute("INSERT INTO Books (title) VALUES ('Beloved')")
        cursor.execute("INSERT INTO Book_Authors (book_id, author_id) VALUES (1,1)")
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('library_system.db')
    cursor = conn.cursor()

    query = '''SELECT Authors.name, Books.title
            FROM Authors
            JOIN Book_Authors ON Authors.author_id = Book_Authors.author_id
            JOIN Books ON Book_Authors.book_id = Books.book_id'''
    
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()

    return render_template('index.html' , library_data=data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)