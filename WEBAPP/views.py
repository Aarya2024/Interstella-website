from flask import Blueprint,jsonify, render_template,request,flash
from  wtforms import FileField
from .models import User
from . import db
# from flask_wtf import FlaskForm
import os, shutil
views = Blueprint('views',__name__)
@views.route('/', methods=['POST','GET'])
def home():
    return render_template("index.html")
@views.route('/quiz', methods=['POST','GET'])
def quiz():
    if request.method == 'POST':
        #fetching
        studentName=request.form.get('fullName')
        schoolName=request.form.get('school')
        studentAge=request.form.get('age')
        studentContactNumber=request.form.get('contact')
        emailAddress=request.form.get('email')
        studentSelectedLocation=request.form.get('location')
        
        new_student=User(studentName=studentName,schoolName=schoolName,studentAge=studentAge,studentContactNumber=studentContactNumber,emailAddress=emailAddress,studentSelectedLocation=studentSelectedLocation)
        db.session.add(new_student)
        db.session.commit()
        return render_template("index.html")



        

    return render_template("quiz.html") 