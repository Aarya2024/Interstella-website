# from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint ,render_template, request , flash,redirect,url_for
auth = Blueprint('auth',__name__)
@auth.route('/login',methods =['POST','GET'])
def login():
        
    return render_template("index.html") 