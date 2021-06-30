from flask_app import app
from flask import request, redirect, render_template, session
from flask_app.models.save import Save
from flask_app.models import user

@app.route('/choose_save')
def choose_save():
    if session['logged_in']:
        username = user.User.get_username({'id': session['user_id']})
        saves = Save.get_saves({'user_id': session['user_id']})
    else:
        return redirect('/')
    return render_template("show_saves.html", saves = saves, username = username['username'])