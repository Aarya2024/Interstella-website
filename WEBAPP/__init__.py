from flask import Flask , render_template
from flask import Blueprint ,render_template, request , flash,redirect,url_for
def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config['SECRET_KEY'] = 'secret_keyisthekey'

    from .views import views
    from .auth import auth
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    
    return app
