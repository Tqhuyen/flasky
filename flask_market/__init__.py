from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'dcd03ef0eabedb64aa2e3b48'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flask_market import routes
