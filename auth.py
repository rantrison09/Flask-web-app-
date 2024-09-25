from flask import Blueprint, render_template, request, flash, redirect, url_for
from icecream import ic
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, logout_user, login_required, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login',methods= ["GET","POST"])
def login():
    if request.method == "POST":
        email =request.form.get("email")
        password= request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('login sucessful', category="success")
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password,try again', category="error")
        else:
            flash('Email does not exsist', category="error")
    return render_template('login.html',user= current_user)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods= ["GET","POST"])
def sign_up():
    if request.method =="POST":
        email =request.form.get("email")
        first_name =request.form.get("first_name")
        password1 =request.form.get("password1")
        password2 =request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists.", category="error")
        elif not email:
            flash("Email must be greater than 3 characters.", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif len( first_name) <2:
            flash("First Name must be greater than 1 character.", category="error")
        elif password1 != password2:
            flash("Passwords dont match.", category="error") 
        elif len(password1) <3:
            flash("Password must be at least 6 characters long .", category="error")
        else:
            
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='scrypt'))
            
            db.session.add(new_user)
            db.session.commit()
            
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template('signup.html')

           
           
           
            

    
