from flask import Flask, request, jsonify
from werkzeug.routing import Rule
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Allow custom HTTP method 'LOGIN'
app.url_map.add(Rule('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'LOGIN', 'OPTIONS'], endpoint='challenge'))

# Get configuration from environment variables
FLAG = os.getenv('FLAG')
LHOST = "0.0.0.0"
LPORT = int(os.getenv('LPORT'))
DEBUG = os.getenv('DEBUG')

# Helper function to build JSON response
def build_returned_json(message_to_return: str, status: str="error"):
    response = {
        "status": status,
        "message": message_to_return,
    }
    return jsonify(response)


# Function to validate headers
def check_header(target_header: str, good_header_value: str, wrong_message_value: str, response_status: int = 403):
    """
    Check if a header matches the expected value.
    Returns (response, status_code) tuple if validation fails, None if passes.
    """
    target_header_value = request.headers.get(target_header, '').lower()
    if target_header_value == good_header_value.lower():
        return None
    return build_returned_json(wrong_message_value), response_status


@app.endpoint('challenge')
def challenge():
    # Handle OPTIONS request - reveal the LOGIN method
    if request.method == 'OPTIONS':
        response = app.make_response(('', 200))
        response.headers['Allow'] = 'GET, POST, PUT, DELETE, OPTIONS, LOGIN, TRACE, CONNECT'
        return response
    
    # Stage 0: Check HTTP method
    if request.method != 'LOGIN':
        return build_returned_json(
            "Ah?! What is this method?"
        ), 405
    
    # Stage 1: Check User-Agent
    result = check_header(
        'User-Agent',
        'smith',
        'You are not agent smith!'
    )
    if result:
        return result
    
    # Stage 2: Check X-Location
    result = check_header(
        'Location',
        'Germany',
        'Sorry. You are not in Germany!'
    )
    if result:
        return result
    
    # Stage 3: Check Age
    result = check_header(
        'Age',
        '30',
        'Delta-secounds should be 0'
    )
    if result:
        return result
    
    # Stage 4: Check Prefer
    result = check_header(
        'Origin',
        'http://127.1',
        'Origin should be local'
    )
    if result:
        return result
    
    # Stage 5: Check X-XSS-Protection
    result = check_header(
        'X-XSS-Protection',
        '0',
        'XSS protection is ON!'
    )
    if result:
        return result

    # Stage 6: Check DNT
    result = check_header(
        'DNT',
        'null',
        'You are being tracked'
    )
    if result:
        return result

    # Stage 7: Check X-Frame-Options
    result = check_header(
        'X-Frame-Options',
        'DENY',
        "We don't like frames here!"
    )
    if result:
        return result
    
    # Stage 8: Check Pragma
    result = check_header(
        'Pragma',
        'no-cache',
        'NOOOO!!!! Old-school caching is enabled!!'
    )
    if result:
        return result
    
    # Stage 9: Check Sniffing!
    result = check_header(
        'X-Content-Type-Options',
        'nosniff',
        'Possible sniffing is happening right now!'
    )
    if result:
        return result
    
    # Stage 10: Override method!
    result = check_header(
        'X-HTTP-Method-Override',
        'GET',
        'Override is required to get the flag'
    )
    if result:
        return result
    
    # All checks passed - return the flag!
    return build_returned_json(
        FLAG,
        status="success",
    ), 200


if __name__ == '__main__':
    app.run(debug=DEBUG, host=LHOST, port=LPORT)
