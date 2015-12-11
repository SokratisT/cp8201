from pysimplesoap.client import SoapClient, SoapFault

# create a simple consumer
client = SoapClient(
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", 
    soap_ns='soap',
    trace = True,
    ns = False)

#ask user for input
var1 = raw_input("Please give the first number to be added: ")
var2 = raw_input("Please give the second number to be added: ")

print "\nCalling the Service...\n"

# call the remote method
response = client.Adder( a = var1, b = var2)

# extract and convert the returned value
result = response.AddResult

print "The result is: ",  int(result)
