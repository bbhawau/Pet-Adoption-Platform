from website import create_app, db
from website.models import AnimalGroup, Animal


app = create_app()

animals_data = {
    "Dogs": [
        {"name": "Bella", "breed": "Labrador", "age": 2, "image": "bella.jpg"},
        {"name": "Max", "breed": "German Shepherd", "age": 3, "image": "max.jpg"},
        {"name": "Rocky", "breed": "Bulldog", "age": 4, "image": "rocky.jpg"},
        {"name": "Milo", "breed": "Beagle", "age": 1, "image": "milo.jpg"},
        {"name": "Daisy", "breed": "Golden Retriever", "age": 2, "image": "daisy.jpg"},
        {"name": "Coco", "breed": "Poodle", "age": 5, "image": "coco.jpg"}
    ],
    "Cats": [
        {"name": "Luna", "breed": "Siamese", "age": 1, "image": "luna.jpg"},
        {"name": "Simba", "breed": "Persian", "age": 4, "image": "simba.jpg"},
        {"name": "Shadow", "breed": "Maine Coon", "age": 4, "image": "shadow.jpg"},
        {"name": "Whiskers", "breed": "Tabby", "age": 3, "image": "whiskers.jpg"},
        {"name": "Nala", "breed": "Bengal", "age": 2, "image": "nala.jpg"},
        {"name": "Oreo", "breed": "British Shorthair", "age": 1, "image": "oreo.jpg"}
    ],
    "Reptiles": [
        {"name": "Lizzy", "breed": "Bearded Dragon", "age": 1, "image": "lizzy.jpg"},
        {"name": "Sneaky", "breed": "Corn Snake", "age": 2, "image": "sneaky.jpg"},
        {"name": "Spike", "breed": "Iguana", "age": 5, "image": "spike.jpg"},
        {"name": "Copper", "breed": "Ball Python", "age": 4, "image": "copper.jpg"},
        {"name": "Slinky", "breed": "Gecko", "age": 1, "image": "slinky.jpg"},
        {"name": "Shelly", "breed": "Tortoise", "age": 10, "image": "shelly.jpg"}
    ],
    "Birds": [
        {"name": "Charlie", "breed": "Parrot", "age": 3, "image": "charlie.jpg"},
        {"name": "Kiwi", "breed": "Macaw", "age": 2, "image": "kiwi.jpg"},
        {"name": "Sunny", "breed": "Canary", "age": 1, "image": "sunny.jpg"},
        {"name": "Sky", "breed": "Budgie", "age": 2, "image": "sky.jpg"},
        {"name": "Echo", "breed": "Cockatiel", "age": 4, "image": "echo.jpg"},
        {"name": "Zazu", "breed": "African Grey", "age": 5, "image": "zazu.jpg"}
    ],
    "Fish": [
        {"name": "Nemo", "breed": "Clownfish", "age": 1, "image": "nemo.jpg"},
        {"name": "Dory", "breed": "Blue Tang", "age": 2, "image": "dory.jpg"},
        {"name": "Bubbles", "breed": "Goldfish", "age": 1, "image": "bubbles.jpg"},
        {"name": "Gill", "breed": "Angelfish", "age": 3, "image": "gill.jpg"},
        {"name": "Marlin", "breed": "Betta", "age": 2, "image": "marlin.jpg"},
        {"name": "Finley", "breed": "Guppy", "age": 1, "image": "finley.jpg"}
    ]
}

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create the animal groups first
    for group_name in animals_data.keys():
        group = AnimalGroup(name=group_name)
        db.session.add(group)
    
    db.session.commit()

    # Create animals for each group
    for group_name, animals in animals_data.items():
        group = AnimalGroup.query.filter_by(name=group_name).first()
        if not group:
            print(f"Group not found for {group_name}")
            continue  # skip this group if it doesn't exist

        for animal_data in animals:
            pet = Animal(
                name=animal_data['name'],
                breed=animal_data['breed'],
                age=animal_data['age'],
                image=animal_data['image'],
                group_id=group.id  # Assign group_id to relate it to the AnimalGroup
            )
            db.session.add(pet)


    db.session.commit()
    print("Database seeded!")
