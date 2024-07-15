from flask import Blueprint ,render_template, request , flash,redirect,url_for
auth = Blueprint('auth',__name__)
@auth.route('/quiz',methods =['POST','GET'])
def quiz():
      
    return render_template("quiz.html") 