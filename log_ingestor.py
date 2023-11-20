# log_ingestor.py

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize SQLite database
conn = sqlite3.connect('logs.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        source TEXT,
        message TEXT
    )
''')
conn.commit()
conn.close()

@app.route('/ingest', methods=['POST'])
def ingest_log():
    data = request.get_json()

    timestamp = data.get('timestamp')
    source = data.get('source')
    message = data.get('message')

    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO logs (timestamp, source, message) VALUES (?, ?, ?)', (timestamp, source, message))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success'}), 201

if __name__ == '__main__':
    app.run(port=3000)
