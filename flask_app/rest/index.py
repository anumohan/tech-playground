
from service.profile_service import ProfileService
from flask import Blueprint, jsonify, request
from rest.validator.validator import validate_profile_input
import time

app = Blueprint('index', __name__)



@app.route('/')
def check():
    time.sleep(20)
    return 'Flask is working'

@app.route('/sleep/<int:seconds>')
def get_time(seconds):
    print(f'sleeping {seconds} seconds')
    time.sleep(seconds)
    return 'Sleeped {0}'.format(seconds)



@app.route('/get/<profile_id>')
def geT_profile(profile_id):
    service = ProfileService()
    return  jsonify(service.get_profile_by_query(profile_id))




@app.route('/profile/list', methods=['GET'])
def list_profile():
    service = ProfileService()
    profiles = service.list_profile()
    return jsonify(profiles)


@app.route('/profile/add', methods=['PUT', 'POST'])
@validate_profile_input
def add_profile():

    data = request.get_json() 
    if not data or 'first_name' not in data or 'last_name' not in data or 'age' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    service = ProfileService()


    first_name = data.get('first_name')
    last_name = data.get('last_name')
    age = data.get('age')

    if not service.get_profile_by_name(first_name):
        service.create_profile(first_name = first_name, last_name = last_name, age=age)
        return jsonify({'status': 'success', 'message': 'New profile created'})
    else:
        return jsonify({'status': 'error', 'message': 'Profile already exists!'}), 409

    '''
    curl -X PUT http://127.0.0.1:5000/profile/add \
        -H "Content-Type: application/json" \
        -d '{"first_name": "Simba", "last_name": "M", "age": 5}'
    '''



@app.route('/profile/<int:profile_id>', methods=['GET'])
def get_profile(profile_id):

    email_only = request.args.get('email_only', 'false').lower() == 'true'


    service = ProfileService()
    return jsonify(service.get_profile_by_id(profile_id))



@app.route('/profile/<int:profile_id>', methods=['DELETE'])
def delete_profile(profile_id):
    service = ProfileService()
    if service.get_profile_by_id(profile_id):
        deleted = service.delete_profile_by_id(profile_id)
        return jsonify({'status': 'success', 'message': deleted})
    else:
        return jsonify({'status': 'error', 'message': "Profile doesn't exists!"}), 400


    '''
    curl -X DELETE http://127.0.0.1:5000/profile/2 
    '''