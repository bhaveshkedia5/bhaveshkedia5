from flask import Flask, request, jsonify;
from elasticsearch import Elasticsearch;

app = Flask(__name__)
es = Elasticsearch()

@app.route('/ingest', methods=['POST'])
def ingest_log():
    log_data = request.get_json()
    es.index(index='logs', doc_type='_doc', body=log_data)
    return jsonify({"message": "Log ingested successfully"}), 201

if __name__ == '__main__':
    app.run(port=3000)
