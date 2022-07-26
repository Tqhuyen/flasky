from crypt import methods
from flask_market import app, db
from flask import render_template, url_for,flash, redirect
from flask import request, redirect
from flask_market.model import Item, User
from flask_market.form import RegisterForm

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

@app.route('/register_page', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        email_address=form.email_address.data,
                        password=form.password1.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for errors_msg in form.errors.values():
            flash(errors_msg[0], category='danger')
    return render_template('register.html', form=form)