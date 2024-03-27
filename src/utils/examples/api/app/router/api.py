from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix="/api/")

@api.route("/")
def index():
    return jsonify("Hello, World!"), 200