import sqlite3

def get_books_by_id(max_id):
    conn = sqlite3.connect('library_system.db')
    cursor = conn.cursor()

    query = "SELECT title FROM Books WHERE book_id. <= ?"

    cursor.execute(query, (max_id,))
    results = cursor.fetchall()

    conn.close()
    return results