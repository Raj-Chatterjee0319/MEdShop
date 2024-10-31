from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from . import db
from flask_login import login_user,login_required,logout_user,current_user
from werkzeug.security import generate_password_hash,check_password_hash


auth=Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        email=request.form.get('email')
        password=request.form.get('password')
        
        if not email or not password:
            flash("Please provide both email and password", category='error')
            return render_template('login.html')
        
        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash("logged in successfully",category='Success')
                login_user(user,remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect Password,Try Again!!",category='error')
        else:
            flash("Email Does not exist",category='error')
        
    return render_template('login.html')

@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=="POST":
        email=request.form.get("email")
        username=request.form.get("username")
        password=request.form.get("password")
        password2=request.form.get("password2")
        
        user=User.query.filter_by(email=email).first()
        if user:
            flash("Email already exist",category='error')
        if len(email)<4:
            flash('Email must be greater than 4 character',category='error')
        elif len(username)<2:
            flash('Username must be greater than 2 character',category='error')
        elif password!=password2:
            flash('password don\'t match',category='error')
        elif len(password)<4:
            flash('password must be greater than 4 character',category='error')
        else:
            new_user=User(email=email,username=username,password=generate_password_hash(password,method='pbkdf2:sha256'))
            print("ttaa",new_user.username)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user,remember=True)
            flash("Account Created!!",category='success')
            return redirect(url_for("views.home"))
    return render_template('signup.html',new_user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.firstpage'))