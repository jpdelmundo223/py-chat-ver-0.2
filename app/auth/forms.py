from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(message="Username cannot be empty")])
    password = PasswordField(label="Password", validators=[DataRequired(message="Password cannot be empty")])
    remember_me = BooleanField(label="Remember Me")
    submit = SubmitField(label="Log In")

class RegisterForm(FlaskForm):
    first_name = StringField(label="First Name", validators=[DataRequired()])
    last_name = StringField(label="Last Name", validators=[DataRequired()])
    username = StringField(label="Username", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8, max=25)])
    confirm_password = PasswordField(label="Password", validators=[DataRequired(), EqualTo(fieldname="password", message="Password and Confirm Password doesn't match")])
    submit = SubmitField(label="Register")