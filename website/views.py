from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required,  current_user

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/browse')
@login_required
def browse_pets():
    animal_groups = {
        "Dogs": [
            {"name": "Bella", "breed": "Labrador", "age": 2, "image": "bella.jpg"},
            {"name": "Max", "breed": "German Shepherd",
                "age": 3, "image": "max.jpg"},
        ],
        "Cats": [
            {"name": "Luna", "breed": "Siamese", "age": 1, "image": "luna.jpg"},
            {"name": "Simba", "breed": "Persian", "age": 4, "image": "simba.jpg"},
            {'name': 'Shadow','breed': 'Maine Coon','age': 4,'image': 'shadow.jpg'},
        ],

        "Reptiles": [
            {"name": "Lizzy", "breed": "Bearded Dragon",
                "age": 1, "image": "lizzy.jpg", },
            {"name": "Sneaky", "breed": "Corn Snake",
                "age": 2, "image": "sneaky.jpg", },
        ],

    }
     # Add a unique ID to each animal
    animal_id = 1
    for group in animal_groups.values():
        for animal in group:
            animal['id'] = animal_id
            animal_id += 1
            
    return render_template("browse_pets.html", animal_groups=animal_groups)


@views.route('/adopt/<int:animal_id>')
@login_required
def adopt(animal_id):
    # Static animal data
    animal_groups = {
        "Dogs": [
            {"name": "Bella", "breed": "Labrador", "age": 2, "image": "bella.jpg"},
            {"name": "Max", "breed": "German Shepherd", "age": 3, "image": "max.jpg"},
        ],
        "Cats": [
            {"name": "Luna", "breed": "Siamese", "age": 1, "image": "luna.jpg"},
            {"name": "Simba", "breed": "Persian", "age": 4, "image": "simba.jpg"},
            {"name": "Shadow", "breed": "Maine Coon", "age": 4, "image": "shadow.jpg"},
        ],
        "Reptiles": [
            {"name": "Lizzy", "breed": "Bearded Dragon", "age": 1, "image": "lizzy.jpg"},
            {"name": "Sneaky", "breed": "Corn Snake", "age": 2, "image": "sneaky.jpg"},
        ],
    }

    # Assign IDs and find matching animal
    animal_id_counter = 1
    selected_animal = None
    for group in animal_groups.values():
        for animal in group:
            if animal_id_counter == animal_id:
                animal['id'] = animal_id_counter
                selected_animal = animal
                break
            animal_id_counter += 1
        if selected_animal:
            break

    if not selected_animal:
        flash("Animal not found", category="error")
        return redirect(url_for("views.browse_pets"))

    return render_template("adopt.html", animal=selected_animal)



@views.route('/how')
@login_required
def how_it_works():
    return render_template("how_it_works.html")

