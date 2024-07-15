<<<<<<< HEAD
# from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
=======
>>>>>>> 7c46b2ed46ea7574958d417552df87533ec062a1
from flask import Blueprint ,render_template, request , flash,redirect,url_for
auth = Blueprint('auth',__name__)
@auth.route('/quiz',methods =['POST','GET'])
def quiz():
      
    return render_template("quiz.html") 