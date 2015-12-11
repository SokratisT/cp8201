#########################################################
#							#
# Client program based in SOAP for RMS calculation      #
#							#
#########################################################
from pysimplesoap.client import SoapClient, SoapFault


# create a simple consumer
client = SoapClient(
    location = "http://localhost:8010/",
    action = 'http://localhost:8010/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", 
    soap_ns='soap',
    trace = True,
    ns = False)

#ask user for input
print "\nCALCULATION OF MEAN SQUARE ROOT OT TWO NUMBERS\n\n"
var1 = raw_input("Please give the first number to be calculated: ")
var2 = raw_input("Please give the second number to be calculated : ")

print "\nCalling the Service...\n"

# call the remote method
response = client.rmses( a = var1, b = var2)
response1 = client.amean( a = var1, b = var2)

# extract and convert the returned value
result = response.AddResult
result1 = response1.AddResult1

print "\nThe First number is:", var1
print "\nThe Second number is:", var2
print "\nThe Root Mean Square is: ", float(result)
print "\nThe Arithmatic Mean is: ", float(result1)
