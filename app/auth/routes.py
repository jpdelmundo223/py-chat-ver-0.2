from flask import redirect, render_template, request, jsonify, current_app, url_for
from flask_login import login_required, login_user, logout_user, current_user
from app.auth import auth
from app.auth.forms import LoginForm, RegisterForm
from app.models import User

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
                login_user(user, remember=False)
                return jsonify(data=data)
            else:
                data = dict(message="Invalid login!", status="error")
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
    pass

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))