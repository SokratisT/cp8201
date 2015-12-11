#!flask/bin/python
from flask import Flask, jsonify
from flask import make_response

app = Flask(__name__)

#---------------------------------------------------------------------------------------------
# to call :
# curl -i http://localhost:8012/bmicalc/<val1>,<val2>
@app.route('/bmicalc/<float:w>,<float:h>', methods=['GET'])
def get_bmicalc(w,h):
  
  r = w/h

  if r<=18.5:
       Cat='UNDERWEIGHT'
  elif (r > 18.5) and (r < 25):
       Cat='NORMAL'
  else:
       Cat = 'OVERWEIGHT'

  return '\nYour bmi index is '+ str(r)+' your category is  ' + Cat+'\n'



#---------------------------------------------------------------------------------------------
@app.errorhandler(404)
def handle_errors(error):
    return make_response(jsonify({'error': 'Something went wrong...'}), 404)

if __name__ == '__main__':
    app.run(debug=True, port=int("8012"))
