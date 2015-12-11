#################################################
#	Server SOAP based model			#
#################################################
from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer

def rmses(a,b):
    "Calculate RMSE of two values"
    meana = (a*a + b*b)/2
    mval = (meana)**(0.5)
    return mval

def amean(a,b):
    "Calculate Mean of two values"
    meana1 = (a + b)/2
    return meana1

dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8010/",
    action = 'http://localhost:8010/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", prefix="ns0",
    trace = True,
    ns = True)

# register the user function
dispatcher.register_function('rmses', rmses,
    returns={'AddResult': float}, 
    args={'a': float,'b': float})

dispatcher.register_function('amean', amean,
    returns={'AddResult1': float}, 
    args={'a': float,'b': float})

print "Starting server..."
httpd = HTTPServer(("", 8010), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()
#################################################
#	Server SOAP based model			#
#################################################
from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer

def rmses(a,b):
    "Calculate RMSE of two values"
    meana = (a*a + b*b)/2
    mval = (meana)**(0.5)
    return mval

def amean(a,b):
    "Calculate Mean of two values"
    meana1 = (a + b)/2
    return meana1

dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8010/",
    action = 'http://localhost:8010/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", prefix="ns0",
    trace = True,
    ns = True)

# register the user function
dispatcher.register_function('rmses', rmses,
    returns={'AddResult': float}, 
    args={'a': float,'b': float})

dispatcher.register_function('amean', amean,
    returns={'AddResult1': float}, 
    args={'a': float,'b': float})

print "Starting server..."
httpd = HTTPServer(("", 8010), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()
