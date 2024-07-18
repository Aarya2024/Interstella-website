from flask import Blueprint,jsonify, render_template,request,flash
from  wtforms import FileField
from .models import User,NSAMUN
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
        if len(studentContactNumber)!=10 :
            flash('Invalid Contact Number',category='error')
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
@views.route('/nsamun', methods=['POST','GET'])
def nsamun():
        if request.method == 'POST':
            
            #if N_studentSelectedLocation == 'nagpur':
                N_studentName=request.form.get('name')
                N_studentAge=request.form.get('age')
                N_studentContactNumber=request.form.get('phone')
                N_emailAddress=request.form.get('email')
                N_collegeName=request.form.get('college')
                N_committee=request.form.get('committee')
                #N_studentSelectedLocation=request.form.get('location')
                N_place=request.form.get('Location')
              
                new_N_student=NSAMUN(
                                     N_studentName=N_studentName,
                                     N_studentAge=N_studentAge,
                                     N_studentContactNumber=N_studentContactNumber,
                                     N_emailAddress=N_emailAddress,
                                     #N_studentSelectedLocation=N_studentSelectedLocation,
                                     N_studentcollage=N_collegeName,
                                     N_studentcommittee = N_committee,
                                     N_studentplace = N_place )               
                db.session.add(new_N_student)
                try :
                    db.session.commit()
                except Exception as e:
                    print(e)
                    flash("Email is already registered")
                    return render_template("nsamun.html")
                flash("User Successfully Registered!.")
                # Add Payment Here

                """if N_studentSelectedLocation == 'pimpri':
                 N_studentName=request.form.get('name')
                 N_schoolName=request.form.get('school')
                 N_studentAge=request.form.get('age')
                 N_studentContactNumber=request.form.get('phone')
                 N_emailAddress=request.form.get('email')
                 N_collegeName=request.form.get('college')
                 N_committee=request.form.get('committee')
                 N_place=request.form.get('place')
                 if len(N_studentContactNumber)!=10 :
                     flash('Invalid Contact Number',category='error')
                 else:
                     new_N_student=NSAMUN(studentName=            N_studentName,
                                          schoolName=             N_schoolName,
                                          studentAge=             N_studentAge,
                                          studentContactNumber=   N_studentContactNumber,
                                          emailAddress=           N_emailAddress,
                                          studentSelectedLocation=N_studentSelectedLocation,
                                          studentcollage =        N_collegeName,
                                          studentcommittee =      N_committee,
                                          studentplace =          N_place )
                     db.session.add(new_N_student)
                     try :
                         db.session.commit()
                     except Exception as e:
                         print(e)
                         flash("Email is already registered")
                         return render_template("nsamun.html")
                     flash("User Successfully Registered!.")
                     # Add Payment Here

            return render_template("nsamun.html")"""
        return render_template("nsamun.html")       