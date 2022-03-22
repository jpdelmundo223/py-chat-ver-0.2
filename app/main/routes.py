from flask import render_template
from app.main import main
from app.main.forms import MessageForm
from app.models import User
from flask_login import login_required

@main.route('/messages')
@login_required
def get_messages():
    form = MessageForm()
    users = User.query.all()
    return render_template("main/messages.html", form=form, users=users)