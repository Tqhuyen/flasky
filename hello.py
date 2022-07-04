from flask import Flask, render_template
from flask import request
from flask import current_app
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Thís is index page</h1>"

@app.route('/client_in4')
def client():
    user_agent = request.headers.get('User-Agent')
    return f"<h1>Your browser agent is {user_agent}</h1>"
@app.route('/facebook')
def facebook():
    return render_template('index.html')
@app.route('/<user>')
def user(user):
    return render_template('user.html', user=user)
# @app.route('/current app')
# def current_app():
#     # current_app_name = current_app.__name()
#     return f"<p>{current_app.__name__()}</p>"
