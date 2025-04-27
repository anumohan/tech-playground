




'''

🚀 Flask Terms and Technical Jargons
Flask has its own set of terminologies that can be a bit confusing at first. 
Let’s break down the most important terms and jargons you might encounter while working with Flask.

📝 1. Route
A route in Flask is a URL pattern that is associated with a specific function, known as a view function. 
It tells Flask which URL should trigger a particular function.

@app.route('/hello')
def hello():
    return "Hello, World!"
Here, /hello is the route, and it triggers the hello() function.

📝 2. View Function
A view function is a Python function that handles the logic for a given route. It returns the HTTP response to be sent to the client.
💡 Example:
@app.route('/greet')
def greet():
    return "Welcome to Flask!"
The greet() function is the view function for the /greet route.

📝 3. Endpoint
An endpoint is the unique identifier for a view function. By default, it is the name of the function itself.
💡 Example:
@app.route('/profile', endpoint='user_profile')
def profile():
    return "User Profile"
The endpoint here is user_profile.

📝 4. URL Rule
The URL rule is the string pattern in the @app.route() decorator that defines the path part of the URL.
💡 Example:
@app.route('/user/<username>')
def show_user(username):
    return f"User: {username}"
URL Rule: /user/<username>
Dynamic part: <username> which is a URL variable.

📝 5. URL Variable
A URL variable is a dynamic part of the URL pattern that can capture variable data from the URL.
💡 Example:
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post ID: {post_id}"
The <int:post_id> part is a URL variable that accepts integers.

📝 6. Request Object
The request object in Flask represents the incoming HTTP request. It contains data like headers, form data, JSON data, and more.
💡 Example:
from flask import request
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f"Hello, {name}!"
request.form['name'] accesses the submitted form data.

📝 7. Response Object
The response object represents the HTTP response that the server sends back to the client. Flask view functions can return strings, 
dictionaries (JSON), or even a complete response object.
💡 Example:
from flask import jsonify
@app.route('/data')
def data():
    return jsonify({"message": "Hello, World!"})
The jsonify function returns a Response object with a JSON body.


📝 8. Templates
Templates are HTML files that can dynamically generate content using Jinja2 syntax.
💡 Example:
<!-- templates/home.html -->
<h1>Hello, {{ name }}!</h1>
@app.route('/home')
def home():
    return render_template('home.html', name='Alice')


📝 9. Jinja2
Jinja2 is a templating engine used in Flask to render HTML with dynamic content. It allows embedding Python code within HTML files.

💡 Example:
{% for user in users %}
    <p>{{ user.name }}</p>
{% endfor %}


📝 10. Blueprint
Blueprints are used to organize routes and views into separate components or modules. They help in modularizing larger applications.
💡 Example:
from flask import Blueprint
user_bp = Blueprint('user', __name__)
@user_bp.route('/profile')
def profile():
    return "User Profile"
You register a blueprint in the main app:
app.register_blueprint(user_bp)


📝 11. Middleware
Middleware is a function or class that intercepts requests and responses. It can be used for logging, authentication, or modifying responses.
💡 Example:
@app.before_request
def log_request():
    print("Request made to:", request.path)


📝 12. Context
Contexts in Flask refer to objects that are only valid during a request or application context. There are two types:
Request Context: Handles request, session, and more.
Application Context: Handles g and current_app.
💡 Example:
from flask import g
@app.before_request
def setup():
    g.user = "John"


📝 13. Session
Session is used to store data for individual users between requests. It is stored on the client side using secure cookies.
💡 Example:
from flask import session
@app.route('/login')
def login():
    session['username'] = 'John'
    return "Logged in"


📝 14. Static Files
Static files are CSS, JS, and images stored in the /static directory.
💡 Example:
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">


📝 15. Debug Mode
Debug mode in Flask automatically reloads the server on code changes and provides an interactive debugger on errors.
💡 Example:
app.run(debug=True)


📝 16. WSGI (Web Server Gateway Interface)
WSGI is the standard for Python web applications. Flask apps are WSGI applications and are typically served using a WSGI server like Gunicorn or uWSGI.
💡 Example: Running with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app


📝 17. RESTful API
A RESTful API in Flask is an API that follows REST principles and uses HTTP methods like GET, POST, PUT, and DELETE.
💡 Example:
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify({"message": "User created", "user": data}), 201


📝 18. Flask Extensions
Flask extensions are third-party libraries that add functionality to Flask.
💡 Examples:
Flask-SQLAlchemy: For database handling.
Flask-Migrate: For database migrations.
Flask-Session: For server-side sessions.


📝 19. Configurations
Flask allows setting up configurations using the app.config object.
💡 Example:
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mysecretkey'


📝 20. Gunicorn
Gunicorn is a WSGI HTTP Server for running Python web applications in production.
💡 Running with Gunicorn:
gunicorn -w 4 -b 0.0.0.0:8000 app:app

'''






'''

✅ How to Make Flask Sessions More Secure

🔒 1. Use a Strong Secret Key
import os
app.secret_key = os.urandom(32)  # Generates a 32-byte random key
app.config['SECRET_KEY'] = os.urandom(32)


🔒 2. Use HTTPS Only (SSL/TLS)
Always enable HTTPS to encrypt data during transit.
app.config['SESSION_COOKIE_SECURE'] = True  # Ensures cookies are only sent over HTTPS


🔒 3. Enable HTTPOnly Cookies
Prevent JavaScript from accessing the session cookie.
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Prevents JavaScript access


🔒 4. Use SameSite Cookies
Restricts sending cookies with cross-site requests to prevent Cross-Site Request Forgery (CSRF).
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # or 'Strict'


🔒 5. Regularly Rotate Secret Keys
Regenerate your secret key periodically to limit the impact of key compromise.



🔒 6. Avoid Storing Sensitive Data in Sessions
Avoid storing sensitive information like passwords or credit card details.
session['username'] = 'john_doe'  # Safe
session['password'] = 'supersecret'  # ❌ Dangerous


🔒 7. Use Server-Side Session Stores
Instead of relying on client-side cookies, store sessions server-side using:
- Redis
- Memcached
- Database (SQLAlchemy)


🔒 8. Regenerate Session ID on Login
Prevent session fixation attacks by regenerating the session ID when a user logs in.
from flask import session

@app.route('/login', methods=['POST'])
def login():
    session.pop('_flashes', None)  # Clear existing session data
    session['user_id'] = 123
    session.permanent = True
    return "Logged in successfully"


🔒 9. Implement Session Timeout
Automatically expire sessions after a period of inactivity.
from datetime import timedelta
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)


🔒 10. Clear Sessions on Logout
Explicitly clear session data when the user logs out.
@app.route('/logout')
def logout():
    session.clear()  # Clear all session data
    return "You have been logged out"




'''

