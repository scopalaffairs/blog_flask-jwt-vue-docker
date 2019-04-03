from flask import Flask
from flask import jsonify
from flask_cors import CORS
from redis import Redis

# ===[ Flask ]===
app = Flask(__name__)
redis = Redis(host='redis', port=6379)

CORS(app)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


# ===[ Index Router ]===
@app.route("/")
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


# ===[ Main App ]===
if __name__ == '__main__':
    app.run(host="0.0.0.0")
