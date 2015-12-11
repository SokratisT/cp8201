
from flask import Flask, jsonify
from flask import make_response

app = Flask(__name__)

# to call : 
## from terminal: curl -i http://http://54.175.118.36:1339/
## from browser: http://54.175.118.36:1339/
@app.route('/')
def root_1():
    return "Go to http://54.175.118.36:1339/index.html to get more information!\n"

# index.html
# to call :
## from terminal curl -i http://http://54.175.118.36:1339/index.html
@app.route('/index.html', methods=['GET'])
def index_1():
    return "This is our index page. TODO: put some more information here\n"

# returns the currency in Indian rupee
# to call :
## from terminal: curl -i http://localhost:5000/softEng
@app.route('/softEng/<int:c>', methods=['GET'])
def get_s2(c):
    res =49.85*c
    return "The currency in Indian rupee is " + str(res) + '\n'

# POST example
@app.route('/postbmi', methods=['POST'])

def CreateBMI():
    print "\n in POST \n"
    return "POST method called"
    if not request.json:
        abort(400)
    return "success", 201

@app.errorhandler(404)
def handle_errors(error):
    return make_response(jsonify({'error': 'Something went wrong...'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int("1339"), debug=False)
