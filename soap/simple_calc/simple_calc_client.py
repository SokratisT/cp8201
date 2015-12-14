from pysimplesoap.client import SoapClient, SoapFault

# create a simple consumer
client = SoapClient(
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", 
    soap_ns='soap',
    trace = False,
    ns = False)

#ask user for input
var1 = raw_input("Please give the first number: ")
var2 = raw_input("Please give the second number: ")

print "\nCalling the Service...\n"

# call the remote services
response1 = client.Add(a = var1, b = var2)
response2 = client.Sub(a = var1, b = var2)
response3 = client.Mul(a = var1, b = var2)
response4 = client.Div(a = var1, b = var2)

# extract and convert the returned value
result1 = response1.AddResult
result2 = response2.SubResult
result3 = response3.MulResult
result4 = response4.DivResult

print "\nAddition: ",  int(result1)
print "Subtraction: ",  int(result2)
print "Multiplication: ",  int(result3)
print "Division: ",  float(result4)
