from flask import Flask , render_template,Blueprint ,render_template, request , flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from os import path
db=SQLAlchemy()
DB_NAME="register.db"
def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config['SECRET_KEY'] = 'secret_keyisthekey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from .views import views
    from .auth import auth
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    from .models import User
    create_Database(app)
    return app
def create_Database(app):
    if not path.exists("WEBAPP/instance"+DB_NAME):
        with app.app_context():
            db.create_all()
            print("Created Database")