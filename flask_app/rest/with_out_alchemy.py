

from flask import Blueprint, jsonify, request
from data.connection import get_db_connection

app = Blueprint('with_out_alchemy', __name__)



@app.route('/woa/get/<profile_id>')
def get_profile(profile_id):

    conn = get_db_connection()
    profile = conn.execute('SELECT * FROM profile WHERE id = ?', (profile_id,)).fetchone()
    conn.close()

    if profile is None:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify(dict(profile))
