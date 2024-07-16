from flask import Blueprint ,render_template
from  wtforms import FileField
# from flask_wtf import FlaskForm
import os, shutil
views = Blueprint('views',__name__)
@views.route('/', methods=['POST','GET'])
def home():
    return render_template("index.html")
@views.route('/quiz', methods=['POST','GET'])
def quiz():    
    return render_template("quiz.html") 