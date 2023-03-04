from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

users_app = Blueprint("users_app", __name__)
USERS = {
    1: "Vadim",
    2: "Alex",
    3: "Andrew",
}

@users_app.route("/")
def users_list():
    return render_template("users/list.html", users=USERS)


@users_app.route("/<int:user_id>/")
def user_details(user_id: int):
    try:
        user_name = USERS[user_id]
    except KeyError:
        raise NotFound(f"User {user_id} doesn't exist!")
    return render_template('users/details.html', user_id=user_id, user_name = user_name)