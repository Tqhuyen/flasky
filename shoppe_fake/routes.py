from shoppe_fake import app_shoppe
from flask import render_template

#---------------------------------------------Shoppe Fake-----------------------------------------
@app_shoppe.route('/shoppe')
def shoppe_index():
    return render_template('index_shoppe.html')