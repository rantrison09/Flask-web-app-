from flask import Blueprint, render_template,request, flash
from icecream import ic


auth = Blueprint('auth', __name__)


@auth.route('/login',methods= ["GET","POST"])
def login():
    ic(request.form)
    data = request.form
    print (data)
    return render_template('login.html',boolean= True)



@auth.route('/logout')
def logout():
    return "<p> logout </p> "

@auth.route('/sign-up',methods= ["GET","POST"])
def sign_up():
    if request.method =="POST":
        email =request.form.get("email")
        first_name =request.form.get("first_name")
        password1 =request.form.get("password1")
        password2 =request.form.get("password2")
        if len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif len( first_name) <2:
            flash("First Name must be greater than 1 character.", category="error")
        elif password1 != password2:
            flash("Passwords dont match.", category="error") 
        elif len(password1) <3:
            flash("Password must be at least 6 characters long .", category="error")
        else:
            flash("Account created.", category="sucess")


    return render_template('signup.html')
