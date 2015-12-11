### RESTfull services implementation

###### Requirements:
* Python
* Flask framework  
    * http://flask.pocoo.org/
    * to install execute: `pip install flask`

###### Execution:
To test the services, navigate to the folder of your preference and start the server by executing: `python <server_file_name>.py`

After the server is running you can:
* call it from your browser by requesting: http://localhost:<PORT>
* invoke it from terminal using [curl](http://man.cx/curl)

###### Examples:
Some more examples of the features implemented.  
Execute the following commands after the server side is running:
    
`curl -i http://localhost:<PORT>`  
This command sends a GET request  
`curl -i http://localhost:<PORT>/<url_path>`  
This command sends a GET request of a specific url_path  
`curl -i http://localhost:<PORT>/<url_path> -X DELETE -v`  
 This command sends a DELETE request of a specific url_path  
 `curl -i http://localhost:<PORT>/<url_path> -d "<attr1>=<value1>&<attr2>=<value2>" -X POST -v`  
 This command sends a POST request of a specific url_path with the data specified after the -d option, separated by an ampersand "&"
