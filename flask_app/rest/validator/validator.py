
from flask import request, jsonify
from functools import wraps


def validate_profile_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('IN Validator.............')
        data = request.get_json()
        if not data or 'first_name' not in data or 'last_name' not in data or 'age' not in data:
            return jsonify({"error": "Missing required fields in validator"}), 400

        return func(*args, **kwargs)
    return wrapper
