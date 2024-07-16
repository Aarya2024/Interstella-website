
from flask import Blueprint ,render_template, request , flash,redirect,url_for
auth = Blueprint('auth',__name__)
from . import db
from .models import User
@auth.route("/admin")
def admin():
    data=db.session.scalars(db.select(User)).all()
    print(data)
    return render_template('admin.html',users=data)