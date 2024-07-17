
from flask import Blueprint ,render_template, request , flash,redirect,url_for
auth = Blueprint('auth',__name__)
from . import db
from .models import User,NSAMUN
@auth.route("/admin")
def admin():
    data=User.query.all()
    print(data)
    return render_template('admin.html',users=data)
@auth.route("/admin2")
def admin2():
    data=NSAMUN.query.all()
    print(data)
    return render_template('admin.html',users=data)