from flask import Flask
from app.rest_api.routes import rest_api
from app.template_app.routes import template_page

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(template_page, url_prefix="/")
app.register_blueprint(rest_api, url_prefix="/api")
