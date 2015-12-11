#############################################
#                CLIENT                     #
## Service 1: Convert currency from Canadian Dollar to American dollar and Indian Rupee #
#############################################

from pysimplesoap.client import SoapClient, SoapFault
# create a simple consumer
client = SoapClient(
    location = "http://localhost:8020/",
    action = 'http://localhost:8020/', # SOAPAction
    namespace = "http://example.com/sample.wsdl",
    soap_ns='soap',
    trace = True,
    ns = False)
#ask user for input
var1 = raw_input("Enter currency in Canadian dollar ")
print "\nCalling the Service...\n"

# call the remote method
response = client.crcy( c =  var1)

result = response.AddResult

print "\n\nYour crcy is",  float(result)


