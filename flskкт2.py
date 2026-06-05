from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user
)
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config["SECRET_KEY"] = "my-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# пользователь
class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# главная
@app.route("/")
def home():
    return redirect(url_for("login"))


# регистрация
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        hashed_password = generate_password_hash(password)

        user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash("Аккаунт создан")

        return redirect(url_for("login"))

    return render_template("register.html")


# вход
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):

            login_user(user)

            return redirect(url_for("profile"))

        flash("Неверный логин или пароль")

    return render_template("login.html")


# профиль
@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")


# выход
@app.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(url_for("login"))


# редактирование профиля
@app.route("/edit-profile", methods=["GET", "POST"])
@login_required
def edit_profile():

    if request.method == "POST":

        current_user.username = request.form.get("username")
        current_user.email = request.form.get("email")

        db.session.commit()

        flash("Данные обновлены")

        return redirect(url_for("profile"))

    return render_template("edit_profile.html")


# смена пароля
@app.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():

    if request.method == "POST":

        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")

        if check_password_hash(current_user.password, old_password):

            current_user.password = generate_password_hash(new_password)

            db.session.commit()

            flash("Пароль успешно изменен")

            return redirect(url_for("profile"))

        flash("Старый пароль введен неправильно")

    return render_template("change_password.html")


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)
