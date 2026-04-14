# # from flask import Flask, render_template
# import sqlite3

# #create flask app instance
# app = Flask(__name__)

# def init_db():
#     #connect to sqlite db file
#     conn = sqlite3.connect('library_system.db')
#     cursor = conn.cursor()
#     cursor.execute('PRAGMA foreign_keys = ON;')

#     #authors table
#     cursor.execute('''CREATE TABLE IF NOT EXISTS Authors
#                     (author_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')
#     #books table
#     cursor.execute('''CREATE TABLE IF NOT EXISTS Books
#                     (book_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT)''')
#     #junction table (many-to-many relationship)
#     #one book can have various authors, one author can write various books
#     cursor.execute('''CREATE TABLE IF NOT EXISTS Book_Authors
#                    (book_id INTEGER, author_id INTEGER,
#                     PRIMARY KEY (book_id, author_id),
#                    FOREIGN KEY (book_id) REFERENCES Books(book_id),
#                    FOREIGN KEY (author_id) REFERENCES Authors(author_id))''')

#     #check if Authors table is empty
#     cursor.execute("SELECT count(*) FROM Authors")

#     #if its empty then insert the new data
#     if cursor.fetchone()[0] == 0:
#         cursor.execute("INSERT INTO Authors (name) VALUES ('Toni Morrison')")
#         cursor.execute("INSERT INTO Books (title) VALUES ('Beloved')")
#         #link the book and author in the junction table
#         cursor.execute("INSERT INTO Book_Authors (book_id, author_id) VALUES (1,1)")
    
#     conn.commit()
#     conn.close()


# #define route for homepage
# @app.route('/')
# def index():
#     #open new db connection per request
#     conn = sqlite3.connect('library_system.db')
#     cursor = conn.cursor()

#     #sql query joining three tables:
#         #authors
#         #books
#         #book_authors (junction table)
#     #produces pairs of (author name, book title)

#     query = '''SELECT Authors.name, Books.title
#             FROM Authors
#             JOIN Book_Authors ON Authors.author_id = Book_Authors.author_id
#             JOIN Books ON Book_Authors.book_id = Books.book_id'''
    
#     cursor.execute(query)
#     #fetch all results as a list of tuples
#     #example: [("Toni Morrison", "Beloved")]
#     data = cursor.fetchall()

#     conn.close()

#     #sends data to flask template
#     #"library_data" becomes available as variable in index.html template
#     return render_template('index.html' , library_data=data)

# if __name__ == '__main__':
#     init_db()
#     app.run(debug=True)