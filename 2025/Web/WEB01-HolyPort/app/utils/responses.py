from flask import Response, make_response

# Returned response contained a location header that should redirect the user to the login page
def location_header_response(reroute_path: str) -> Response:
    response = make_response("", 302)
    response.headers['Location'] = reroute_path
    return response

