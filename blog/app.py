from flask import Flask, request, render_template
from blog.views.users import users_app

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

app.register_blueprint(users_app, url_prefix="/users")