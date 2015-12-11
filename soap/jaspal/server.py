#################################################################
##                         SERVER                               #
##                                                              #
## Service 1: Convert currency from Canadian Dollar to American dollar and Indian Rupee #
##                                                              #
#################################################################
from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer
def crcy(c):
    "Calculating currency exchange"
    return (49.85*c)      
dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8020/",
    action = 'http://localhost:8020/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", prefix="ns0",
    trace = True,
    ns = True)
# register the user function
dispatcher.register_function('crcy', crcy,
    returns={'AddResult': float},
    args={'c': float}) ## args type float

print "Starting server..."
httpd = HTTPServer(("", 8020), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()

