from flask import Flask, Blueprint

blueprint = Blueprint("my_blueprint", __name__)


@blueprint.route("/show/<string:name>/<string:surname>")
def shows(name, surname):
    return f"Hello {name, surname}"
