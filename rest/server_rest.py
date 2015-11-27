#!flask/bin/python
from flask import Flask, jsonify
from flask import make_response

app = Flask(__name__)

# most simple case - just returns 'Hello World' when called
# to call : 
# curl -i http://localhost:5000
@app.route('/')
def index():
    return "Hello, World!"

# another simple case when calling the URI of the service
# to call :
# curl -i http://localhost:5000/softEng/api/v1
@app.route('/softEng/api/v1', methods=['GET'])
def get_s1():
    return "empty call of our api\n"

# returns the squared value of the number
# to call :
# curl -i http://localhost:5000/softEng/api/v1/2
@app.route('/softEng/api/v1/<int:var1>', methods=['GET'])
def get_s2(var1):
    res = var1**2
    return str(res) + '\n'

# POST example
@app.route('/softEng/api/v1', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.errorhandler(404)
def handle_errors(error):
    return make_response(jsonify({'error': 'Something went wrong...'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
