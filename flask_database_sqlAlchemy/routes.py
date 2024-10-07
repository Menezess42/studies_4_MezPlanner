# File where we define the routes, redirect
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from models import User


def register_routes(app, db, bcrypt):

    @app.route("/", methods=["GET", "POST"])
    def index():
        return render_template("index.html")

    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        if request.method == "GET":
            return render_template("signup.html")
        elif request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")

            hashed_password = bcrypt.generate_password_hash(password)
            user = User(username=username, password=hashed_password)

            db.session.add(user)
            db.session.commit()
            return redirect(url_for("index"))

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "GET":
            return render_template("login.html")
        elif request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")

            user = User.query.filter(User.username == username).first()

            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return render_template('index.html')
            else:
                return 'Failed'
                

    @app.route("/logout", methods=["GET", "POST"])
    def logout():
        logout_user()
        return render_template('index.html')

    @app.route('/secret')
    @login_required
    def secret():
        return "Secret section!!!"


# def register_routes(app, db):
#     @app.route("/", methods=["GET", "POST"])
#     def index():
#         if request.method == "GET":
#             people = Person.query.all()
#             return render_template("index.html", people=people)
#         elif request.method == "POST":
#             name = request.form.get("name")
#             age = int(request.form.get("age"))
#             job = request.form.get("job")

#             person = Person(name=name, age=age, job=job)
#             db.session.add(person)
#             db.session.commit()

#             people = Person.query.all()
#             return render_template("index.html", people=people)


#     @app.route("/delete/<pid>", methods=["DELETE"])
#     def delete(pid):
#         Person.query.filter(Person.pid == pid).delete()

#         db.session.commit()
#         people = Person.query.all()
#         return render_template('index.html', people=people)


#     @app.route('/details/<pid>')
#     def details(pid):
#         person = Person.query.filter(Person.pid == pid).first()
#         return render_template('detail.html', person=person)
