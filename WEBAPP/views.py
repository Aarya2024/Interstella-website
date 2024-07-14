from flask import Blueprint ,render_template, request , flash,redirect,url_for,send_file
from  wtforms import FileField
from flask_wtf import FlaskForm
import os, shutil
views = Blueprint('views',__name__)
@views.route('/', methods=['POST','GET'])
def home():
    return render_template("index.html")
