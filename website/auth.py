from . import db
from .modles import User, Note
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required


auth= Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email=request.form.get("email")
    password=request.form.get("password")
    
    user=User.query.filter_by(email=email).first()
    if user:
      if check_password_hash(user.password, password=password):
        flash("Login successfully", category="success")
        login_user(user, remember=True)
        return redirect(url_for("views.home"))
      else:
        flash("Password incorrect!, try again.", category='error') 
    else:
      flash("Email does not exist!", category='error') 
  return render_template("login.html", title='Log In',user=current_user)

@auth.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
  logout_user()
  return redirect(url_for('auth.login'))


@auth.route("/signup", methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    email= request.form.get("email")
    fname=request.form.get("FirstName")
    password1= request.form.get("password1")
    password2=request.form.get("password2")
    
    user = User.query.filter_by(email=email).first()
    if user:
      flash("That user is already exists!.", category='error')
    elif len(fname) < 2:
      flash("Your first name must be greater then 1 character.", category="error")
    elif len(email) < 4:
      flash("Your email must be greater then 3 character.", category="error")
    elif len(password1) < 7:  
      flash("Password must be at least 7 character.", category="error")
    elif password1 != password2:
      flash("Passwords don't matches.", category="error")
    else:
      new_user=User(email=email, FirstName=fname, password=generate_password_hash(password2, method='pbkdf2:sha256'))
      db.session.add(new_user)
      db.session.commit()
      flash("Account created", category='success')
      login_user(user, remember=True)
      return redirect(url_for('views.home'))
    
  return render_template('sign_up.html', title='Sign Up', methods=['GET', 'POST'], user=current_user)