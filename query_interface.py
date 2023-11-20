# query_interface.py

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/query', methods=['GET'])
def query_logs():
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    source = request.args.get('source')
    keyword = request.args.get('keyword')

    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()

    query = 'SELECT * FROM logs WHERE 1=1'

    if start_time:
        query += f" AND timestamp >= '{start_time}'"
    if end_time:
        query += f" AND timestamp <= '{end_time}'"
    if source:
        query += f" AND source = '{source}'"
    if keyword:
        query += f" AND message LIKE '%{keyword}%'"

    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()

    return jsonify({'logs': result})

if __name__ == '__main__':
    app.run(port=4000)
