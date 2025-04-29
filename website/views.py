from flask import Blueprint, render_template
from flask_login import  login_required,  current_user

views = Blueprint('views', __name__)



@views.route('/')
def home():
    return render_template("home.html")


@views.route('/browse')
@login_required
def browse_pets():
    return render_template("browse_pets.html")

@views.route('/how')
@login_required
def how_it_works():
    return render_template("how_it_works.html")






