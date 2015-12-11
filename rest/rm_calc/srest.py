#################################################################
#		Server for RESTful model       			#
#################################################################
#!flask/bin/python& flask is a microframework for python based on Werkzeug and Jinja 2
#
from flask import Flask, jsonify 
from flask import make_response

app = Flask(__name__)

# most simple case - just returns Welcome message' when called
# to call : 
# curl -i http://localhost:8010
@app.route('/')
def index():
  return "WELCOME  TO RESTFUL SERVICE DEMONESTRATION\n\n"

# another simple case when calling the URI of the service
# to call :
# curl -i http://localhost:8010/softEng/api/v1
@app.route('/softEng/api/v1', methods=['GET'])
def get_s1():
    return "\nReturning String test\n"

# returns the Root Mean squared value and arithmatic mean value of two real numbers
# to call :
# curl -i http://localhost:8010/softEng/api/v1/2
@app.route('/softEng/api/v1/<float:var1>,<float:var2>', methods=['GET'])
def get_s2(var1,var2):
    meana = (var1*var1 + var2*var2)/2
    rmsm = (meana)**(0.5)
    amean = (var1 + var2)/2
    return '\nCalculation of RMS and Arithmatic mean values\n'+ '\nTwo Values are = ' + str(var1) + ' and ' + str(var2) +'\n' + '\nRMS Value  = ' + str(rmsm) + '\nArithmatic mean value = ' + str(amean) +'\n'


# POST example
@app.route('/softEng/api/v1', methods=['POST'])
def add_in_table():
    if not request.json:
        abort(400)
    return "success", 201

@app.errorhandler(404)
def handle_errors(error):
    return make_response(jsonify({'error': 'Something went wrong...'}), 404)

if __name__ == '__main__':
    app.run(debug=True, port=int("8010"))
