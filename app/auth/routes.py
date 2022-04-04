from flask import redirect, render_template, request, jsonify, current_app, url_for
from flask_login import login_required, login_user, logout_user, current_user
from app.auth import auth
from app.auth.forms import LoginForm, RegisterForm
from app.models import User
from app.extensions import db
from sqlalchemy import or_

# Render login page
@auth.route("/login")
def login():
    form = LoginForm()
    title = "Login"
    return render_template("auth/login.html", form=form, title=title)

# Login user
@auth.route("/login-user", methods=["GET", "POST"])
def _login_user():
    form = LoginForm()
    username = form.username.data
    password = form.password.data
    remember_me = form.remember_me.data
    user = User.query.filter_by(username=username).first()
    form_errors = []
    if request.method == "POST":
        if form.validate_on_submit():
            if user and User.verify_password_hash(user.password_hash, password):
                data = dict(message="Login successful!", status="success")
                login_user(user, remember=remember_me)
                return jsonify(data=data)
            else:
                data = dict(message="Incorrect username or password!", status="error")
                for key, val in form.errors.items():
                    form_errors.append(val)
                return jsonify(data=data)
        else:
            for key, val in form.errors.items():
                form_errors.append({key: val})
            return jsonify(data=form_errors)

# Render register page
@auth.route("/register")
def register():
    form = RegisterForm()
    title = "Register"
    return render_template("auth/register.html", form=form, title=title)

@auth.route("/register-user", methods=["GET", "POST"])
def _register_user():
    form = RegisterForm()
    first_name = form.first_name.data
    last_name = form.last_name.data
    username = form.username.data
    email = form.email.data
    password = form.password.data
    user = User.query.filter(or_(User.username==username, User.email==email)).first()
    if request.method == "POST":
        if form.validate_on_submit():
            if user is None:
                new_user = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                db.session.add(new_user)
                db.session.commit()
                data = dict(message="User successfully registered!", status="success")
                return jsonify(data=data)
            else:
                data = dict(message="There is something wrong with your registration.", status="error")
                return jsonify(data=data)
        else:
            form_errors = []
            for key, value in form.errors.items():
                form_errors.append(value)
            return jsonify(data=form_errors)

@auth.route("/get_room", methods=["GET"])
def _get_room():
    room = "From query"
    if request.method == "GET":
        return jsonify(room=room)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))