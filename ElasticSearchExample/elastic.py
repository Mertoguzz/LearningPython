from datetime import datetime
from elasticsearch import Elasticsearch
from flask import Flask, jsonify, request
# es = Elasticsearch()
host='localhost'
port='9200'
connection=Elasticsearch([{'host':host,'port':port}],timeout=100)
app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    results=connection.get(index='contents', doc_type='title', id='0')
    return jsonify(results['_source'])


@app.route('/insert_data',methods=['POST'])
def insert_data():

    slug=request.form['slug']
    title=request.form['title']
    content=request.form['content']

    body={
        'slug':slug,
        'title':title,
        'content':content,
        'timestamp':datetime.now()


    }
    result=connection.index(index='contents',doc_type='title',id=slug,body=body)

    return jsonify(result)



@app.route('/search',methods=['POST']) 
def search():
    keyword=request.form['keyword']

    # multi_match : bir özellik

    body={
        "query":{
            "multi_match":{
                "query":keyword,
                "fields":["content","title"]
            }
        }
    }   

    result=connection.search(index='contents',doc_type="title",body=body)
    return jsonify(result['hits']['hits'])


app.run(port=5001,debug=True)



# doc = {
#     'author': 'kimchy',
#     'text': 'Elasticsearch: cool. bonsai cool.',
#     'timestamp': datetime.now(),
# }
# res = es.index(index="test-index", id=1, body=doc)
# print(res['result'])

# res = es.get(index="test-index", id=1)
# print(res['_source'])

# es.indices.refresh(index="test-index")

# res = es.search(index="test-index", body={"query": {"match_all": {}}})
# print("Got %d Hits:" % res['hits']['total']['value'])
# for hit in res['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])