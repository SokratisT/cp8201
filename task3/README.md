##Computer_Science_Registry

This is a service for the requirements of the third task of the term's project.

The registry service was developed by the team and an extrnal API was used in order to achieve the service composition. The name of the external API is [Mixpanel](https://mixpanel.com) and it is a data analytics service.

####Registry service:
The registry service implements a registry/database of students of a specific department and provides to the user the ability to make certain operations on it.

Since the project was not meant to test our skills in database administration we used a dictionary data structure (python dictionary) to store the students and their properties. Python dictionaries are also easily converted into JSON (JavaScript Object Notation). The key for each record in the dictionary is the student’s ID which is unique and auto-incremented. The attributes of each student/record are the following:
* s_id – student’s ID, unique and auto-incremented
* name – name of the student
* courses – courses currently enrolled or completed
* department – department that the student is enrolled
* status – current status of the student

####Service composition
The composition was succeeded by calling the analytics service, with the required parameters, every time the primary service (Computer_Science_Registry) is invoked. The data analytics service, provides a user interface that we can access and monitor the main service usage.
