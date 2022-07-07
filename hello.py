from flask import Flask, render_template
from flask import request
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

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
# ------------------------------------------------Market App--------------------------------------------

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', item_name=items)
@app.route('/login_page')
def login():
    return

@app.route('/register_page')
def register():
    return

# @app.route('/current app')
# def current_app():
#     # current_app_name = current_app.__name()
#     return f"<p>{current_app.__name__()}</p>"
#---------------------------------------------Shoppe Fake-----------------------------------------
@app.route('/shoppe')
def shoppe_index():
    return render_template('index_shoppe.html')