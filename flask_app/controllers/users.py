from flask_app import app
from flask import request, redirect, render_template, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User

bcrypt  = Bcrypt(app)

@app.route('/')
def index():
    if 'user_id' in session:
        session.pop('user_id')
    session['logged_in'] = False
    return render_template("index.html")

@app.route('/register', methods=["POST"])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    user_id = User.create(data)
    session['user_id'] = user_id
    session['logged_in'] = True
    return redirect("/save")

@app.route('/login', methods=["POST"])
def login():
    data = { "email": request.form["email"]}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", "login")
        return redirect('/')
    session['user_id'] = user_in_db.id
    session['logged_in'] = True
    return redirect("/save")