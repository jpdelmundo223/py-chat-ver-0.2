from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(message="Username cannot be empty")])
    password = PasswordField(label="Password", validators=[DataRequired(message="Password cannot be empty")])
    remember_me = BooleanField(label="Remember Me")
    submit = SubmitField(label="Log In")

class RegisterForm(FlaskForm):
    first_name = StringField(label="First Name", validators=[DataRequired(message="First Name cannot be empty")])
    last_name = StringField(label="Last Name", validators=[DataRequired(message="Last Name cannot be empty")])
    username = StringField(label="Username", validators=[DataRequired(message="Username cannot be empty")])
    email = StringField(label="Email", validators=[DataRequired(message="Email cannot be empty"), Email(message="Please provide a valid email address")])
    password = PasswordField(label="Password", validators=[DataRequired(message="Password cannot be empty"), Length(min=8, max=25)])
    confirm_password = PasswordField(label="Password", validators=[DataRequired(message="You must confirm your password"), EqualTo(fieldname="password", message="Password and Confirm Password doesn't match"), Length(min=8, max=25)])
    submit = SubmitField(label="Register")