from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# we gona have a db object that is gonna be needed in the models.py file
db = SQLAlchemy()


# Creates the app and return as an object
def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./testdb.db"
    app.secret_key='SOME KEY'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    from models import User

    # defining for the LoginManager what is a Logad user
    @login_manager.user_loader
    def logad_user(uid):
        return User.query.get(uid)

    # imports later on
    # Avoiding circular imports(infinite recursive)
    from routes import register_routes

    bcrypt = Bcrypt(app)

    register_routes(app, db, bcrypt)

    migrate = Migrate(app, db)
    return app
