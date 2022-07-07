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
@app.route('/client_in4')
def client():
    user_agent = request.headers.get('User-Agent')
    return f"<h1>Your browser agent is {user_agent}</h1>"
@app.route('/facebook')
def facebook():
    return render_template('flask_market/index.html')
@app.route('/<user>')
def user(user):
    return render_template('flask_market/user.html', user=user)

# ------------------------------------------------Market App--------------------------------------------

@app.route('/home')
def home_page():
    return render_template('flask_market/home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('flask_market/market.html', item_name=items)
@app.route('/login_page')
def login():
    return

@app.route('/register_page')
def register():
    return

#---------------------------------------------Shoppe Fake-----------------------------------------
@app.route('/shoppe')
def shoppe_index():
    return render_template('shoppe_fake/index_shoppe.html')

# --------------------------------------------Browser Infomation--------------------------------------