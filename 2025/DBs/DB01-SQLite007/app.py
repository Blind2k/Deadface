from flask import Flask, request, session, redirect, url_for, render_template, jsonify
import sqlite3
import os
import logging
from dotenv import load_dotenv
from config import LOGIN_TEMPLATE, DASHBOARD_TEMPLATE
from db_utils import init_db

# Setup logging—Will not be used here
# logging.basicConfig(filename='ctf_app.log', level=logging.ERROR)

# Flask app setup
app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')
AUTH_DB = os.getenv('AUTH_DB')
DATA_DB = os.getenv('DATA_DB')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')


# Run DB initialization
init_db()

# Routes
@app.route('/', methods=['GET', 'POST'])
def login():
    """Handle user login with a vulnerable SQL query for CTF purposes."""
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
        except KeyError:
            return render_template(LOGIN_TEMPLATE, error='Missing username or password')
        # Intentionally vulnerable to SQL injection for CTF
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        try:
            with sqlite3.connect(AUTH_DB) as conn:
                c = conn.cursor()
                c.execute(query)
                user = c.fetchone()
                if user:
                    session['logged_in'] = True
                    return redirect(url_for('dashboard'))
                return render_template(LOGIN_TEMPLATE, error='Invalid credentials!')
        except Exception as e:
            logging.error(f"Login error for username {username}: {str(e)}")
            return render_template(LOGIN_TEMPLATE, error=str(e))
    return render_template(LOGIN_TEMPLATE, error=None)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    """Handle dashboard with vulnerable search for CTF flag extraction."""
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    results = ''
    if request.method == 'POST':
        try:
            search_term = request.form['search']
            db_name = request.form['database']
        except KeyError:
            return render_template(DASHBOARD_TEMPLATE, results='Missing search or database parameters')
        # Intentionally vulnerable to SQL injection for CTF
        query = f"SELECT * FROM {db_name} WHERE '{search_term}' LIKE %T%"
        try:
            with sqlite3.connect(DATA_DB) as conn:
                c = conn.cursor()
                c.execute(query)
                rows = c.fetchall()
                results = '<br>'.join([', '.join(str(col) for col in row) for row in rows])
        except Exception as e:
            logging.error(f"Dashboard query error: {str(e)}")
            results = str(e)  # Keep error leak for CTF
    return render_template(DASHBOARD_TEMPLATE, results=results)

# Extra endpoints - They are not related to the solution
@app.route('/logout', methods=['POST'])
def logout():
    """Log out the user and clear the session."""
    session.clear()
    return redirect(url_for('login'))

@app.route('/health', methods=['GET'])
def health():
    """Return health status for monitoring."""
    return jsonify(status='ok')

@app.route('/.git', methods=['GET'])
def git():
    """Return health status for monitoring."""
    return jsonify(status='No no no!')

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
