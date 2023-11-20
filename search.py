from flask import Flask, request, render_template
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_logs():
    query = request.form.get('query')
    results = search_logs_in_elasticsearch(query)
    return render_template('results.html', results=results)

def search_logs_in_elasticsearch(query):
    # Perform Elasticsearch query based on the user's input
    # You need to implement the specific logic for constructing the Elasticsearch query
    # based on the provided filters and search terms
    # For simplicity, let's assume a basic full-text search for now
    body = {
        "query": {
            "match": {
                "message": query
            }
        }
    }
    response = es.search(index='logs', body=body)
    return response['hits']['hits']

if __name__ == '__main__':
    app.run(port=5000)
