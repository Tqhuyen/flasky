from flask_market import app 
from shoppe_fake import app_shoppe

if __name__ == '__main__':
    app_shoppe.run(host='0.0.0.0',port=80,debug=True)