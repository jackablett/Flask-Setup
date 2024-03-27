from app.router.api import api
from flask import Flask

app = Flask(__name__)

app.config.from_pyfile("config.py")

app.register_blueprint(api)