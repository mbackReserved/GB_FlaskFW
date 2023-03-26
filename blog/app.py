import os

from flask import Flask, render_template
from flask_migrate import Migrate

from .configs import DevConfig
from .models.database import db
from .security import flask_bcrypt
from .views.articles import articles_app
from .views.authors import authors_app
from .views.auth import login_manager, auth_app
from .views.users import users_app
from .admin import admin

app = Flask(__name__)

app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(authors_app, url_prefix="/authors")

app.config.from_object(DevConfig)

file_path = os.path.abspath(os.getcwd()) + "\database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


app.config["SECRET_KEY"] = "abcdefg123456"
app.register_blueprint(auth_app, url_prefix="/auth")
login_manager.init_app(app)

flask_bcrypt.init_app(app)

migrate = Migrate(app, db, compare_type=True)

admin.init_app(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.cli.command("create-admin")
def create_admin():
    from blog.models.user import User
    admin = User(username='admin', is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or "adminpass"

    db.session.add(admin)
    db.session.commit()
   
    print("created admin:", admin)


@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from .models.tag import Tag
    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("created tags")
