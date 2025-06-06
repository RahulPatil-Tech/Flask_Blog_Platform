# app/__init__.py

from flask import Flask
from dotenv import load_dotenv
import os
from datetime import datetime

from app.extensions import db, migrate, jwt, login_manager
from flask_login import current_user
from flask_cors import CORS
from app.models.user import User

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login' # type: ignore
    CORS(app)

    # User loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Inject current_user into all templates
    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)
    
    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow}

    # Register Blueprints
    from app.routes.auth import auth_bp
    from app.routes.posts import post_bp
    from app.routes.admin import admin_bp
    from app.routes.comment import comment_bp
    from app.routes.main import main_bp
    from app.routes.profile import profile_bp
    
    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(post_bp, url_prefix='/posts')
    app.register_blueprint(comment_bp, url_prefix='/comment')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(profile_bp, url_prefix='/profile')

    return app
