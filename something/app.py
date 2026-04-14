from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def audit_page():
    # connect to database
    conn = sqlite3.connect('library_system.db')
    cursor = conn.cursor()

    # fetch all records
    cursor.execute("SELECT id, title, author, rating, cover_url FROM Books")
    all_books = cursor.fetchall()

    conn.close()

    # Send data to HTML templete 
    return render_template('audit.html', books=all_books)

if __name__ == '__main__':
    app.run(debug=True)