from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

students_db = {
    '1': {'s_id': 1, 
        'name': u'Sokratis',
        'courses': ['cp8202', 'cp8301'],
        'department': u'Computer Science',
        'status': u'In Progress'
    },
    '2': {'s_id': 2,
        'name': u'Jorge',
        'courses': ['cp8202', 'cp8301'],
        'department': u'Computer Science',
        'status': u'In Progress'
    },
    '3': {'s_id': 3,
        'name': u'Sorrur',
        'courses': ['cp8202', 'cp8301'],
        'department': u'Computer Science',
        'status': u'In Progress'
    },
    '4': {'s_id': 4,
        'name': u'Jaspal',
        'courses': ['cp8202', 'cp8301'],
        'department': u'Computer Science',
        'status': u'In Progress'
    }
}


def abort_request(s_id):
    if s_id not in students_db:
        abort(404, message="Student with id {} doesn't exist".format(s_id))

# define the parameters that the api can take
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name of the student')
parser.add_argument('courses', type=str, help='List of the courses this term')
parser.add_argument('department', type=str, help='Department enrolled in')
parser.add_argument('status', type=str, help='Current status of the student')


# Specific students
# returns, removes and edits specific students by their id
class students(Resource):
    # curl -i http://localhost:1333/students/1
    # returns the specific student specified by its id
    def get(self, s_id):
        abort_request(s_id)
        return students_db[s_id]

    # curl http://localhost:1333/students/1 -X DELETE -v
    # removes a student from the db
    def delete(self, s_id):
        abort_request(s_id)
        del students_db[s_id]
        return '', 204

    #curl -i http://localhost:1333/students/1 -d "name=John&department=CS&courses=cp1203,asd123&status=live" -X POST -v
    # edits specific fields from a student
    def put(self, s_id):
        args = parser.parse_args()
        if args['name']:
            students_db[s_id]['name'] = args['name']
        if args['department']:
            students_db[s_id]['department'] = args['department']
        if args['courses']:
            students_db[s_id]['courses'] = args['courses'].split(",")
        if args['status']:
            students_db[s_id]['status'] = args['status']

        return students_db[s_id], 201


# studentsList
# shows a list of all students and allows to add (POST) new
class studentsList(Resource):
    # curl -i http://localhost:1333/students
    # just returns the entire db
    def get(self):
        return students_db

    # adds a new entry in the students_db
    # curl -i http://localhost:1333/students -d "name=David&department=cs&courses=cp1203,asd123&status=In Progress" -X POST -v
    def post(self):
        args = parser.parse_args()
        s_id = int(max(students_db.keys())) + 1

	# convert strig parameter to list of strings
        courses_conv = args['courses'].split(",")

        students_db[s_id] = {'s_id': s_id, 'name': args['name'], \
                             'courses': courses_conv, 'department': args['department'], \
                             'status': args['status']}
        return students_db[s_id], 201

##
## Actually setup the Api resource routing here
#
api.add_resource(studentsList, '/students')
api.add_resource(students, '/students/<s_id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = int('1333'), debug=True)
