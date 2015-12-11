#############################################
#                CLIENT                     #
# Service 1: BMI calculator                 #
# Given your weight and height returns      #
# your BMI index and the category you fall  #
# in                                        #
#############################################
from pysimplesoap.client import SoapClient, SoapFault
# create a simple consumer
client = SoapClient(
    location = "http://localhost:8012/",
    action = 'http://localhost:8012/', # SOAPAction
    namespace = "http://example.com/sample.wsdl",
    soap_ns='soap',
    trace = True,
    ns = False)
#ask user for input
var1 = raw_input("Enter your weight in pounds: ")
var2 = raw_input("Enter your height in feets:")
print "\nCalling the Service...\n"
# call the remote method
response = client.Bmi( w = var1, h = var2)
result = response.AddResult
# call the remote method
response = client.BmiC( r = result )
resultC = response.CatResult

print "\n\nYour BMI is:",  float(result)
print "\n\nYour Category is:", str(resultC)
