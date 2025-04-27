from flask import Flask, render_template, Blueprint, jsonify, request, session, redirect, url_for
from service.profile_service import ProfileService

app = Blueprint('profile_controller', __name__)


@app.route('/profile/list/', methods=['GET'])
@app.route('/profile/list')
def list_profile():
    service = ProfileService()
    profiles = service.list_profile()
    return render_template('profile/index.html', profiles=profiles)




@app.route('/profile')
#@app.route('/profile/')
def index():
    username = session.get('username')
    if username:
        return f"Hello, {username}! Welcome back!"
    return "Hello, Guest!"


@app.route('/profile/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('profile_controller.index'))

    if session and session['username']:
        return redirect(url_for('profile_controller.index'))
        
    return render_template('profile/login.html')    


@app.route('/profile/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('profile_controller.index'))    


# name = request.form['name']
# user_name = request.args.get('user_name')   ?username=anu 