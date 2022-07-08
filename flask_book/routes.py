from flask_market import app
from flask import render_template
from flask import request
from flask_market.model import Item

@app.route('/')
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
