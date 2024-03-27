from app.router.views import views
from flask import Flask

app = Flask(__name__)

app.config.from_pyfile("config.py")

app.register_blueprint(views)