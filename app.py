import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        msg = request.form.get('msg')

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO messages (name, msg) VALUES (?, ?)", (name, msg))
        
        conn.commit()
        conn.close()

        return render_template('thank_you.html', name=name)

    return render_template('contact.html')

# display messages
@app.route('/messages')
def messages():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, msg FROM messages")
    data = cursor.fetchall()

    conn.close()

    return render_template('messages.html', messages=data)

#db
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            msg TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    
# Run app
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
