from flask import Flask, render_template

app_shoppe = Flask(__name__)

from shoppe_fake import routes