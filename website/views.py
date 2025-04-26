from flask import Blueprint, render_template
from flask_login import  login_required,  current_user

views = Blueprint('views', __name__)



@views.route('/')
def home():
    return render_template("home.html")


@views.route('/add')
@login_required
def add_pet():
    return render_template("add_pet.html")






