from flask import Blueprint
admins = Blueprint("admin", __name__, template_folder="templates", static_folder="static")

from . import adminviews
# from flaskr import model


