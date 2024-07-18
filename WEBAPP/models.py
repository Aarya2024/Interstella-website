from . import db
# for quiz form
class User(db.Model):
    
    id=db.Column(db.Integer,primary_key=True)
    studentName=db.Column(db.String(50),nullable=False)
    schoolName=db.Column(db.String(100),nullable=False)
    studentAge=db.Column(db.Integer,nullable=False)
    studentContactNumber=db.Column(db.Integer,nullable=False,unique=True)
    emailAddress=db.Column(db.String(150),nullable=False,unique=True)
    studentSelectedLocation=db.Column(db.String(10))
    paymentStatus=db.Column(db.Boolean,default=False)
#for nsamun form
class NSAMUN(db.Model):
    
    N_id=db.Column(db.Integer,primary_key=True)
    N_studentName=db.Column(db.String(50),nullable=False)
    N_studentAge=db.Column(db.Integer,nullable=False)
    N_studentContactNumber=db.Column(db.Integer,nullable=False,unique=True)
    N_emailAddress=db.Column(db.String(150),nullable=False,unique=True)
    #N_studentSelectedLocation=db.Column(db.String(10))
    N_studentcollage=db.Column(db.String(100),nullable=False)
    N_studentcommittee = db.Column(db.String(50),nullable=False)
    N_studentplace = db.Column(db.String(50),nullable=True)
    N_paymentStatus=db.Column(db.Boolean,default=False)

    
