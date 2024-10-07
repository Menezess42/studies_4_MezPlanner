# Blueprint is a way of using flask in a more porfessional way.
# It modularize the code, making more powerfull and allowing
# devs to work in different modules without get int he way of
# one another
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    # each blueprint has his template folder
    app = Flask(__name__, template_folder="templates")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./blueprints.db"

    db.init_app(app)

    # import and register all blueprints(merge everthing together)
    from blueprintapp.core.routes import core
    from blueprintapp.todos.routes import todos
    from blueprintapp.people.routes import people

    app.register_blueprint(core, url_prefix="/")
    app.register_blueprint(todos, url_prefix="/todos")
    app.register_blueprint(people, url_prefix="/people")

    migrate = Migrate(app, db)
    return app
