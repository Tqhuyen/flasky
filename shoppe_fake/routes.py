from flask_market.routes import login
from shoppe_fake import app_shoppe
from flask import render_template

#---------------------------------------------Shoppe Fake-----------------------------------------
@app_shoppe.route('/shoppe')
def shoppe_index():
    return render_template('index_shoppe.html')
@app_shoppe.route('/shoppe/login')
def shoppe_login():
    return render_template('login.html')