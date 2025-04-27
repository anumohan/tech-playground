from flask import Flask, request
from data.connection import db

from rest.index import app as main_bp
from rest.with_out_alchemy import app as woa_bp
from controllers.profile_controller import app as profile_bp

from rest.middlewares.timing_middleware import TimingMiddleware

# using Flask’s Built-in Middleware Hooks
def create_built_in_middleware_hooks(app):
    #This middleware runs before any request is processed.
    @app.before_request
    def log_before_request():
        print(f"🚀 Incoming Request: {request.method} {request.path}")

    # This middleware runs after a request is processed and before the response is sent.
    @app.after_request
    def log_after_request(response):
        print(f"✅ Processed Request: {request.method} {request.path}")
        return response

    
    #Runs after the request is completed, even if an exception occurs.
    @app.teardown_request
    def close_db_connection(exception):
        """Middleware to clean up after each request"""
        print("🔄 Closing database connection...")        
        
        

def create_app():
    app = Flask(__name__)

    # handle trailing slashes globally
    app.url_map.strict_slashes = False

    app.testing = True


    # Setting Custom Template Folder
    #app = Flask(__name__, template_folder='my_templates')

    # Set a secret key for signing the session cookie
    app.secret_key = "supersecretkey123"  # Always keep it secret and complex
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\\working\\github\\anumohan\\tech-playground\\flask_app\\test.db'

    
    # Create Flask app and wrap with middleware
    create_built_in_middleware_hooks(app)
    app.wsgi_app = TimingMiddleware(app.wsgi_app)

    db.init_app(app)  # Initialize database with app
    with app.app_context():
        #db.create_all()  # Ensure tables exist
        pass


    app.register_blueprint(main_bp)
    app.register_blueprint(woa_bp)
    app.register_blueprint(profile_bp)

    return app


app = create_app()



if __name__ == "__main__":
    app.run(debug=True, threaded=True)
    

'''
Run in Windows
-----------------------------------------------
set FLASK_APP=app.py
set PYTHONPATH=D:\working\tryouts\flask_app
flask run
-----------------------------------------------

export FLASK_APP=app.py - Linux/macOS
set FLASK_APP=app.py - Windows (Command Prompt)
$env:FLASK_APP="app.py"  - Windows (PowerShell)
flask run --host=0.0.0.0 --port=8080

Running Flask with Gunicorn (Production)
gunicorn -w 4 -b 0.0.0.0:5000 app:app

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