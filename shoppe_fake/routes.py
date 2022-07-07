from shoppe_fake import app
from flask import render_template

#---------------------------------------------Shoppe Fake-----------------------------------------
@app.route('/shoppe')
def shoppe_index():
    return render_template('index_shoppe.html')