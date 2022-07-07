from flask_market import app 
from shoppe_fake import app

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)