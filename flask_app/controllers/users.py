from flask_app import app
from flask import request, redirect, render_template, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User

bcrypt  = Bcrypt(app)