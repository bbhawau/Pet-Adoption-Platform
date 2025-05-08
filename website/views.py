from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required,  current_user
from .models import Animal, AnimalGroup


views = Blueprint('views', __name__)


@views.route('/')
@views.route('/home')
def home():
    return render_template("home.html")


@views.route('/browse')
@login_required
def browse_pets():
    animal_groups = AnimalGroup.query.all()
    grouped_animals = {group.name: group.animals for group in animal_groups}
    return render_template("browse_pets.html", animal_groups=grouped_animals)

@views.route('/adopt/<int:animal_id>')
@login_required
def adopt(animal_id):
    animal = Animal.query.get_or_404(animal_id)
    return render_template("adopt.html", animal=animal)

@views.route('/how')
@login_required
def how_it_works():
    return render_template("how_it_works.html")

