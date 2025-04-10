from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# Sample data
pets = [
    {"id": 1, "name": "Buddy", "type": "Dog", "age": 3},
    {"id": 2, "name": "Mittens", "type": "Cat", "age": 2}
]

@views.route('/')
def home():
    return render_template("home.html", pets=pets)

@views.route('/pet/<int:pet_id>')
def pet_detail(pet_id):
    pet = next((p for p in pets if p["id"] == pet_id), None)
    return render_template("pet_detail.html", pet=pet)

@views.route('/add')
def add_pet():
    return render_template("add_pet.html")

@views.route('/login')
def login():
    return render_template("login.html")
