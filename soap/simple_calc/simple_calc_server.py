from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer

def adder(a,b):
    "Add two numbers"
    return a+b

def subtractor(a,b):
    "Subtract two numbers"
    return a-b

def multiplier(a,b):
    "Multiply two numbers"
    return a*b

def divider(a,b):
    "Divide two numbers"
    return str(a/b)

dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", prefix="ns0",
    trace = True,
    ns = True)

# register the user functions
dispatcher.register_function('Add', adder,
    returns={'AddResult': int}, 
    args={'a': int,'b': int})

dispatcher.register_function('Sub', subtractor,
    returns={'SubResult': int},
    args={'a': int,'b': int})

dispatcher.register_function('Mul', multiplier,
    returns={'MulResult': int},
    args={'a': int,'b': int})

dispatcher.register_function('Div', divider,
    returns={'DivResult': str},
    args={'a': int,'b': int})

print "Starting server..."
httpd = HTTPServer(("", 8008), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()
