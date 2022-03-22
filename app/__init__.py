from flask import Flask, render_template
from .extensions import db, login_manager, migrate
from .socket import socketio
from .models import User
from flask_socketio import send, join_room, leave_room
from flask_login import current_user

def create_app():
    app = Flask(__name__)
    # Use the ff. command to quickly generate a value for Flask.secret_key (or SECRET_KEY).
    app.config.from_object("config")
    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"

    from .models import User
    db.create_all(app=app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp)
    
    from .main import main as main_bp
    app.register_blueprint(main_bp)

    return app