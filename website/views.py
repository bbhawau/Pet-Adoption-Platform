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
            {"name": "Rocky", "breed": "Bulldog", "age": 4, "image": "rocky.jpg"},
            {"name": "Milo", "breed": "Beagle", "age": 1, "image": "milo.jpg"},
            {"name": "Daisy", "breed": "Golden Retriever",
                "age": 2, "image": "daisy.jpg"},
            {"name": "Coco", "breed": "Poodle", "age": 5, "image": "coco.jpg"}
        ],
        "Cats": [
            {"name": "Luna", "breed": "Siamese", "age": 1, "image": "luna.jpg"},
            {"name": "Simba", "breed": "Persian", "age": 4, "image": "simba.jpg"},
            {'name': 'Shadow', 'breed': 'Maine Coon',
                'age': 4, 'image': 'shadow.jpg'},
            {"name": "Whiskers", "breed": "Tabby",
                "age": 3, "image": "whiskers.jpg"},
            {"name": "Nala", "breed": "Bengal", "age": 2, "image": "nala.jpg"},
            {"name": "Oreo", "breed": "British Shorthair",
                "age": 1, "image": "oreo.jpg"}
        ],

        "Reptiles": [
            {"name": "Lizzy", "breed": "Bearded Dragon",
                "age": 1, "image": "lizzy.jpg", },
            {"name": "Sneaky", "breed": "Corn Snake",
                "age": 2, "image": "sneaky.jpg", },
            {"name": "Spike", "breed": "Iguana", "age": 5, "image": "spike.jpg"},
            {"name": "Copper", "breed": "Ball Python",
                "age": 4, "image": "copper.jpg"},
            {"name": "Slinky", "breed": "Gecko", "age": 1, "image": "slinky.jpg"},
            {"name": "Shelly", "breed": "Tortoise",
                "age": 10, "image": "shelly.jpg"},

        ],
        "Birds": [
            {"name": "Charlie", "breed": "Parrot",
                "age": 3, "image": "charlie.jpg"},
            {"name": "Kiwi", "breed": "Macaw", "age": 2, "image": "kiwi.jpg"},
            {"name": "Sunny", "breed": "Canary", "age": 1, "image": "sunny.jpg"},
            {"name": "Sky", "breed": "Budgie", "age": 2, "image": "sky.jpg"},
            {"name": "Echo", "breed": "Cockatiel", "age": 4, "image": "echo.jpg"},
            {"name": "Zazu", "breed": "African Grey", "age": 5, "image": "zazu.jpg"}
        ],
        "Fish": [
            {"name": "Nemo", "breed": "Clownfish", "age": 1, "image": "nemo.jpg"},
            {"name": "Dory", "breed": "Blue Tang", "age": 2, "image": "dory.jpg"},
            {"name": "Bubbles", "breed": "Goldfish",
                "age": 1, "image": "bubbles.jpg"},
            {"name": "Gill", "breed": "Angelfish", "age": 3, "image": "gill.jpg"},
            {"name": "Marlin", "breed": "Betta", "age": 2, "image": "marlin.jpg"},
            {"name": "Finley", "breed": "Guppy", "age": 1, "image": "finley.jpg"}
        ]

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
            {"name": "Max", "breed": "German Shepherd",
                "age": 3, "image": "max.jpg"},
            {"name": "Rocky", "breed": "Bulldog", "age": 4, "image": "rocky.jpg"},
            {"name": "Milo", "breed": "Beagle", "age": 1, "image": "milo.jpg"},
            {"name": "Daisy", "breed": "Golden Retriever",
                "age": 2, "image": "daisy.jpg"},
            {"name": "Coco", "breed": "Poodle", "age": 5, "image": "coco.jpg"}
        ],
        "Cats": [
            {"name": "Luna", "breed": "Siamese", "age": 1, "image": "luna.jpg"},
            {"name": "Simba", "breed": "Persian", "age": 4, "image": "simba.jpg"},
            {'name': 'Shadow', 'breed': 'Maine Coon',
                'age': 4, 'image': 'shadow.jpg'},
            {"name": "Whiskers", "breed": "Tabby",
                "age": 3, "image": "whiskers.jpg"},
            {"name": "Nala", "breed": "Bengal", "age": 2, "image": "nala.jpg"},
            {"name": "Oreo", "breed": "British Shorthair",
                "age": 1, "image": "oreo.jpg"}
        ],

        "Reptiles": [
            {"name": "Lizzy", "breed": "Bearded Dragon",
                "age": 1, "image": "lizzy.jpg", },
            {"name": "Sneaky", "breed": "Corn Snake",
                "age": 2, "image": "sneaky.jpg", },
            {"name": "Spike", "breed": "Iguana", "age": 5, "image": "spike.jpg"},
            {"name": "Copper", "breed": "Ball Python",
                "age": 4, "image": "copper.jpg"},
            {"name": "Slinky", "breed": "Gecko", "age": 1, "image": "slinky.jpg"},
            {"name": "Shelly", "breed": "Tortoise",
                "age": 10, "image": "shelly.jpg"},

        ],
        "Birds": [
            {"name": "Charlie", "breed": "Parrot",
                "age": 3, "image": "charlie.jpg"},
            {"name": "Kiwi", "breed": "Macaw", "age": 2, "image": "kiwi.jpg"},
            {"name": "Sunny", "breed": "Canary", "age": 1, "image": "sunny.jpg"},
            {"name": "Sky", "breed": "Budgie", "age": 2, "image": "sky.jpg"},
            {"name": "Echo", "breed": "Cockatiel", "age": 4, "image": "echo.jpg"},
            {"name": "Zazu", "breed": "African Grey", "age": 5, "image": "zazu.jpg"}
        ],
        "Fish": [
            {"name": "Nemo", "breed": "Clownfish", "age": 1, "image": "nemo.jpg"},
            {"name": "Dory", "breed": "Blue Tang", "age": 2, "image": "dory.jpg"},
            {"name": "Bubbles", "breed": "Goldfish",
                "age": 1, "image": "bubbles.jpg"},
            {"name": "Gill", "breed": "Angelfish", "age": 3, "image": "gill.jpg"},
            {"name": "Marlin", "breed": "Betta", "age": 2, "image": "marlin.jpg"},
            {"name": "Finley", "breed": "Guppy", "age": 1, "image": "finley.jpg"}
        ]
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
