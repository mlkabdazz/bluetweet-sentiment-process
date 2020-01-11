from flask import Blueprint

home_blueprint = Blueprint("/", __name__)


@home_blueprint.route("/")
def home():
    return "hello malik"
