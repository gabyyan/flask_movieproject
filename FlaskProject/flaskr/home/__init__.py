from flask import Blueprint
homes = Blueprint("home", __name__, template_folder="templates", static_folder="static")


from . import views, model








