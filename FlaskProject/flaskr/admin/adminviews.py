from . import admins


@admins.route("/")
def admin():
    return "admin"

