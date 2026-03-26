import sqlite3
from flask import Flask , render_template , request

app = Flask(__name__)

@app.route('/filter')

def filter_by_id():
    # capture the main_id from the url
    # if missing it will default to 0

    min_id = request.args.get('main_id', 0)

    conn = sqlite3.connect('library_system.db')
    cursor = conn.cursor()

    # this wil tell the databse to give me the rows where the ID is higher than x

    query = "SELECT book_id, title FROM Books WHERE book_id > ?"
    cursor.execute(query, (min_id,))

    results = cursor.fetchall()
    conn.close()

    return render_template('filter.html', books=results,current_id=min_id)

if __name__ == "__main__":
    app.run(debug=True)
    filter_by_id()