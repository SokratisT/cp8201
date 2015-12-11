#################################################################
##                         SERVER                               #
##                                                              #
## Service 1: Calculate BMI given entered weight and Height     #
##                                                              #
#################################################################
from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer
def bmi(w,h):
    "Calculating BMI"
    return w/h
	
def bmiC(r):
    "Calculating BMI"
    if r<=18.5:
       Cat='UNDERWEIGHT'
    elif (r > 18.5) and (r < 25):
       Cat='NORMAL'
    else:
       Cat = 'OVERWEIGHT'
    
    return Cat
       
dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8012/",
    action = 'http://localhost:8012/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", prefix="ns0",
    trace = True,
    ns = True)
# register the user function
dispatcher.register_function('Bmi', bmi,
    returns={'AddResult': float},
    args={'w': float,'h': float}) ## args type float
# register the user function 2
dispatcher.register_function('BmiC', bmiC,
    returns={'CatResult': str}, ## changed to str!
    args={'r': float}) ## arg type float
	
print "Starting server..."
httpd = HTTPServer(("", 8012), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()
