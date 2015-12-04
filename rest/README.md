### RESTfull services implementation

###### Requirements:
* Python
* Flask framework  
    * http://flask.pocoo.org/
    * to install execute: `pip install flask`

###### Execution:
To test locally, start the server by executing: `python server_rest.py`

After the server is running you can:
* call it from your browser by requesting: <http://localhost:5000>
* invoke it from terminal using [curl](http://man.cx/curl)

###### Examples:
Some more examples of the features implemented.  
Execute the following commands after the server side is running:
    
`curl -i http://localhost:5000`  
This command sends a GET request and the server returns the String "Hello World!"  
`curl -i http://localhost:5000/softEng/api/v1`  
This command sends a GET request and the server returns a string that was specified in the server side code  
`curl -i http://localhost:5000/softEng/api/v1/2`  
 This command sends a GET request and the server returns the last number in the command (2 in this case) squared  
