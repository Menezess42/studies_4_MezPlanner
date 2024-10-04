from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# we gona have a db object that is gonna be needed in the models.py file
db = SQLAlchemy()


# Creates the app and return as an object
def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./testdb.db"

    db.init_app(app)

    # imports later on
    ## Avoiding circular imports(infinite recursive)
    from routes import register_routes

    register_routes(app, db)
    ##
    migrate = Migrate(app, db)
    return app
