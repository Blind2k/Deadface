from flask import Flask, request, render_template_string
from dotenv import load_dotenv
import os
from utils.request_helpers import valuate_port_from_header, return_login_page
from utils.responses import location_header_response

# Simulated port routes based on Host header (e.g. 127.0.0.1:8001)
from utils.port_routes_collection import PORT_ROUTES

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

FLAG = os.getenv('FLAG')
LHOST = "0.0.0.0"
LPORT = int(os.getenv('LPORT'))
DEBUG = os.getenv('DEBUG')

#### SERVER STARTS
# Server returns random text, or a location header on specific ports.
@app.route('/', methods=['GET'])
def index():
    target_port = valuate_port_from_header()
    if target_port in [80, 4644, 6776, 18000, 32000, 65445]:
        return location_header_response('/logMeInPlz')
    else:
        content = PORT_ROUTES.get(target_port, "Unknown port. Nothing to see here.")
        return render_template_string("<h2>{{content}}</h2>", content=content)


# To solve this challenge, user should use the POST method
@app.route('/logMeInPlz', methods=['GET'])
def respond_request():
    return return_login_page()


# The flag will return from this function
@app.route('/logMeInPlz', methods=['POST'])
def login():
    import hashlib, hmac
    port = valuate_port_from_header()

    try:
        port = int(port)
    except Exception:
        return return_login_page(418) # Edge-case

    form = request.form
    request_username = form.get("username", "").strip()
    request_password = form.get("password", "").strip()
    print(request_username)
    print(request_password)

    # If the server failed to get the body return BAD REQUEST
    if not (request_username and request_password):
        return return_login_page(400)

    # compute hashes
    username_hash = hashlib.md5(request_username.encode()).hexdigest()
    password_hash = hashlib.md5(request_password.encode()).hexdigest()

    # expected hashes (keep them outside or in config/env)
    expected_user_hash = os.getenv('USER_NAME')         # md5("username")
    expected_pass_hash = os.getenv('USER_PASSWORD')     # md5("password")

    # constant-time compare
    user_ok = hmac.compare_digest(username_hash, expected_user_hash)
    pass_ok = hmac.compare_digest(password_hash, expected_pass_hash)
    print(username_hash)
    print(expected_user_hash)
    print(user_ok)
    
    print(password_hash)
    print(expected_pass_hash)
    print(pass_ok)
    if user_ok and pass_ok and port == 18000:
        return render_template_string(f"<p>✅ Success! Flag: {FLAG}</p>")

    # Wrong credentials & wrong port return NOT FOUND
    return return_login_page(404)


if __name__ == '__main__':
    app.run(debug=DEBUG, host=LHOST, port=LPORT)
