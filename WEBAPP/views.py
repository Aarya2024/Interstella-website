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
        if len(studentContactNumber)>10 and len(studentContactNumber)<0:
            flash("Invalid Contact Number",category='error')
        else:
            new_student=User(studentName=studentName,schoolName=schoolName,studentAge=studentAge,studentContactNumber=studentContactNumber,emailAddress=emailAddress,studentSelectedLocation=studentSelectedLocation)
            db.session.add(new_student)
            try:
                db.session.commit()
            except Exception as e:
                print(e)
                flash("Email is already registered")
                return render_template("quiz.html")

            flash("User Successfully Registered!.")
            # Add Payment Here
    return render_template("quiz.html") 