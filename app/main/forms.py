from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class MessageForm(FlaskForm):
    message = TextAreaField(validators=[DataRequired(), Length(max=255)])
    send = SubmitField(label="Send")