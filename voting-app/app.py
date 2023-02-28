from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vote', methods=['POST'])
def vote():
    animal = request.form['animal']
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS votes (id INTEGER PRIMARY KEY AUTOINCREMENT, animal TEXT)')
    c.execute('INSERT INTO votes (animal) VALUES (?)', (animal,))
    conn.commit()
    conn.close()
    return 'Thank you for voting!'

@app.route('/results')
def results():
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    c.execute('SELECT animal, COUNT(*) FROM votes GROUP BY animal')
    results = c.fetchall()
    conn.close()
    return render_template('results.html', results=results)
