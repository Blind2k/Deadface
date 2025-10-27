from flask import request, render_template, make_response, Response, render_template_string
from utils.validators import is_real_int


# Grab the port number from the Host header.
def valuate_port_from_header(default: int = 8000) -> int:
    port = request.headers.get("X-Forwarded-Port", "").strip()
    return int(port) if port.isdigit() else default


# This will determine, according the port number, which page should be served to the end-user
def return_login_page(status_code:int=200) -> Response:
    target_port = valuate_port_from_header()
    match target_port:
        case 80:
            return make_response(render_template('login001.html'), status_code)
        case 4644:
            return make_response(render_template('login002.html'), status_code)
        case 6776:
            return make_response(render_template('login003.html'), status_code)
        case 18000:
            return make_response(render_template('login004.html'), status_code)
        case 32000:
            return make_response(render_template('login005.html'), status_code)
        case 65445:
            return make_response(render_template('login006.html'), status_code)
        case _:
            return render_template_string(f"<p>No. I don't know this port</p>")

