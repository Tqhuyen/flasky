from flask_market import app
from flask import render_template
from flask import request
from flask_market.model import Item

# ------------------------------------------------Market App--------------------------------------------

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', item_name=items)
@app.route('/login_page')
def login():
    return

@app.route('/register_page')
def register():
    return